#----------------------------------------#
# filter sequence from list of ids from a text file
# modification tips: file type, column of file ids
# __author__ = 'atrx'
# Date: 20012014
#----------------------------------------#
import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

usage= "Usage %s infile" % sys.argv[0] #specific massage for no input
try:
    seqid = sys.argv[1]
    fastafile = sys.argv[2]
except:
    print usage, sys.exit(1)

seqid_read = open(seqid,'r')
final_records=[]

for id in seqid_read:
    id1 = id.split('>')
    print id1
    for seq_record in SeqIO.parse(fastafile,"fasta"):
        if seq_record.id.strip() == id1[1].strip():
            print seq_record
            final_records.append(seq_record)
else:
    seqid_read.close()
SeqIO.write(final_records,"{0}.fasta".format(seqid), "fasta")

