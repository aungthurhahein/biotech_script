#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

clstwithrep = sys.argv[1]  # cluster with repmem and others (cdhit-parser format 2)
clstlsit = sys.argv[2]

clst = []
rep = []
with open(clstwithrep, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        clst.append(line_split[0])
        rep.append(line_split[1])

with open(clstlsit,'rb') as f2:
    for line2 in f2:
        if line2.strip('\n').strip() in clst:
            ind = clst.index(line2.strip('\n').strip())
            sys.stdout.write(rep[ind]+'\n')
