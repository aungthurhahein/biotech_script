#! /usr/bin/env/ python

"""
# format blast_tophit into #Cat/QueryID/GI/TaxonID/Division/20_Division/Species
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
blast_tophit = sys.argv[1]
taxonfile = sys.argv[2]

catgroup=[]
queryid = []
gi = []
taxonid = []
with open(blast_tophit,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        catgroup.append(line_split[0])
        queryid.append(line_split[1])
        gi.append(line_split[5])
        taxonid.append(line_split[26].strip('\n'))

taxon_compare = []
division =  []
division20 = []
species = []
with open(taxonfile, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        taxon_compare.append(line2_split[0])
        species.append(line2_split[2])
        division.append(line2_split[4])
        division20.append(line2_split[5].strip('\n'))

for x, tid in enumerate(taxonid):
    if tid in taxon_compare:
        ind = taxon_compare.index(tid)
        sys.stdout.write(catgroup[x]+"\t"+queryid[x]+"\t"+gi[x]+"\t"+taxonid[x]+"\t"+division[ind]+"\t"+division20[ind]+"\t"+species[ind]+'\n')



