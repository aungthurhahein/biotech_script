#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]
capoutmap = sys.argv[2]

contig_id = []
org_atmid = []
with open(capoutmap,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        contig_id.append("Contig"+l1_split[0])  
        org_atmid.append(l1_split[1])

with open(mapfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        indexes = [i for i,e in enumerate(contig_id) if e == l2_split[0]]
        for i in indexes:
            sys.stdout.write(l2_split[0]+"\t"+org_atmid[i]+"\t"+l2_split[1]+"\n")



