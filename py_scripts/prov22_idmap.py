#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
allid = sys.argv[1]

newid = []
oldid = []
with open(allid,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        newid.append(l1_split[1].strip('\n'))
        oldid.append(l1_split[0])

iduniq = list(set(newid))

for uid in iduniq:
        indexes = [i for i,e in enumerate(newid) if e == uid]
        oid = []
        for ind in indexes:
            # if len(oldid[ind].split('|')) > 2:
            #     oid_tmp = oldid[ind].split('|')[1]+"|"+oldid[ind].split('|')[2]
            # else:
            oid_tmp = oldid[ind]
            oid.append(oid_tmp)
        uniq_oid = list(set(oid))
        asid = "SgpatESTcmV3-"+uid
        sys.stdout.write(uid+'\t'+asid+'\t'+str(len(uniq_oid))+'\t'+';'.join(uniq_oid)+'\n')
