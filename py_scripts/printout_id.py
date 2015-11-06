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

with open(idmap, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        tmp = ""
        for x,m in enumerate(l1_split):
            if x == 4:
                m_split = m.split('|')
                tmp += "\t" + m_split[1]
            elif x == 0:
                tmp = m
            else:
                tmp += "\t" + m
        sys.stdout.write(tmp)


        # sys.stdout.write(l1.strip('\n')+"\t"+l1_split[0]+"\n")
