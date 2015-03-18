#!/usr/bin/env python
"""
# -------------------------------------------------------------------------#
# To cut out fastq sequence with longer than xxx bp
# Usage
# $ fastq_cut_length.py xxx.fasta length(int)
# Dev: Aung
# Date: 05012015
#-------------------------------------------------------------------------#
"""
import sys
from Bio import SeqIO

# user parameters
fastq_file = sys.argv[1]
length = sys.argv[2]

final_records = []
for seq_record in SeqIO.parse(fastq_file, "fastq"):
    seq_len = len(seq_record.seq)
    if seq_len < int(length):
        final_records.append(seq_record)
    else:
        print seq_record.id,seq_len
SeqIO.write(final_records, "{0}_{1}_bp.fastq".format(fastq_file, length), "fastq")
