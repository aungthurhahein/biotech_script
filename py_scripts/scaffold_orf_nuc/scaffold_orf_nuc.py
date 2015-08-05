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

scaffold = sys.argv[1]
pep_orf = sys.argv[2]

scaffold_id = []
scaffold_seq = []
for seq_record in SeqIO.parse(scaffold, "fasta"):
    scaffold_id.append(str(seq_record.id))
    scaffold_seq.append(str(seq_record.seq))

with open(pep_orf, 'rb') as f1:
    for line in f1:
        if ">" in line:
            line_split = line.split('_')
            orf_id = line_split[0].strip('>')
            pos1 = int(line_split[1].split('-')[0].split('[')[1].strip())-1
            pos2 = int(line_split[1].split('-')[1].strip(']').strip().strip(']').strip(' (REVERSE SENSE)').strip(']'))-1
            if orf_id.strip() in scaffold_id:
                ind = scaffold_id.index(orf_id)
            if pos1 < pos2:
                sys.stdout.write(line)
                sys.stdout.write(scaffold_seq[ind][pos1:pos2]+'\n')
            elif pos1 > pos2:
                sys.stdout.write(line)
                seq_str = str(scaffold_seq[ind][pos2:pos1]) # get chunck by coordinates
                my_dna = Seq(seq_str, generic_dna)  # convert to dna object
                revseq = my_dna.reverse_complement()  # reverse complement
                sys.stdout.write(str(revseq)+'\n')






