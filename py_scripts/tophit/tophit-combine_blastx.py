#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

prev_combine = sys.argv[1]
blastx = sys.argv[2]

open_combine = open(prev_combine, 'r')
open_blastx = open(blastx, 'r')

queryid = []
record = []

blastxqueryid = []
group = []

f = open('combine.log', 'w')
o = open('5sourcescombine', 'w')
for line in open_combine:
    line_split = line.split('\t')
    queryid.append(line_split[0])
    record.append(line.strip('\n'))

for line2 in open_blastx:
    line2_split = line2.split('\t')
    if line2_split[0] == "#XC1":
        group.append("6B-"+line2_split[2].strip('\n'))
    elif line2_split[0] == "#XC2":
        group.append("6C-" + line2_split[2].strip('\n'))
    else:
        group.append("6A-" + line2_split[2].strip('\n'))
    blastxqueryid.append(">"+line2_split[1])

for x, qid in enumerate(queryid):
    if qid in blastxqueryid:
        ind = blastxqueryid.index(qid)
        sys.stdout.write(record[x].rstrip('\t')+"\t"+group[ind]+"\n")
        o.write(record[x].rstrip('\t')+"\t"+group[ind]+"\n")
        f.write(qid+"of category"+group[ind]+"in blastx"+'\n')
    else:
        o.write(record[x].rstrip('\t') + "\t-\n")
        sys.stdout.write(record[x].rstrip('\t') + "\t-\n")
