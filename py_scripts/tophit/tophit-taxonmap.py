#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

taxon = sys.argv[1]
map = sys.argv[2]

taxon_id = []
taxon_species = []

with open(taxon,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        taxon_id.append(line_split[0])
        taxon_species.append(line_split[2])

map_record = []
map_taxonid = []
with open(map,'r') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        map_taxonid.append(line2_split[3])
        map_record.append(line2.strip('\n'))

for e,tid in enumerate(map_taxonid):
    if tid in taxon_id:
        ind = taxon_id.index(tid)
        sys.stdout.write(map_record[e]+"\t"+taxon_species[ind]+"\n")


