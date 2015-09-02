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
descfile = sys.argv[2]
trinity_id = []
astran_id = []

with open(idmap,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())


with open(descfile,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        trid = line2_split[0].strip()
        if trid in trinity_id:
            ind = trinity_id.index(trid)
            desc=""
            if line2_split[1] != "NaN":
                desc += line2_split[1].lstrip("|")+"|"
            if line2_split[2] != "NaN":
                desc += line2_split[2]
            sys.stdout.write(astran_id[ind]+'\t'+desc+'\n')
