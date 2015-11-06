#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
topfile = sys.argv[1]
groupmem = sys.argv[2]

clustid = []
desc = []

with open(topfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clustid.append(l1_split[0])
        tmp = ""
        for d in l1_split[1:]:
            if tmp == "":
                tmp = d.strip('\n')
            else:
                tmp += "\t"+d.strip('\n')
        desc.append(tmp)

with open(groupmem,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        comclstid = l2_split[0]
        if comclstid in clustid:
            ind = clustid.index(comclstid)
            sys.stdout.write(l2.strip('\n')+"\t"+desc[ind]+'\n')
        else:
            tmp ="-\t-\t-"
            sys.stdout.write(l2.strip('\n') + "\t" + tmp + '\n')

