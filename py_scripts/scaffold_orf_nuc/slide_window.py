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


for seq_record in SeqIO.parse(inputfasta, "fasta"):
    start = 0
    end = 200
    seq_str = (str(seq_record.seq))     #seq string
    seq_id = (str(seq_record.id))       # seq id
    length = len(seq_record.seq)        # seq len
    if length >= 200:
        while (end <= length):
            print seq_record.seq[start:end],length,start,end
            C_count = seq_record.seq[start:end].count('C')              # count C
            G_count = seq_record.seq[start:end].count('G')              # count G
            cg_percentage = (float(C_count + G_count) / 200)*100        # CG%                    
            sys.stdout.write(seq_id+"\t"+str(length)+'\t'+str(start)+'\t'+str(end)+'\t'+str(cg_percentage)+'\t'+'1'+'\n')            
            start += 1
            end += 1  
    else:
        C_count = seq_record.seq.count('C') 
        G_count = seq_record.seq.count('G') 
        cg_percentage = (float(C_count + G_count) / 200)*100   
        sys.stdout.write(seq_id+"\t"+str(length)+'\t'+'0'+'\t'+str(length)+'\t'+str(cg_percentage)+'\t'+'0'+'\n')
