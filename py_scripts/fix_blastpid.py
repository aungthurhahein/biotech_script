#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
blastp = sys.argv[1]

with open(blastp,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        qid = "c"+line_split[0].split('c')[1]
        tmp = qid
        for m in line_split[1:]:
            tmp +="\t"+m
        sys.stdout.write(tmp)
