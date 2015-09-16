#!/usr/bin/env bash

#scripts location
step1script="/fs/home/card/blastscripts/bsecseq.pl"
step2blastx="/fs/home/card/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/fs/home/card/blastscripts/blstpSECqsubNoParse.pl"

# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
basedir="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast/"
outputloc="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast/fastafiles/"   # base dir of outputfile
prefix="trinitynonF.id.fasta_astranid.fasta"      # prefix of output files
outputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast/trinitynonF.id.fasta_astranid.fasta"  # input fastafile
inputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
