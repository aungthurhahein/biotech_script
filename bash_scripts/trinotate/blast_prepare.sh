#!/usr/bin/env bash

#scripts location
step1script="/fs/home/card/blastscripts/bsecseq.pl"
step2blastx="/fs/home/card/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/fs/home/card/blastscripts/blstpSECqsubNoParse.pl"
mkdir fastafiles && mkdir pepfiles

# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
basedir="/colossus/home/anuphap/Ortho20151125_Compare/fastafiles/"
outputloc="/colossus/home/anuphap/Ortho20151125_Compare/fastafiles/smallchunks_HI/"   # base dir of outputfile
prefix="RepSeq_allprot_HI"      # prefix of output files
outputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/pepfiles/"
prefixpep="pepfshort.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/colossus/home/anuphap/Ortho20151125_Compare/fastafiles/RepSeq_allprot_HI.fasta"  # input fastafile
inputpep="/fs/home/card/Aung/SIESTCM_CDHIT/StepT/blast2/pepfshort.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
