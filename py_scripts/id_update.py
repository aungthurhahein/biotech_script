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

id_file = sys.argv[1]
fasta_file = sys.argv[2]

open_id = open(id_file,'r')
existing_id =[]
updated_id = []

for x in open_id:
    x_split = x.split('\t')
    existing_id.append(x_split[0].strip())
    updated_id.append(x_split[1].strip())

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    if seq_record.id in existing_id:
        inx = existing_id.index(seq_record.id)
        updatedid = updated_id[inx]
        existingid = existing_id[inx]
        oldid_split = existingid.split('|')
        new_id = str(updatedid) + "|" + str(oldid_split[1]) + "|" + str(oldid_split[2])
        seq_record.id = new_id
    print ">"+seq_record.id
    print seq_record.seq
