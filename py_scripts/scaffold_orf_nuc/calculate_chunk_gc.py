#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
inputfasta = sys.argv[1] 
chunklist = sys.argv[2] 

seq_id_list = []
seq_str_list = []
for seq_record in SeqIO.parse(inputfasta, "fasta"):    
    seq_id = (str(seq_record.id))       # seq id    
    seq_str = seq_record.seq     #seq string
    seq_id_list.append(seq_id)
    seq_str_list.append(seq_str)

with open(chunklist,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        cid = l2_split[0].strip()
        start = int(l2_split[2])
        end = int(l2_split[3].strip('\n'))        
        if cid in seq_id_list:            
            ind = seq_id_list.index(cid)
            cseq = seq_str_list[ind]
            sys.stdout.write(">"+cid+'\t['+str(start)+':'+str(end)+']\n')
            sys.stdout.write(str(cseq[start:end])+'\n')

            # C_count = cseq[start:end].count('C')                         # count C
            # G_count = cseq[start:end].count('G')                         # count G
            # cg_percentage = (float(C_count + G_count) / abs(end-start))*100        # CG%                    
            # sys.stdout.write(l2.strip('\n').strip()+'\t'+str(cg_percentage)+'\n')