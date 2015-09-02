#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import re

CClstfile = sys.argv[1]
FDescfile = sys.argv[2]
idmapfile = sys.argv[3]

clstrep = []
clst_allmem = []
with open(CClstfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        clstrep.append(line_split[0].strip('>'))
        clst_allmem.append(line_split[1].strip('>').strip('\n'))

trinity_id = []
astran_id = []
with open(idmapfile,'rb') as open_map:
    for line in open_map:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())

with open(FDescfile,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        repid = line2_split[0]
        if repid in trinity_id:
            astrrepid = astran_id[trinity_id.index(repid)]
        if astrrepid in clstrep:
            ind = clstrep.index(astrrepid)
            mem_split = clst_allmem[ind].split(';')
            for m in mem_split:
                e01 = re.search(r'PM_e0101\w+', m)
                if e01:
                    sys.stdout.write(m.strip('>')+'\t'+line2_split[1]+'\n')


