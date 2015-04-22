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

nucestfile = sys.argv[1]  # nucest
sequencefile = sys.argv[2]  # sequence
datasetfile = sys.argv[3]  # dataset

open_nucest = open(nucestfile, 'r')
open_dataset = open(datasetfile, 'r')

fasta_id = []
fasta_sequence = []
fasta_header = []
nucest_gi = []
nucest_libEST = []

for seq_record in SeqIO.parse(sequencefile, "fasta"):
    id_split = seq_record.id.split('|')
    fasta_id.append(id_split[1].strip())
    fasta_header.append(seq_record.id)
    fasta_sequence.append(seq_record.seq)

for line in open_nucest:
    line_split = line.split('\t')
    nucest_gi.append(line_split[0].strip())
    nucest_libEST.append(line_split[1].strip())

for libID in open_dataset:
    indices = [i for i, x in enumerate(nucest_libEST) if x == libID.strip()]
    for ind in indices:
        if nucest_gi[ind].strip() in fasta_id:
            seq_indx = fasta_id.index(nucest_gi[ind].strip())
            print fasta_header[seq_indx]
            print fasta_sequence[seq_indx]
