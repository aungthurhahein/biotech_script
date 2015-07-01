#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

tophit = sys.argv[1]
blastx = sys.argv[2]

opentophit = open(tophit, 'r')
openblastx = open(blastx, 'r')

blastx_cat = []
queryid = []
gi = []
taxonid = []
division = []

for line in opentophit:
    line_split = line.split('\t')
    blastx_cat.append(line_split[0])
    queryid.append(line_split[3])
    gi.append(line_split[7])
    taxonid.append(line_split[9])
    division.append(line_split[12])
x_taxon = []
x_20div = []
for line2 in openblastx:
    line2_split = line2.split('\t')
    x_taxon.append(line2_split[0])
    x_20div.append(line2_split[5])
f = open("map_log",'w')
for k, tophittaxon in enumerate(taxonid):
    if tophittaxon in x_taxon:
        ind = x_taxon.index(tophittaxon)
        sys.stdout.write(blastx_cat[k])
        sys.stdout.write('\t')
        sys.stdout.write(queryid[k])
        sys.stdout.write('\t')
        sys.stdout.write(gi[k])
        sys.stdout.write('\t')
        sys.stdout.write(taxonid[k])
        sys.stdout.write('\t')
        sys.stdout.write(division[k])
        sys.stdout.write('\t')
        sys.stdout.write(x_20div[ind])
    else:
        f.write(tophittaxon)

