#! /usr/bin/env/ python

"""
# change rep cluser format file into astranID file with members
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

idmap = sys.argv[1]
repfile = sys.argv[2]

orgid = []
astranid = []
with open(idmap, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        orgid.append(l1_split[1].split('|')[0])
        astranid.append(l1_split[2])
o= open(repfile+"_astranid",'w')
with open(repfile, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        mem = l2_split[2].replace(">", "").strip('\n').split("|")
        uniq_mem = []
        for m in mem:
            m_split = m.split('|')[0]
            if m_split == "E01":
                print "it1"
            elif m_split == "E02":
                print "it2"
            elif m_split not in uniq_mem:
                uniq_mem.append(m_split)

        if l2_split[1].strip('>') in orgid:
            o.write(l2_split[0].strip('>')+'\t'+astranid[orgid.index(l2_split[1].strip('>'))]+'\t'+str(len(uniq_mem))+'\t'+l2_split[1].replace(">","")+"|"+ '|'.join(uniq_mem)+'\n')