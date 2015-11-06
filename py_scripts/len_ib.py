#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

seqlen = sys.argv[1]
idlist = sys.argv[2]

sid= []
slen = []
with open(seqlen, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        sid.append(l1_split[0])
        slen.append(l1_split[1].strip('\n'))


with open(idlist, 'rb') as f2:
    for l2 in f2:
        l2id = l2.strip('\n')
        if l2id in sid:
            sys.stdout.write(slen[sid.index(l2id)]+'\n')

