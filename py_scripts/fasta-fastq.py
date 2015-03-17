#!/usr/bin/env python
"""
fasta(w qual) to fastq converter
Usage: python fasta_to_fastq.py reads.fasta reads.qual reads.fastq
__author__ = 'Aung ေအာင်သူရဟိန်း'
Date:12022015
"""

import sys
import os
from Bio import SeqIO
from Bio.SeqIO.QualityIO import PairedFastaQualIterator
# Get the shell arguments #
fa_path = sys.argv[1]
qa_path = sys.argv[2]
fq_path = sys.argv[3]
# Check that the path is valid #
if not os.path.exists(fa_path): raise Exception("No file at %s." % fa_path)
# Do it #
handle = open(fq_path, "w")
records = PairedFastaQualIterator(open(fa_path), open(qa_path))
count = SeqIO.write(records, handle, "fastq")
handle.close()
print "Converted %i records" % count
