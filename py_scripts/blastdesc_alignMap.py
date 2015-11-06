#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

align_desc = sys.argv[1]
align_map = sys.argv[2]

accession_id = []
accession_desc = []
with open(align_desc, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        accession_id.append(l1_split[7].strip('\n').strip('\r'))
        accession_desc.append(l1_split[1].strip('\n').strip('\r'))

with open(align_map, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split(',')
        subID = l2_split[1].split('|')[3].strip()
        # subID = l2_split[0]
        # print subID
        tmp = "-"
        if subID in accession_id:
            tmp = accession_desc[accession_id.index(subID)]
        sys.stdout.write(l2.strip('\n').strip('\r')+','+tmp+'\n')
