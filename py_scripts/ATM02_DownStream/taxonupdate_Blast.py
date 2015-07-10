#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
taxongi = sys.argv[1]
blasttophit = sys.argv[2]

taxon = []
gi = []
with open(taxongi, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        gi.append(line_split[0])
        taxon.append(line_split[1])

record = []
gilook = []
with open(blasttophit, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        gilook.append(line2_split[5])
        record.append(line2.strip('\n'))

for x, giid in enumerate(gilook):
    if giid in gi:
        ind = gi.index(giid)
        sys.stdout.write(record[x]+"\t"+taxon[ind])