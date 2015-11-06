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
genus = sys.argv[2]

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    sys.stdout.write(">PV_ATM03_"+str(genus)+"-"+str(seq_record.id)+'\n')
    sys.stdout.write(str(seq_record.seq)+'\n')
