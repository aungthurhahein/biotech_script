#!/usr/bin/perl
use lib "$ENV{'HOME'}/perllib";
use strict;
use warnings;


#my $dirread = $ARGV[0];
my $f_nameori = shift @ARGV;  ## the whole path and prefix
my $f_blastpref = shift @ARGV;  ## the whole path /blxt
my $dir_qsub = shift @ARGV;  ## the whole path
my $f_db = shift @ARGV;  ## the whole path

my $extn = shift @ARGV;
my $dlength = shift @ARGV;  ## the whole path and prefix  the blast/actual-blst-file-directory/pref_XXXX.

my $strt = shift @ARGV;
my $endq = shift @ARGV;

my $pfxqsub = shift @ARGV;  ##anything for qsub in the same directory.

my @orifseq = split("/", $f_nameori);
my $blsxt_pref = $orifseq[-1];

print "@orifseq\n$blsxt_pref\n";

checkallpar();


sub checkallpar{

    my $fblast_dir = $f_blastpref;
    my $fseq = $f_nameori.".".fillspace(1, 4).".fasta";
    my $chkdb = 0;

    $chkdb = 1 if((-e $f_db . ".nhr" ) || (-e $f_db . ".phr" ) || (-e $f_db . ".nnd" ) || (-e $f_db . ".pnd" ) || (-e $f_db . ".00.phr" ) || (-e $f_db . ".00.nhr" ));

    print "$chkdb\n";

    if( (-e $fblast_dir) && (-e $fseq) && $chkdb){
        #       print "PASS\n";
        blast_subfile();
    }
    else{
        print "check $fblast_dir \n" if !(-e $fblast_dir);
        print "check $fseq \n" if !(-e $fseq);
        print "check $f_db \n" if !$chkdb;
    }

}


sub blast_subfile{

    my $start =  $strt;
    my $end =  $endq;

    my $f_pre = "cn".$pfxqsub;

    my $dir_qsubF = $dir_qsub;
    system("mkdir $dir_qsubF") if !(-e $dir_qsubF);
    my $f_qsub = $dir_qsubF."qsub.".$f_pre.".".$end.".sh";  ## this is the main qsub

    my $fblast_dir = $f_blastpref;
    my $dir_finmv = $fblast_dir."finmv/";

    system("mkdir $dir_finmv") if !(-e $dir_finmv);

    system("mkdir $fblast_dir") if !(-e $fblast_dir);
    open F, ">$f_qsub";
    print F "\#!/bin/sh\n";
    close F;

    system("chmod u+x $f_qsub");

    #    my $i =0;


    my %recntPrevJ;

    my $nbr_nodes = 15;

    my %qhosts = (

    0 => "compute-0-13",
    1 => "compute-0-14",
    2 => "compute-0-15",
    3 => "compute-0-8",
    4 => "compute-0-9",
    5 => "compute-0-8",
    6 => "compute-0-10",
    7 => "compute-0-17",
    8 => "compute-0-11",
    9 => "compute-0-7",
    10 => "Compute-0-7",
    11 => "Compute-0-13",
    12 => "Compute-0-9",
    13 => "compute-0-8",
    14 => "compute-0-9"
    );

##   Colossus
#    my $nbr_nodes = 10;
#
#    my %qhosts = (
#
#        0 => "compute-0-3",
#        1 => "compute-0-4",
#        2 => "compute-0-5",
#        3 => "compute-0-6",
#        4 => "compute-0-7",
#        5 => "compute-0-8",
#        6 => "compute-0-9",
#        7 => "compute-1-1",
#        8 => "compute-1-2",
#        9 => "compute-1-3"
#        );
#
#

    for(my $i = $start; $i <= $end; $i++){
        #    foreach my $orfsz (keys %orfs){
        #       $i++;
        my $f_sh = $dir_qsubF.$f_pre."_". fillspace($i, 4).".sh";
        my $rel_f = $f_pre."_". fillspace( $i, 4).".sh";

        my $fseq = $f_nameori.".".fillspace($i, 4).".fasta";
        #       my $fseq = $f_nameori.".fasta";

        my $fblast = $fblast_dir.$blsxt_pref.".". fillspace( $i, 4) .".".$extn.".blast";

#        my $line = "perl /fs/home/card/LinWork/byTri/e0102/stepw/blstV2225.EachSeqALL.pl blastp $f_db  $fseq $fblast  -outfmt 6 -max_target_seqs 50 -evalue 0.001 -soft_masking true -matrix BLOSUM45\n";

        my $line = "perl /colossus/home/anuphap/blastscripts/blstV2225.EachSeqALL.pl blastx $f_db  $fseq $fblast -task blastn  -outfmt 6 -max_target_seqs 500 -evalue 0.001  -dust no\n";

s 20 -evalue 0.001 -soft_masking true -matrix BLOSUM45\n";
        my $linemv = "mv $fblast $dir_finmv\n";

        my $fpreFinmv = $dir_finmv.$blsxt_pref;

        my $linesparse = "perl /colossus/home/anuphap/blastscript/blstNXSECParsetab.pl $fpreFinmv $i  $i $extn $dlength\n";


        my $qlx = $i % $nbr_nodes;

        my $qhx = $qhosts{$qlx};

        open F, ">>$f_qsub";
        if(defined($recntPrevJ{$qlx})){
            my $prevj = $recntPrevJ{$qlx};
            print F "qnbr=\$(qsub -l hostname=$qhx -hold_jid $prevj $rel_f)\n";
            print F "echo -e \"$rel_f\\t\"\$qnbr\n";
        }
        else{
            print F "qnbr=\$(qsub -l hostname=$qhx $rel_f)\n";
        my $qlx = $i % $nbr_nodes;

        my $qhx = $qhosts{$qlx};

        open F, ">>$f_qsub";
        if(defined($recntPrevJ{$qlx})){
            my $prevj = $recntPrevJ{$qlx};
            print F "qnbr=\$(qsub -l hostname=$qhx -hold_jid $prevj $rel_f)\n";
            print F "echo -e \"$rel_f\\t\"\$qnbr\n";
        }
        else{
            print F "qnbr=\$(qsub -l hostname=$qhx $rel_f)\n";
            print F "echo -e \"$rel_f\\t\"\$qnbr\n";
        }

        $recntPrevJ{$qlx} = $rel_f;

        close F;

        #=pod
        open Fx, ">$f_sh";
        print Fx "#\$ -S /bin/bash\n";
        print Fx "#\$ -cwd\n";
        print Fx ". /fs/home/card/.bashrc\n";
        print Fx ". /fs/home/card/.bash_proSysPerl\n";

        print Fx $line;
        print Fx $linemv;
        #       print Fx $linesparse;
        close Fx;
        system("chmod u+x $f_sh");
        #=cut
    }
}



sub fillspace{
    my $nbr = $_[0];
    my $lx = $_[1];

    while(($lx - length( $nbr)) > 0){
        $nbr = "0" .$nbr;
    }
    return $nbr;
}
