#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
maxfile = sys.argv[1]
lt50 = sys.argv[2]
querycat = sys.argv[3]

maxclust = []
maxid = []
with open(maxfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        maxclust.append(line_split[0])
        maxid.append(line_split[1])

cluster = []
ofmem = []
ofATM01 = []
with open(lt50, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        cluster.append(line3_split[0].strip())
        ofmem.append(line3_split[1])
        ofATM01.append(line3_split[2])

qcid = []
qcrecords = []
with open(querycat, 'rb') as f4:
    for line4 in f4:
        line4_split = line4.split('\t')
        qcid.append(line4_split[0].strip().strip('>'))
        qcrecords.append(line4.strip('\n'))

f = open("NOT_nonshrimpANDATM01specific.res",'w')
for x,clusterid in enumerate(cluster):
    tmp = clusterid + "\t" + ofmem[x] + "\t" + ofATM01[x]
    if clusterid in maxclust:
        inx = maxclust.index(clusterid)
        if maxid[inx].strip() in qcid:
            ind2 = qcid.index(maxid[inx])
            tmp += "\t"+qcrecords[ind2]
            sys.stdout.write(tmp+'\n')
        else:
            f.write(tmp+"\n")

