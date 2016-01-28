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

c01_trinity = sys.argv[1]
c01_mira = sys.argv[2]
colfile = sys.argv[3]

trinity_id = []
trinity_seq = []
mira_id = []
mira_seq = []

for seq_record in SeqIO.parse(c01_trinity, "fasta"):
    trinity_id.append(str(seq_record.id).strip())
    trinity_seq.append(str(seq_record.seq))

for seq_record in SeqIO.parse(c01_mira, "fasta"):
    mira_id.append(str(seq_record.id).strip())
    mira_seq.append(str(seq_record.seq))

with open(colfile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split()
        id_ = l1_split[1].strip('\n').strip()
        if l1_split[0].strip() == 'trinity':
            if id_ in trinity_id:
                ind = trinity_id.index(id_)
                sys.stdout.write(">trinity_"+id_+'\n')
                sys.stdout.write(trinity_seq[ind]+'\n')
        elif l1_split[0].strip() == 'mira':
            if id_ in mira_id:
                ind = mira_id.index(id_)
                sys.stdout.write(">mira_"+id_+'\n')
                sys.stdout.write(mira_seq[ind].upper()+'\n')
