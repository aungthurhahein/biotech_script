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
        for x,m in enumerate(l1_split[4].split('|')):
            sys.stdout.write(m.strip('\n')+'\n')

