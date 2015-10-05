#!/usr/bin/env bash

#scripts location
step1script="/fs/home/card/blastscripts/bsecseq.pl"
step2blastx="/fs/home/card/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/fs/home/card/blastscripts/blstpSECqsubNoParse.pl"
mkdir fastafiles && mkdir pepfiles

# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
basedir="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/"
outputloc="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/fastafiles/"   # base dir of outputfile
prefix="trinityfshort.id.fasta_astranid.fasta"      # prefix of output files
outputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/pepfiles/"
prefixpep="pepfshort.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/trinityfshort.id.fasta_astranid.fasta"  # input fastafile
inputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/pepfshort.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
