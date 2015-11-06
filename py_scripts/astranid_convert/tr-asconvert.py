#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
trfile = sys.argv[1]
idmapfile = sys.argv[2]

trinity_id = []
astran_id = []
with open(idmapfile,'rb') as open_map:
    for line in open_map:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())

with open(trfile,'rb') as f:
    for line in f:
        line_split = line.split('\t')
        if line_split[0] in trinity_id:
            ind = trinity_id.index(line_split[0])
            sys.stdout.write(astran_id[ind]+"\t"+line_split[1]+'\n')