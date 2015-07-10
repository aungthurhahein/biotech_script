#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
gitaxon = sys.argv[1]
gidesc = sys.argv[2]

gi1 =[]
gi1taxon = []
with open(gitaxon, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        gi1.append(line_split[0])
        gi1taxon.append(line_split[1].strip('\n'))
gi2 = []
gi2desc = []
with open(gidesc, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        gi2.append(line2_split[0])
        gi2desc.append(line2_split[1])

for x,giid in enumerate(gi1):
    if giid in gi2:
        ind = gi2.index(giid)
        sys.stdout.write(giid+"\t"+gi1taxon[x]+"\t"+gi2desc[ind])