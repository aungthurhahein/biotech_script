#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

clstfile = sys.argv[1]

with open(clstfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        for x in line_split[1:]:
            sys.stdout.write(x.strip().strip('\n')+"\n")
