#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
allcountfile = sys.argv[1]
descountfile = sys.argv[2]

psxcode = []
psxdesc_count = []
psxdesc_countdesc = []
with open(descountfile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        psxcode.append(l1_split[0])
        psxdesc_count.append(l1_split[1].strip('\n'))
        psxdesc_countdesc.append(l1_split[2].strip('\n'))

with open(allcountfile, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        code = l2_split[0].strip()
        if code in psxcode:
            ind = psxcode.index(code)
            sys.stdout.write(l2.strip('\n')+'\t'+psxdesc_count[ind]+'\t'+psxdesc_countdesc[ind]+'\n')
        else:
            sys.stdout.write(l2.strip('\n') + '\t' + "0\t0"+'\n')

