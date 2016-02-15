#!/usr/bin/env bash

#scripts location
step1script="/colossus/home/anuphap/blastscripts/bsecseq.pl"
step2blastx="/colossus/home/anuphap/blastscripts/blstxSECqsubNoParse.pl"
step2blastp="/colossus/home/anuphap/blastscripts/blstpSECqsubNoParse.pl"
mkdir fastafiles && mkdir pepfiles
# step 1: splitting files

#---------------These variables need to adjust-------------------------------#
    basedir="/colossus/home/anuphap/Ortho20151125-HI/"
outputloc="/colossus/home/anuphap/Ortho20151125-HI/fastafiles/"   # base dir of outputfile
prefix="RepSeq_allprot_HI.fasta"      # prefix of output files
outputpep="/colossus/home/anuphap/e0106/blast/pepfiles/"
prefixpep="pepnonF.id.fasta_astranid.fasta"
seqsize="200"  #size to split fasta file
inputfasta="/colossus/home/anuphap/Ortho20151125-HI/RepSeq_allprot_HI.fasta"  # input fastafile
inputpep="/colossus/home/anuphap/e0106/blast/pepnonF.id.fasta_astranid.fasta"  # input pepfile
#---------------These variables need to adjust-------------------------------#

perl $step1script $outputloc$prefix $seqsize $inputfasta
perl $step1script $outputpep$prefixpep $seqsize $inputpep
