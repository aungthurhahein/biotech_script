#!/usr/bin/env bash

#scripts location
step1script="/colossus/home/anuphap/blastscripts/bsecseq.pl"
step2blastx="/colossus/home/anuphap/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/colossus/home/anuphap/blastscripts/blstpSECqsubNoParse.pl"
mkdir fastafiles && mkdir pepfiles
# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
basedir="/colossus/home/anuphap/e0106/blast/"
outputloc="/colossus/home/anuphap/e0106/blast/fastafiles/"   # base dir of outputfile
prefix="trinitynonF.id.fasta_astranid.fasta"      # prefix of output files
outputpep="/colossus/home/anuphap/e0106/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/colossus/home/anuphap/e0106/blast/trinitynonF.id.fasta_astranid.fasta"  # input fastafile
inputpep="/colossus/home/anuphap/e0106/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
