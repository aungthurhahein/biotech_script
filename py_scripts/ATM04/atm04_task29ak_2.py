#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
maplist = sys.argv[1]
fpkmmatrix = sys.argv[2]

contig_id = []
atm_id = []
with open(maplist,'rb') as f2:
    for l2 in f2:
        atm_id.append(l2.split('\t')[1].strip())
        contig_id.append(l2.split('\t')[2].strip())
        
with open(fpkmmatrix,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        if l3_split[1] in atm_id:
            ind = atm_id.index(l3_split[1])
            sys.stdout.write(l3.strip()+"\t"+contig_id[ind]+"\n")
        else:
            sys.stdout.write(l3.strip()+"\t-\n")

