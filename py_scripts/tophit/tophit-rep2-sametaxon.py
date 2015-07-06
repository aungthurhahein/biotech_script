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

uniq_qid = list(set(qid))
for queryid in uniq_qid:
    indexes = [i for i,e in enumerate(qid) if e == queryid]
    tmp_c1 = []
    tmp_c2 = []
    for i in indexes:
        if catgroup[i] == "#XC1":
            tmp_c1.append(i)
        elif catgroup[i] == "#XC2":
            tmp_c2.append(i)

    if len(tmp_c1) > 0:
        for c1 in tmp_c1:
            sys.stdout.write(mapfile_record[c1])
    elif len(tmp_c1) == 0 and len(tmp_c2) > 0:
        for c2 in tmp_c2:
            sys.stdout.write(mapfile_record[c2])


