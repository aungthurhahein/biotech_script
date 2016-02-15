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
# genus = sys.argv[2]

o= open(fasta_file+"_map",'w')
count =0

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    newid = ">PV_ATM06_CDF-"+str(count)
    sys.stdout.write(newid+'\n')
    sys.stdout.write(str(seq_record.seq)+'\n')
    o.write(str(seq_record.id)+'\t'+newid+'\t'+"CAP3DF"+"\t"+"ATM04_Task26-A"+'\n')
    count += 1