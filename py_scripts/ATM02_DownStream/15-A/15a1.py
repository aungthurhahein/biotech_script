#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

filea = sys.argv[1]
fileb = sys.argv[2]

aid = []
acol2 = []
acol3 = []
with open(filea,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        aid.append(line_split[0].strip('>'))
        acol2.append(line_split[2])
        acol3.append(line_split[3])
o = open(fileb+"_15a",'w')
with open(fileb, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        qid = line2_split[1].strip('\n').strip()
        if qid in aid:
            ind = aid.index(qid)
            o.write(line2.strip('\n')+'\t'+acol2[ind]+'\t'+acol3[ind]+'\n')