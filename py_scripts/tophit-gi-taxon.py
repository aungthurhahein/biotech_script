#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
giTaxon = sys.argv[1]
taxonDiv = sys.argv[2]
topHit = sys.argv[3]
opengiTaxon = open(giTaxon, 'r')
opentaxonDiv = open(taxonDiv, 'r')
opentopHit = open(topHit, 'r')

gi_list = []
taxon_list = []

for line in opengiTaxon:
    line_split = line.split('\t')
    gi_list.append(line_split[0].strip())
    taxon_list.append(line_split[1].strip())

taxondiv_list = []
sci_list = []
rank = []
div = []
for line2 in opentaxonDiv:
    line2_split = line2.split('\t')
    taxondiv_list.append(line2_split[0].strip())
    sci_list.append(line2_split[2].strip())
    rank.append(line2_split[3].strip())
    div.append(line2_split[4].strip())

queryid = []
gitopHit = []
for line3 in opentopHit:
    line3_split = line3.split('\t')
    queryid.append(line3_split[0].strip())
    gitopHit.append(line3_split[4].strip())

for it, gitop in enumerate(gitopHit):
    indices = [i for i, x in enumerate(gi_list) if x == gitop]
    for ind in indices:
        taxonid = taxon_list[ind]
        taxon_indices = [i for i, x in enumerate(taxondiv_list) if x == taxonid]
        for taxon_ind in taxon_indices:
            sys.stdout.write(queryid[it]) #Query ID
            sys.stdout.write('\t')
            sys.stdout.write(gitop) # GI
            sys.stdout.write('\t')
            sys.stdout.write(taxonid) # Taxon
            sys.stdout.write('\t')
            sys.stdout.write(sci_list[taxon_ind])
            sys.stdout.write('\t')
            sys.stdout.write(rank[taxon_ind])
            sys.stdout.write('\t')
            sys.stdout.write(div[taxon_ind]) # Div
            sys.stdout.write('\n')