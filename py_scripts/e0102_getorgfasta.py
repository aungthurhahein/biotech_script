# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-16 15:51:34
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-16 16:53:46
import sys
from Bio import SeqIO
idlist = sys.argv[1]
fastafile = sys.argv[2]

fasta_rec = {}
for seq_record in SeqIO.parse(fastafile, "fasta"):
    fasta_rec[str(seq_record.id)] = str(seq_record.seq)
out = open(idlist+".fasta",'w')
with open(idlist, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        aung_id = l1_split[1].strip()
        org_id = l1_split[2].strip()
        if aung_id in fasta_rec:
            out.write(">"+org_id+"\n")
            out.write(fasta_rec[aung_id]+"\n")

