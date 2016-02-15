#!/usr/bin/env bash

#scripts location
step1script="/colossus/home/anuphap/blastscripts/bsecseq.pl"
step2blastx="/colossus/home/anuphap/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/colossus/home/anuphap/blastscripts/blstpSECqsubNoParse.pl"

#---------------These variables need to adjust-------------------------------#
# Hint: copy from blast_prepare.sh
basedir="/colossus/home/anuphap/ATM04-Task27/infiles/"
outputloc="/colossus/home/anuphap/ATM04-Task27/infiles/fastafiles/"   # base dir of outputfile
prefix="ATM04-Task27.fasta"      # prefix of output files
outputpep="/colossus/home/anuphap/e0106/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/colossus/home/anuphap/ATM04-Task27/infiles/ATM04-Task27.fasta"  # input fastafile
inputpep="/colossus/home/anuphap/e0106/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile
#---------------------------------------------------#

# step 2.1: generating qsub files and a wrapper to submit jobs (BLASTX)

# input
inputfiles=$outputloc
prefix2=$prefix

# some likely to stable files path and variables
#---->
blasttype="blstx"
db90="/colossus/home/anuphap/trinotate_req/uniprot_uniref90/uniprot_uniref90.trinotate.pep"
db="/colossus/home/anuphap/trinotate_req/uniport_sprot/uniprot_sprot.trinotate.pep"

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
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  1 20 UniPorta
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  21 40 UniPortb
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  41 60 UniPortc
perl $step2blastx $inputfiles$prefix2 $outputdir $qsubout $db $blasttype  61 77 UniPortd


perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  1 20 UniRef90a
perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  21 40 UniRef90b
perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  41 60 UniRef90c
perl $step2blastx $inputfiles$prefix2 $outputdir90 $qsubout90 $db90 $blasttype  61 77 UniRef90d

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


perl $step2blastp $inputfiles$prefix3 $outputdir $qsubout $db $blasttype  1 20 UniPorta
perl $step2blastp $inputfiles$prefix3 $outputdir $qsubout $db $blasttype  21 31 UniPortb


perl $step2blastp $inputfiles$prefix3 $outputdir90 $qsubout90 $db90 $blasttype  1 20 UniRef90a
perl $step2blastp $inputfiles$prefix3 $outputdir90 $qsubout90 $db90 $blasttype  21 31 UniRef90b


#---------------------------------------------------#ls

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

