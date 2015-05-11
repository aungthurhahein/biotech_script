#! /usr/bin/env/ python

"""
# to convert fasta file from orgid to astranid
# usage:
# output: stdout.save as fasta file
# Dev: __author__ = 'aung' 
# Date: 07052015
"""
import sys
from Bio import SeqIO

org_fasta = sys.argv[1]
map_file = sys.argv[2]  # two columns orgID-AstranID
org_id = []
org_sequence = []
open_org = open(org_fasta, 'r')
open_map = open(map_file, 'r')

for seq_record in SeqIO.parse(org_fasta, "fasta"):
    org_id.append(seq_record.id)
    org_sequence.append(seq_record.seq)

for line in open_map:
    line_split = line.split('\t')
    orgid = line_split[0].strip()
    astranid = line_split[1].strip()
    if orgid in org_id:
        ind = org_id.index(orgid)
        print ">"+astranid
        print org_sequence[ind]


