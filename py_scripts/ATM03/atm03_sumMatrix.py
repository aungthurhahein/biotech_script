#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

qlenfile = sys.argv[1]
blastn = sys.argv[2]
blastx = sys.argv[3]

nid = []
n_div = []
with open(blastn, "rb") as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        nid.append(l1_split[1])
        n_div.append(l1_split[2].strip('\n'))

xid = []
x_div = []
with open(blastx, "rb") as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        xid.append(l2_split[1])
        x_div.append(l2_split[2].strip('\n'))

with open(qlenfile, 'rb') as f3:
    for f3 in f3:
        f3_split = f3.split('\t')
        tmp = f3_split[0]+'\t'+f3_split[1].strip('\n')


        # blastn
        if f3_split[0] in nid:
            tmp += "\t"+n_div[nid.index(f3_split[0])]
        else:
            tmp += "\t-"

            # blastx
        if f3_split[0] in xid:
            tmp += "\t" + x_div[xid.index(f3_split[0])]
        else:
            tmp += "\t-"

        if (f3_split[0] in xid) or (f3_split[0] in nid):
            sys.stdout.write(tmp+'\n')