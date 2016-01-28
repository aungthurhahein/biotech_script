#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

atmnonshrimpidlist = sys.argv[1]
cdhitclst = sys.argv[2]

atmnonshrimp_id = []
with open(atmnonshrimpidlist, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        atmnonshrimp_id.append(l1_split[0])

o1 = open(cdhitclst+"_y",'w')
o2 = open(cdhitclst+"_n",'w')
with open(cdhitclst,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        repid = l2_split[1].strip('>').strip()
        mem = l2_split[3].replace('>','').strip().strip('\n')

        notfound = "-"
        if repid not in atmnonshrimp_id:l
            notfound = repid

        if l2_split[3] != "\n":
            for m in mem.split('|'):
                m = m.strip('|').strip('>').strip().strip('\n')
                if m not in atmnonshrimp_id:
                    if notfound == "-":
                        notfound = m
                    else:
                        notfound += "|"+m

        if notfound == "-":
            o1.write(l2)
        else:
            o2.write(l2.strip('\n')+'\t'+notfound+'\n')
