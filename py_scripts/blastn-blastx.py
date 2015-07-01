#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
blastn = sys.argv[1]
blastx = sys.argv[2]
open_blastn = open(blastn, 'r')
open_blastx = open(blastx, 'r')
f = open("blastn_blastx_taxonid.list",'w')

blastn_oldiv = []
blastn_list = []
for line in open_blastn:
    line_split = line.split('\t')
    blastn_oldiv.append(line_split[0])
    blastn_list.append(line.strip('\n'))

blastx_oldiv = []
blastx_sp = []
for line2 in open_blastx:
    line2_split = line2.split('\t')
    blastx_oldiv.append(line2_split[0])
    blastx_sp.append(line2_split[1].strip('\n'))

for k, xid in enumerate(blastx_oldiv):
    if xid in blastn_oldiv:
        print xid + " is in blastn"
    else:
        f.write(xid + "\t" + "\t" + "\t" + blastx_sp[k] +'\n')






