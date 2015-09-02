#! /usr/bin/env/ python

"""
# fasta to tsv converter
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
from Bio import SeqIO
fasta_file = sys.argv[1]

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    sys.stdout.write(str(seq_record.id)+"|Penaeus_vannamei"+'\t'+str(seq_record.seq)+'\n')
