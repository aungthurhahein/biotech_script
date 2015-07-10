#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
from Bio import SeqIO

fileA = sys.argv[1]
fileB = sys.argv[2]
fastafile = sys.argv[3]
filA_id = []
fileA_atm98 = []
fileA_record = []
with open(fileA,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        filA_id.append(line_split[0])
        fileA_atm98.append(line_split[2])
        fileA_record.append(line.strip('\n'))

fileB_id = []
fileB_nonShrimp = []
with open(fileB,'r') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        fileB_id.append(line2_split[0])
        fileB_nonShrimp.append(line2_split[1])

seq_recordid = []
seq = []
for seq_record in SeqIO.parse(fastafile, "fasta"):
    seq_recordid.append(seq_record.id)
    seq.append(str(seq_record.seq))

for x,Aid in enumerate(filA_id):
    if Aid in fileB_id:
        if fileA_atm98[x].strip() == fileB_nonShrimp[fileB_id.index(Aid)] == "y":
            if Aid.strip('>') in seq_recordid:
                sys.stdout.write(Aid+'\n')
                ind = seq_recordid.index(Aid.strip('>'))
                sys.stdout.write(seq[ind]+'\n')
