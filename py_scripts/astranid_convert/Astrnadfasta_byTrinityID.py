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

org_fasta = sys.argv[1] # astranid formated fastafile
map_file = sys.argv[2]  # map file(Column 1:TrinityID, Column 3: AsTranID)
idfile = sys.argv[3]

org_id = []
org_sequence = []
for seq_record in SeqIO.parse(org_fasta, "fasta"):
    org_id.append(str(seq_record.id).strip())
    org_sequence.append(str(seq_record.seq))
print org_id

trinity_id = []
astran_id = []
with open(map_file,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())

with open(idfile,'rb') as f2:
    for line2 in f2:
        asid = line2.strip('>').strip().strip('\n')
        if asid in trinity_id:
            ind = trinity_id.index(asid)
            targetid = astran_id[ind]
            if targetid.strip() in org_id:
                print targetid
                sys.stdout.write(">"+targetid+'\n')
                sys.stdout.write(org_sequence[org_id.index(targetid)] + '\n')
