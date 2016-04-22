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
o = open(fpkmmatrix+"_pass",'w')

with open(fpkmmatrix,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')        
        if (l1_split[12] == "-" and float(l1_split[10]) <= 0) or (l1_split[12] != "-" and l1_split[13] == "-\n"):
            sys.stdout.write(l1)
        else:
            o.write(l1)
