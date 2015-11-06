#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

idcount = sys.argv[1]
nuclorg = sys.argv[2]
protorg = sys.argv[3]


nucl_groupid = []
nucl_clusterid = []
nucl_memlen = []
with open(nuclorg, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        nucl_groupid.append(l2_split[0].strip())
        nucl_clusterid.append(l2_split[1].strip())
        nucl_memlen.append(str(len(l2_split[2].split(';'))))

prot_groupid = []
prot_clusterid = []
prot_memlen = []
with open(protorg, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        prot_groupid.append(l3_split[0].strip())
        prot_clusterid.append(l3_split[1].strip())
        prot_memlen.append(str(len(l3_split[2].split(';'))))

with open(idcount, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        groupid = (l1_split[0].strip())
        clusterid = (l1_split[1].strip())
        tmp_nuclcount = "0"
        tmp_protcount = "0"
        if clusterid in nucl_clusterid:
            ind = nucl_clusterid.index(clusterid)
            if nucl_groupid[ind] == groupid:
                tmp_nuclcount = nucl_memlen[ind]
        if clusterid in prot_clusterid:
            ind2 = prot_clusterid.index(clusterid)
            if prot_groupid[ind2] == groupid:
                tmp_protcount = prot_memlen[ind2]
        sys.stdout.write(l1.strip('\n')+'\t'+tmp_nuclcount+'\t'+tmp_protcount+'\n')
        # record.append(l1.strip('\n'))



