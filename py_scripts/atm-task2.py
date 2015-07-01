#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
map = sys.argv[1]
rsem = sys.argv[2]
open_rsem = open(rsem, 'r')
open_map = open(map, 'r')

trinityid = []
astranid = []
for line in open_map:
    line_split = line.split('\t')
    trinityid.append(line_split[1].strip())
    astranid.append(line_split[2].strip())

rsem_list = []
for line2 in open_rsem:
    rsem_list.append(line2.strip('\n'))

for x in rsem_list:
    x_split = x.split('\t')
    if x_split[0].strip() in trinityid:
        ind = trinityid.index(x_split[0].strip())
        del trinityid[ind]
        del astranid[ind]
        # sys.stdout.write(astranid[ind])
        # sys.stdout.write('\t')
        # sys.stdout.write(x)
        # sys.stdout.write('\n')
    # else:
    #     sys.stdout.write(x)
    #     sys.stdout.write('\n')

for k,tri in enumerate(trinityid):
    sys.stdout.write(astranid[k])
    sys.stdout.write('\t')
    sys.stdout.write(tri)
    sys.stdout.write('\n')