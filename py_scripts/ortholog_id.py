#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

idmap = sys.argv[1]
orthofile = sys.argv[2]

meid = []
orgid = []
with open(idmap, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        meid.append(l1_split[1])
        orgid.append(l1_split[3].strip('\n'))
o = write()
with open(orthofile, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        idlook = l2_split[2].strip('\n').split(';')
        allorgid = ""
        for m in idlook:
            if m in meid:
                ind = meid.index(m)
                if allorgid == "":
                    allorgid = orgid[ind].replace('|', ';')
                else:
                    allorgid += ";"+orgid[ind].replace('|', ';')
        sys.stdout.write(l2_split[0]+'\t'+l2_split[1]+'\t'+allorgid.lstrip(';')+'\n')
