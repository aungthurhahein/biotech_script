#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import re
descfile = sys.argv[1]

clstid = []
clst_score = []
clst_desc = []
with open(descfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clstid.append(l1_split[0])
        clst_score.append(l1_split[1])
        clst_desc.append(l1_split[2].strip('\n'))

uniqclstid= set(list(clstid))

for clid in uniqclstid:
    indexes = [i for i,e in enumerate(clstid) if e == clid]
    tmp = clid
    if len(indexes) >= 3:
        for ind in indexes[0:3]:
            tmp += "\t" + clst_desc[ind]
        sys.stdout.write(tmp + '\n')
    else:
        for ind in indexes:
            tmp += "\t" + clst_desc[ind]
        if len(indexes) == 2:
            tmp += "\t-"
        elif len(indexes) == 1:
            tmp += "\t-\t-"
        sys.stdout.write(tmp+'\n')

        # out = re.sub(r'\{[^}]*\}', '', l1)
        # sys.stdout.write(out)
        # groupid = l1_split[1]
        # sys.stdout.write(">"+groupid+'\n')
        # mem = l1_split[3].split(';')
        # # if len(mem) == 1:
        # #     mem = l1_split[3].split('|')
        # for m in mem:
        #     if "{" in m:
        #         m = m.split('{')[0]
        #         sys.stdout.write(groupid + ">gi|X|ref|A| " + m.strip('\n') + '\n')
        #     elif "}" in m:
        #         m = m.split('}')[1]
        #         # sys.stdout.write(groupid + ">gi|X|ref|A| " + m.strip('\n') + '\n')
        #     elif m == "\n":
        #         m = m
        #     elif m == "":
        #         m = m
        #     else:
        #         sys.stdout.write(groupid+">gi|X|ref|A| "+m.strip('\n')+'\n')


