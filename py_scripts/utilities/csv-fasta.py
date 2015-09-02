#! /usr/bin/env/ python

"""
# 
# usage: convert csv to fasta format
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
csv_file = sys.argv[1]
open_csv = open(csv_file, 'r')

for line in open_csv:
    line_split = line.split(',')
    print ">"+line_split[0].strip('\"').strip()
    print line_split[1].strip('\"').strip('\"').strip()[:-1]