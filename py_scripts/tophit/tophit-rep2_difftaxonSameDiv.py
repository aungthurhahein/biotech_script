#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]

catgroup = []
qid = []
mapfile_record = []
with open(mapfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        catgroup.append(line_split[0])
        qid.append(line_split[1])
        mapfile_record.append(line)

for x,queryid in enumerate(qid):
    if catgroup[x] == "#XCal":
        sys.stdout.write(mapfile_record[x])