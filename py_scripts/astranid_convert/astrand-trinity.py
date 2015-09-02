#! /usr/bin/env/ python

"""
# to convert fasta file from trinity id to astranid id
# usage:
# output: stdout.save as fasta file
# Dev: __author__ = 'aung'
# Date: 07052015
"""
import sys
from Bio import SeqIO

org_fasta = sys.argv[1] # astranid fastafile
map_file = sys.argv[2]  # map file(Column 1:TrinityID, Column 3: AsTranID)
org_id = []
org_sequence = []
open_map = open(map_file, 'r')
o = open(org_fasta+"_trinity.fasta", 'w')

for seq_record in SeqIO.parse(org_fasta, "fasta"):
    org_id.append(str(seq_record.id).strip())
    org_sequence.append(str(seq_record.seq))

trinity_id = []
astran_id = []
for line in open_map:
    line_split = line.split('\t')
    trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
    astran_id.append(line_split[2].strip())

for x, asid in enumerate(astran_id):
    if asid in org_id:
        ind = org_id.index(asid)
        o.write(">" + trinity_id[x] +"\n")
        o.write(org_sequence[ind] + "\n")
