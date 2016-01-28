#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
fpkmmatrix = sys.argv[1]

contig_id = []
norm_atmval = []
record_all = []
with open(fpkmmatrix,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        contig_id.append(l1_split[12].strip())
        norm_atmval.append(float(l1_split[10].strip()))
        record_all.append(l1)

uniq_contig = list(set(contig_id))

rmind = []
for c in uniq_contig:
    indexes = [i for i,e in enumerate(contig_id) if e == c]
    p = []
    for i in indexes:
        p.append(norm_atmval[i])
    res = ["y" for i in p if i > 0 ]    
    if len(res) == len(p):
        fp = 1
    else:
        fp = 0    
    if fp == 1:
        for i in indexes:                    
            rmind.append(i)
            sys.stdout.write(record_all[i].strip('\n')+"\t"+"p"+"\n")

for k in sorted(rmind, reverse=True):     
    del record_all[k]

for x in record_all:
    sys.stdout.write(x.strip('\n')+"\t"+"-"+"\n")

