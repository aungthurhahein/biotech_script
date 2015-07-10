#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
gilist = sys.argv[1]
gi_taxon = sys.argv[2]

gi_list = []
with open(gilist,'rb') as f1:
    for line in f1:
        gi_list.append(line.strip('\n'))

gilookup=[]
taxonlookup = []

with open(gi_taxon,'rb') as f2:
    for line2 in f2:
        line_split = line2.split('\t')
        gilookup.append(line_split[0])
        taxonlookup.append(line_split[1])

res = []
for gi in gi_list:
    if gi in gilookup:
        res.append(taxonlookup[gilookup.index(gi)])

for x in list(set(res)):
    print x
