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

usage = "Usage %s infile" % sys.argv[0]  # specific massage for no input
try:
    seqid = sys.argv[1]
    fastafile = sys.argv[2]
except:
    print usage, sys.exit(1)

seqid_read = open(seqid, 'r')
final_records = []
seq_id_file = []
fasta_content={}

for id in seqid_read:
    id1 = id.split('\t')
    seq_id_file.append(id1[0].strip())

for seq_record in SeqIO.parse(fastafile, "fasta"):
    id_number = seq_record.id.split('-')
    fasta_content[id_number[1].strip()] = seq_record

for seq_id in seq_id_file:
    print seq_id
    if seq_id in fasta_content:
        print seq_id
        final_records.append(fasta_content.get(seq_id))
SeqIO.write(final_records, "{0}.fasta".format(seqid), "fasta")
