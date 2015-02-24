#!/usr/bin/env python
"""
fastq to fasta and quality scores file converter
Usage: python fastq_to_fasta.py reads.fastq reads.fasta reads.qual
__author__ = 'aung'
Date:11022015
"""
import sys
import os
from Bio import SeqIO

# Get the shell arguments #
fq_path = sys.argv[1]
fa_path = sys.argv[2]
qa_path = sys.argv[3]
# Check that the path is valid #
if not os.path.exists(fq_path): raise Exception("No file at %s." % fa_path)
# Do it #
SeqIO.convert(fq_path, "fastq", qa_path, "qual")
SeqIO.convert(fq_path, "fastq", fa_path, "fasta")
print "File converted successfully!"