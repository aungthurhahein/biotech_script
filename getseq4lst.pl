#!/usr/bin/perl
use lib "$ENV{'HOME'}/perllib";
use strict;
use warnings;


#my $selx = shift @ARGV;

my $fsex = shift @ARGV; # "/home/anuphap/eclipse/EST/all4spp/TIK13/TIKrecut.all.ntnr.7550A50.lstrealFWRW.RMs.final.G.".$getX;
my $dbx = shift @ARGV; # "/home/anuphap/eclipse/EST/Tik/20100623/vectorrm/20101221TIKvectorcut.fasta.blstn.both.seq";
my $foutx = shift @ARGV; #"/home/anuphap/eclipse/EST/all4spp/TIK13/2p1/TIKrecut.G.".$getX.".".$selx.".fasta";

workseq();

sub workseq{
    open Fx, ">$foutx";
    open (FILEx, "$fsex") || die "Could not open file $fsex :$!\n";
    while (<FILEx>){
        chomp;
        if($_ !~ m/#/){
            my @info = split(/\t/, $_);
	    my $seqx = getfasta($info[0], $dbx) ;
	    print Fx ">", $info[0], "\n$seqx\n";
	    
        }       
    }
    close FILEx;
    close Fx;
    
    
}



sub getfasta{
    
    
    my $gix = $_[0];
    my $dbx = $_[1];
    my $seq = "";
    open (FILEINPUTx, "look_afasta2s \"$gix\" $dbx |") || die "Could not run look_afasta2s :$!\n";
    while (<FILEINPUTx>){
        chomp;
        if($_ !~ m/>/){
            $seq = $seq . $_;
        }
    }
    close FILEINPUTx;
    
    return ($seq);
}
