#!/usr/bin/env bash

#scripts location
step1script="/fs/home/card/blastscripts/bsecseq.pl"
step2blastx="/fs/home/card/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/fs/home/card/blastscripts/blstpSECqsubNoParse.pl"

# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
basedir="/fs/home/card/Aung/ATM03-Task23"
outputloc="/fs/home/card/Aung/ATM03-Task23/fastafiles/"   # base dir of outputfile
prefix="nonshrimpATM03_all.id.fasta"      # prefix of output files
outputpep="/fs/home/card/Aung/by_trinotate/e0101_trinotate/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/fs/home/card/Aung/ATM03-Task23/nonshrimpATM03_all.id.fasta"  # input fastafile
inputpep="/fs/home/card/Aung/by_trinotate/e0101_trinotate/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
