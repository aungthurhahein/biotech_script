"""
# get occurences of ref_ids by Lib_IDs
# modification tips: file type, column of file ids
# __author__ = 'atrx'
# Date: 22012015
"""

import sys
from Bio import SeqIO

usage = "Usage %s infile" % sys.argv[0]  # specific massage for no input
try:
    fastafile = sys.argv[1]
    contigid = sys.argv[2]
except:
    print usage, sys.exit(1)

fasta_file = open(fastafile, 'r')
ref_file = open(contigid, 'r')

id_list = []
contig_list = []
id_key = []

for l in ref_file:
    id = l.split()
    id_list.append(l)
    id_key.append(id[1].strip())

for seq in SeqIO.parse(fasta_file, "fasta"):
    contig_list.append(seq.id)

for seq_record in contig_list:
    contigid = seq_record.strip()
    if contigid in id_key:
        lo = id_key.index(contigid)
        print id_list[lo].strip()
    else:
        print "0 " + seq_record
