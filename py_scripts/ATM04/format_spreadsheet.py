#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
catorder = sys.argv[1]
catx_output = sys.argv[2]

catx_id = []
catx_record = []
with open(catx_output,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')        
        catx_id.append(l1_split[1])
        catx_record.append(l1)

tmp_ind = []
with open(catorder,'rb') as f2:
    for l2 in f2:
        l2 = l2.strip('\n')
        if l2 in catx_id:
            ind = catx_id.index(l2)
            sys.stdout.write(catx_record[ind])
            tmp_ind.append(ind)
        else:
            sys.stdout.write("D\t"+l2+"\t0\t0\n")

for k in sorted(tmp_ind, reverse=True):     
    del catx_record[k]

print catx_record