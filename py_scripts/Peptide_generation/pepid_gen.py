#! /usr/bin/env/ python

"""
# to convert peptide file into customized aspedid
# usage: pepid_gen.py AstranIDmapfile pepfile
# output: pep map file and pep file with new aspedid
# Dev: __author__ = 'aung' 
# Date: 20151007
"""
import sys
from Bio import SeqIO

astranmap = sys.argv[1]
pepfile = sys.argv[2]

trinity_id = []
astran_id = []
with open(astranmap, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        trinity_id.append(l1_split[0].split()[0].strip('>'))
        astran_id.append(l1_split[2])

pep_id = []
pep_trinity = []
pep_seq = []
pep_header = []
for seq_record in SeqIO.parse(pepfile, "fasta"):
    pid = str(seq_record.id)
    pep_trinity.append(pid.split('|')[0])
    pep_id.append(str(seq_record.id))
    pep_header.append(str(seq_record.description))
    pep_seq.append(str(seq_record.seq))

# output
o = open(pepfile+"_map", 'w')
o2 = open(pepfile+"_fmt", 'w')

for x, tid in enumerate(trinity_id):
    indexes = [i for i, e in enumerate(pep_trinity) if e == tid.strip()]
    for c,ind in enumerate(indexes):
        print astran_id[x], ind
        custom_pep = astran_id[x]+"_P"+str((str(c)).zfill(2))
        o.write(astran_id[x]+"\t"+tid+"\t"+str(len(indexes))+'\t'+pep_id[ind]+'\t'+custom_pep+'\n')
        o2.write(">"+custom_pep+" "+pep_header[ind]+'\n')
        o2.write(pep_seq[ind]+'\n')

print pepfile +" Done"


