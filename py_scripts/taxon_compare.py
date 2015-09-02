#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
newlist = sys.argv[1]
existlist = sys.argv[2]

newtaxon = []
with open(newlist,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        newtaxon.append(line_split[0])
avbe
with open(existlist,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        if line2_split[0] in newtaxon:
            ind = newtaxon.index(line2_split[0])
            del newtaxon[ind]

for line in newtaxon:
    sys.stdout.write(line+"\n")