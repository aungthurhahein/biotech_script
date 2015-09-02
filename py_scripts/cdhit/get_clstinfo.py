#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

clustfile = sys.argv[1]
csvfile = sys.argv[2]

clst = []
clstmem = []
clstsize = []
with open(clustfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        for m in line_split[1:]:
            clst.append(line_split[0])
            clstmem.append(m.strip().strip('\n').strip('>'))
            clstsize.append(len(line_split))

with open(csvfile,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        if line2_split[0].strip() in clstmem:
            ind = clstmem.index(line2_split[0].strip())
            sys.stdout.write(clst[ind]+'\t'+str(clstsize[ind])+'\t'+line2)


