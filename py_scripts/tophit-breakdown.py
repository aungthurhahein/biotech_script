#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

divquery = sys.argv[1]
opendivquery = open(divquery,'r')

for line in opendivquery:
    line_split = line.split('\t')
    group_id = line_split[0].strip().strip('\n')
    group_cat = line_split[5].strip().strip('\n')
    query_name = "6A-"
    sys.stdout.write(group_id)
    sys.stdout.write('\t')
    sys.stdout.write(query_name+group_cat)
