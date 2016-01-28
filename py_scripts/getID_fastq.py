#!/usr/bin/env python
"""
fasta(w qual) to fastq converter
Usage: python fasta_to_fastq.py reads.fasta reads.qual reads.fastq
__author__ = 'Aung'
Date:12022015
"""
import sys
import os
from Bio import SeqIO
from Bio.SeqIO.QualityIO import PairedFastaQualIterator

# Get the shell arguments #
idlist = sys.argv[1]
fq_file = sys.argv[2]

id_array = []
with open(idlist,'rb')  as f1:
    for l1 in f1:
        l1_split = l1.split()
        id_array.append(l1_split[0].strip('@'))

final_records = []
for seq_record in SeqIO.parse(fq_file, "fastq"):
    if str(seq_record.id) in id_array:
        final_records.append(seq_record)
SeqIO.write(final_records, "{0}_flt.fastq".format(fq_file), "fastq")
