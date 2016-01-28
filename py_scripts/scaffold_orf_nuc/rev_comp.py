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
     seq_str = (str(seq_record.seq))
     my_dna = Seq(seq_str, generic_dna)  # convert to dna object
     revseq = my_dna.reverse_complement()  # reverse complement
     sys.stdout.write(">"+str(seq_record.id)+'\n')
     sys.stdout.write(str(revseq)+'\n')


# python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/C01/C01_MIRA_id_map.txt c01_PM_out.unpadded.fasta_2Trinity.fasta.transdecoder.pep


    
    
