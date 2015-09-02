#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
speciesfile = sys.argv[1]
a2file = sys.argv[2]

aid= []
aspecies = []
with open(speciesfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        for x in line_split[3].split(';'):
            aid.append(x.strip().strip('-N').strip('-X'))
            aspecies.append(line_split[1])

with open(a2file,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        for m in line2_split[4].split('|'):
            sp = ""
            inds = [i for i,e in enumerate(aid) if e == m.strip()]
            for ind in inds:
                if sp == "":
                    sp = aspecies[ind]
                else:
                    sp += ";"+aspecies[ind]

            print line2.strip('\n')+'\t'+sp


