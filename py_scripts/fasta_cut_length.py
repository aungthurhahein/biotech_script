#!/usr/bin/env python
"""
# -------------------------------------------------------------------------#
# To cut out fasta sequence with longer than xxx bp
# Usage
# $ fasta_cut_length.py xxx.fasta length(int)
# Dev: Aung ေအာင်သူရဟိန်း
# Date: 05012015
#-------------------------------------------------------------------------#
"""
import sys
from Bio import SeqIO

# user parameters
fasta_file = sys.argv[1]
length = sys.argv[2]
final_records = []

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    seq_len = len(seq_record.seq)
    if seq_len < int(length):
        final_records.append(seq_record)
    else:
        print seq_record.id,seq_len
SeqIO.write(final_records, "{0}_{1}_bp.fasta".format(fasta_file, length), "fasta")
