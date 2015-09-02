#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
put_matrix = sys.argv[1]
atm03_matrix = sys.argv[2]

putid = []
putrecord = []
with open(put_matrix,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        putid.append(line_split[0])
        putrecord.append(line.strip('\n'))

nonshrimpid = []
nonshrimpval = []
with open(atm03_matrix,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        nonshrimpid.append(line2_split[0].strip('>'))
        nonshrimpval.append(line2_split[1].strip())

for pid,x in enumerate(putid):
    if pid in nonshrimpid:
        ind = nonshrimpid.index(pid)
        sys.stdout.write(putrecord[x]+'\t'+nonshrimpval[ind]+'\n')