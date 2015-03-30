#! /usr/bin/env/ python

"""
# change c01_mira id between 2 pairs
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
from Bio import SeqIO

id_map = sys.argv[1]
open_id_map = open(id_map,'r')
fastafile = sys.argv[2]
used_id = []
unused_id = []
final_records = []
for mira_id in open_id_map:
    id_split = mira_id.split('\t')
    used_id.append(id_split[0].strip())
    unused_id.append(id_split[1].strip())

for seq_record in SeqIO.parse(fastafile, "fasta"):
    header = seq_record.description.strip()
    if header in unused_id:
        print header
        tmp_indx = unused_id.index(header.strip())
        used_header = used_id[tmp_indx]
        seq_record.id = used_header.strip('>')
        seq_record.description = " "
    final_records.append(seq_record)
SeqIO.write(final_records, "{0}_usedid.fasta".format(fastafile), "fasta")