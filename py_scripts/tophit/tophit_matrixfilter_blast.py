#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

blastn = sys.argv[1]
blastx = sys.argv[2]
matrixfilter = sys.argv[3]

openblastn = open(blastn, 'r')
openblastx = open(blastx, 'r')
openfilter = open(matrixfilter, 'r')


blastn_id = []
blastn_record = []
for line in openblastn:
    line_split = line.split('\t')
    DorNot = line_split[0].split('-')[0]
    if DorNot == "#D":
        blastn_id.append(line_split[3])
        blastn_record.append(line)

blastx_id = []
blastx_record = []
for line2 in openblastx:
    line2_split = line2.split('\t')
    blastx_id.append(line2_split[1])
    blastx_record.append(line2)


for line3 in openfilter:
    line3_split = line3.split('\t')
    if len(line3_split) == 1:
        qid = line3_split[0].strip().strip('\n').strip('>')
        if qid !="//":
            print ">" + qid
        else:
            print qid
        blastn_ind = [i for i,e in enumerate(blastn_id) if e == qid]
        blastx_ind = [i for i, e in enumerate(blastx_id) if e == qid]
        for nind in blastn_ind:
            sys.stdout.write("#D\t"+blastn_record[nind])
        for xind in blastx_ind:
            sys.stdout.write("#X\t" + blastx_record[xind])
    else:
        if len(line3_split) == 7:
            sys.stdout.write("#B\t"+line3)
        else:
            sys.stdout.write("#A\t" + line3)




