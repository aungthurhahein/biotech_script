#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

oldtaxon = sys.argv[1]
newtaxon = sys.argv[2]

old_id = []
old_record = []
with open(oldtaxon, 'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        old_id.append(line_split[0].strip())
        old_record.append(line)

new_id = []
new_record = []
with open(newtaxon, 'r') as f2:
    for line in f2:
        line_split = line.split('\t')
        new_id.append(line_split[0].strip())
        new_record.append(line)

for x, oid in enumerate(old_id):
    if oid in new_id:
        ind = new_id.index(oid)
        sys.stdout.write(new_record[ind])
    else:
        sys.stdout.write(old_record[x])

