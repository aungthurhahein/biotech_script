#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
# https://twitter.com/heysarah/status/659714181709492224

import sys
import re
mapfile = sys.argv[1]

clstid = []
clst_psxcode = []
clst_desc = []
with open(mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clstid.append(l1_split[0])
        clst_psxcode.append(l1_split[6])
        clst_desc.append(l1_split[7])

uniq_psxcode = list(set(clst_psxcode))

for code in uniq_psxcode:
    indexes = [i for i,e in enumerate(clst_psxcode) if e == code ] # and clst_desc[i] != "-"
    sys.stdout.write(code+'\t'+str(len(indexes))+'\n')
    tmp_clstid =[]
    for i in indexes:
        if clstid[i] not in tmp_clstid:
            tmp_clstid.append(clstid[i])
    # sys.stdout.write(code+'\t'+str(len(list(set(tmp_clstid))))+'\n')
