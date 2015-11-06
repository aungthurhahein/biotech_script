#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

matrix = sys.argv[1]
blastn = sys.argv[2]
blastx = sys.argv[3]

nqid = []
nspecies = []
with open(blastn, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        nqid.append(l1_split[1])
        nspecies.append(l1_split[3].strip('\n'))

xqid = []
xspecies = []
with open(blastx, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        xqid.append(l2_split[1])
        xspecies.append(l2_split[3].strip('\n'))

with open(matrix,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        qid = l3_split[0].strip()
        catx = l3_split[3].split('(')
        tmp = qid+"\t"
        if catx[1] == "X)":
            tmp += catx[0]+ "\t" +"X" +"\t" + xspecies[xqid.index(qid)]
        elif catx[1] == "N)":
            tmp += catx[0] + "\t" + "N" + "\t" + nspecies[nqid.index(qid)]

        sys.stdout.write(tmp+'\n')
