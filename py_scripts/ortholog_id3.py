#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

pool_map = sys.argv[1]
aung_map = sys.argv[2]
orthofile = sys.argv[3]

pool_id = []
pool_orgid = []
with open(pool_map, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        pool_id.append(l1_split[1])
        pool_orgid.append(l1_split[3].strip('\n').replace('|',';'))

aung_id = []
aung_orgid = []
with open(aung_map, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        aung_id.append(l2_split[1])
        aung_orgid.append(l2_split[3].strip('\n'))

with open(orthofile, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        mem = l3_split[2].strip('\n').split(';')
        tmpmem = ""
        for m in mem:
            if m.strip() in pool_id:
                if tmpmem == "":
                    tmpmem = pool_orgid[pool_id.index(m.strip())]
                else:
                    tmpmem += ";"+pool_orgid[pool_id.index(m.strip())]
            elif m.strip() in aung_id:
                if tmpmem == "":
                    tmpmem = aung_orgid[aung_id.index(m.strip())]
                else:
                    tmpmem += ";" + aung_orgid[aung_id.index(m.strip())]
            else:
                if tmpmem == "":
                    tmpmem = m.strip()
                else:
                    tmpmem += ";" + m.strip()
        sys.stdout.write(l3_split[0]+'\t'+l3_split[1]+'\t'+tmpmem.rstrip(';')+'\n')
