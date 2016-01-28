#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

map_file = sys.argv[1]  # map file(Column 1:TrinityID, Column 3: AsTranID)
blastout = sys.argv[2]

trinity_id = []
astran_id = []

with open(map_file,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())

with open(blastout,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        if line2_split[0].strip() in astran_id:
            trid = trinity_id[astran_id.index(line2_split[0].strip())]
            tmpout = trid+'\t'
            for x,m in enumerate(line2_split[1:]):
                if x == len(line2_split[1:])-1:
                    tmpout += m
                else:
                    tmpout += m+"\t"

            sys.stdout.write(tmpout)
