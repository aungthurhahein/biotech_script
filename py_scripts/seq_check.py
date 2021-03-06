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

orgfile = sys.argv[1]
checkfile = sys.argv[2]

org_id = []
org_sequence = []
check_id = []
check_sequence = []
f = open('fasta_check.log', 'w')

for seq_record in SeqIO.parse(orgfile, "fasta"):
    org_id.append(seq_record.id.strip())
    org_sequence.append(seq_record.seq.strip())

for seq_record in SeqIO.parse(checkfile, "fasta"):
    check_id.append(seq_record.id.strip())
    check_sequence.append(seq_record.seq.strip())

for x, seq in enumerate(org_sequence):
    if str(seq) == str(check_sequence[x]):
        print org_id[x], check_id[x]
    else:
        f.write(org_id[x]+'\n')
