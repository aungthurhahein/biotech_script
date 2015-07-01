#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

matrix5file = sys.argv[1]

blastn = []
blastx = []
record = []
with open(matrix5file,'r') as infile:
    for line in infile:
        line_split = line.split('\t')
        blastn.append(line_split[13].strip())
        blastx.append(line_split[14].strip())
        record.append(line)

f1 = open(matrix5file+"_same",'w')
f2 = open(matrix5file+"_diff",'w')
f3 = open(matrix5file+"_onlyN",'w')
f4 = open(matrix5file+"_onlyX",'w')
f5 = open(matrix5file+"_None",'w')
for x,n_rec in enumerate(blastn):
    x_rec = blastx[x]
    # None
    if n_rec == "-" and x_rec == "-":
        f5.write(record[x])
    elif n_rec != "-" and x_rec == "-":
        f3.write(record[x])
    elif n_rec == "-" and x_rec != "-":
        f4.write(record[x])
    # same cat
    elif n_rec != x_rec:
        f2.write(record[x])
    elif n_rec == x_rec:
        f1.write(record[x])
    else:
        print record[x]
