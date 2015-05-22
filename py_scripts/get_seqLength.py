"""
# get max/min seq length from fasta file
"""
__author__ = 'Aung'
import sys
from Bio import SeqIO

fasta_file = sys.argv[1]
result_file = open("{0}_lngth".format(fasta_file),'w')
length = []

for seq_record in SeqIO.parse(fasta_file, "fasta"):
    length.append(len(seq_record.seq))
    result_file.write(seq_record.id + "\t" + str(len(seq_record.seq))+"\n")

def avg(list):
    sum = 0
    for ele in list:
        sum += ele
    return sum/len(list)*1.0

print "Max length:", max(length)
print "Min length:", min(length)
print "Average length:", avg(length)

