#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

matrix = sys.argv[1]
a3file = sys.argv[2]

aid= []
ablastn = []
ablastx = []
with open(matrix,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        aid.append(line_split[0].strip('>').strip())
        ablastn.append(line_split[3].strip())
        # ablastx.append(line_split[2].strip('\n').strip())

with open(a3file,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        tmp = ""
        for m in line2_split[4].split('|'):
            if m.strip() in aid:
                ind = aid.index(m.strip())
                if tmp == "":
                    tmp = ablastn[ind] #+ ablastx[ind]
                else:
                    tmp += "|"+ ablastn[ind] #+ ";" + ablastx[ind]
        sys.stdout.write(line2.strip('\n')+"\t"+tmp+'\n')
