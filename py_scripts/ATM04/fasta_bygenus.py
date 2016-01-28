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
fastafile = sys.argv[1]
genuslist = sys.argv[2]

seq_id = []
seq_rec = []
for seq_record in SeqIO.parse(fastafile, "fasta"):
    seq_id.append(str(seq_record.id))
    seq_rec.append(str(seq_record.seq))

with open(genuslist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        group = l1_split[0]        
        genus = l1_split[1]      
        if "-X" in l1_split[5]:      
            o1 = open(genus+"-X.fasta",'w')
        if "-N" in l1_split[5]:      
            o2 = open(genus+"-N.fasta",'w')
        for x in l1_split[5].split(';'):
            id_ = x.strip().strip('\n').strip('-XN')
            if "-X" in x:
                if id_ in seq_id:
                    ind = seq_id.index(id_)
                    o1.write(">"+id_+"\n")
                    o1.write(seq_rec[ind]+"\n")
            else:
                if id_ in seq_id:
                    ind = seq_id.index(id_)
                    o2.write(">"+id_+"\n")
                    o2.write(seq_rec[ind]+"\n")



