#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
fastalength = sys.argv[1]
clstfile = sys.argv[2]
lt50 = sys.argv[3]
querycat = sys.argv[4]

qid = []
qlngth = []
with open(fastalength,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        qid.append(line_split[0].strip())
        qlngth.append(int(line_split[1].strip('\n')))

cluster = []
ofmem = []
ofATM01 = []
with open(lt50, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        cluster.append(line3_split[0].strip())
        ofmem.append(line3_split[1])
        ofATM01.append(line3_split[2])

clst = []
longATM01 = []
longATM01len = []
with open(clstfile, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        tmp_len = []
        tmp_id = []
        for x in line2_split[1:]:
            if x.strip('>').strip() in qid:
                tmp_id.append(x.strip('>').strip())
                tmp_len.append(qlngth[qid.index(x.strip('>').strip())])

        if len(tmp_id) > 0 and line2_split[0].strip() in cluster:
            maxlen = max(tmp_len)
            ind = tmp_len.index(max(tmp_len))
            maxid = tmp_id[ind]
            clst.append(line2_split[0].strip())
            longATM01.append(maxid)
            longATM01len.append(maxlen)
            sys.stdout.write(line2_split[0].strip()+"\t"+maxid+"\t"+str(maxlen)+"\n")
