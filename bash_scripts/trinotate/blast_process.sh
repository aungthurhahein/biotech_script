#!/usr/bin/env bash

#scripts location
step1script="/fs/home/card/blastscripts/bsecseq.pl"
step2blastx="/fs/home/card/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/fs/home/card/blastscripts/blstpSECqsubNoParse.pl"

#---------------These variables need to adjust-------------------------------#
# Hint: copy from blast_prepare.sh
basedir="/fs/home/card/Aung/ATM03-Task23/"
outputloc="/fs/home/card/Aung/ATM03-Task23/fastafiles/"   # base dir of outputfile
prefix="nonshrimpATM03_all.id.fasta"      # prefix of output files
outputpep="/fs/home/card/Aung/by_trinotate/e0101_trinotate/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/fs/home/card/Aung/ATM03-Task23/nonshrimpATM03_all.id.fasta"  # input fastafile
inputpep="/fs/home/card/Aung/by_trinotate/e0101_trinotate/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile

#---------------------------------------------------#

# step 2.1: generating qsub files and a wrapper to submit jobs (BLASTX)

# input
inputfiles=$outputloc
prefix2=$prefix

# some likely to stable files path and variables
#---->
blasttype="blstx"
db90="/fs/home/card/Aung/trinotate_req/uniprot_uniref90/uniprot_uniref90.trinotate.pep"
db="/fs/home/card/Aung/trinotate_req/uniport_sprot/uniprot_sprot.trinotate.pep"

# uniprot out
dir1="blastx/blastx_out/"
dir2="blastx/qsub.blastx_out/"
mkdir -p $basedir$dir1
mkdir -p $basedir$dir2
outputdir=$basedir$dir1
qsubout=$basedir$dir2

# uniRef90
dir3="blastx/blastx90_out/"
dir4="blastx/qsub.blastx90_out/"
mkdir -p $basedir$dir3
mkdir -p $basedir$dir4
outputdir90=$basedir$dir3
qsubout90=$basedir$dir4
#<-----------

#generate files
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  1 11 UniPorta
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  12 22 UniPortb

perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  1 11 UniRef90a
perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  12 22 UniRef90b

#---------------------------------------------------#

# step 2.2: generating qsub files and a wrapper to submit jobs (BLASTP)
# input

inputfiles=$outputpep
prefix3=$prefixpep
# some likely to stable files path and variables
#---->
# uniprot out
blasttype="blstp"

dir1="blastp/blastp_out/"
dir2="blastp/qsub.blastp_out/"
mkdir -p $basedir$dir1
mkdir -p $basedir$dir2
outputdir=$basedir$dir1
qsubout=$basedir$dir2

# uniRef90
dir3="blastp/blastp90_out/"
dir4="blastp/qsub.blastp90_out/"
mkdir -p $basedir$dir3
mkdir -p $basedir$dir4
outputdir90=$basedir$dir3
qsubout90=$basedir$dir4


perl $step2blastp $inputfiles$prefix3 $outputdir $qsubout $db $blasttype  1 3 UniPorta
perl $step2blastp $inputfiles$prefix3 $outputdir $qsubout $db $blasttype  4 7 UniPortb

perl $step2blastp $inputfiles$prefix3 $outputdir90 $qsubout90 $db90 $blasttype  1 3 UniRef90a
perl $step2blastp $inputfiles$prefix3 $outputdir90 $qsubout90 $db90 $blasttype  4 7 UniRef90b
#---------------------------------------------------#

#step 3: concat outputfiles to final ones
# blastx.outfmt6
# uniref90.blastx.outfmt6
#
# blastp.outfmt6
# uniref90.blastp.outfmt6

#for i in *.blast
#do
#    cat $i >> $1$out
#done

# count unique queryID
#cat uniref90.blastp.outfmt6 | awk '{split($1,a,"|"); print a[1]"|"a[2]}'
