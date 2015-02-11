"""
#----------------------------------------#
# filter sequence from list of ids from a text file
# modification tips: file type, column of file ids
# __author__ = 'atrx'
# Date: 20012014
#----------------------------------------#
"""
import sys
from Bio import SeqIO

usage= "Usage %s infile" % sys.argv[0]  # specific massage for no input
try:
    seqid = sys.argv[1]
    fastafile = sys.argv[2]
except:
    print usage, sys.exit(1)

seqid_read = open(seqid,'r')
final_records = []
seq_id_file = []

for id in seqid_read:
    id1 = id.split()
    seq_id_file.append(id1[0].strip())

for seq_record in SeqIO.parse(fastafile, "fasta"):
    if seq_record.id.strip() in seq_id_file:
        final_records.append(seq_record)
SeqIO.write(final_records, "{0}.fasta".format(seqid), "fasta")
