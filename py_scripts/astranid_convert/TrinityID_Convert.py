#! /usr/bin/env/ python
"""
# to convert fasta file from astranid id to  trinity id
# usage: TrinityID_Convert.py astranid.fasta idmap.txt transdecoder.pep
# output:
#           1. astranid.fasta_trinity.fasta # trinityID formatted fasta file
#           2. transdecoder.pep_trinity.pep # transdecoder.pep for corresponding
# Dev: __author__ = 'aung'
# Date: 21062015
"""

import sys
from Bio import SeqIO

org_fasta = sys.argv[1]
map_file = sys.argv[2]  # map file(Column 1:TrinityID, Column 3: AsTranID)
pep_file = sys.argv[3]

org_id = []
org_sequence = []
pep_trinityid = []
pep_id = []
pep_triid = []
pep_sequence = []
trinity_id = []
astran_id = []
open_map = open(map_file, 'r')
o = open(org_fasta+"_trinity.fasta", 'w')
p = open(pep_file+"_trinity.pep", 'w')

for seq_record in SeqIO.parse(org_fasta, "fasta"):
    org_id.append(str(seq_record.id).strip())
    org_sequence.append(str(seq_record.seq))

for seq_record2 in SeqIO.parse(pep_file, "fasta"):
    pepid = str(seq_record2.id)
    trinityid = pepid.split("|")[0]
    pepid += seq_record2.description
    pep_id.append(pepid.strip())
    pep_triid.append(trinityid.strip())
    pep_sequence.append(str(seq_record2.seq))

for line in open_map:
    line_split = line.split('\t')
    trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
    astran_id.append(line_split[2].strip())

for x, asid in enumerate(astran_id):
    if asid in org_id:
        ind = org_id.index(asid)
        o.write(">" + trinity_id[x] +"\n")
        o.write(org_sequence[ind] + "\n")
        if trinity_id[x] in pep_triid:
            pind = [i for i, e in enumerate(pep_triid) if e == trinity_id[x]]
            for indx in pind:
                p.write(">"+ pep_id[indx]+"\n")
                p.write(pep_sequence[indx]+"\n")
