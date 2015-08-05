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

final_records = []
seq_id_file = []
fasta_content={}

with open(seqid,'rb') as f1:
    for id in f1:
        id1 = id.split('\t')
        seq_id_file.append(id1[0].strip().strip('>'))

for seq_record in SeqIO.parse(fastafile, "fasta"):
    id_number = str(seq_record.id)
    fasta_content[id_number.strip()] = seq_record

for seq_id in seq_id_file:
    if seq_id in fasta_content:
        print seq_id
        final_records.append(fasta_content.get(seq_id))
SeqIO.write(final_records, "{0}.fasta".format(seqid), "fasta")
