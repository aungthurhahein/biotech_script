#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

idmap = sys.argv[1]
count = sys.argv[2]
tmm = sys.argv[3]
tmmnorm = sys.argv[4]

trinity_id = []
astran_id = []
with open(idmap,'rb') as f:
    for line in f:
        line_split = line.split('\t')
        trinity_id.append(line_split[0].strip().strip('>').split()[0].strip())
        astran_id.append(line_split[2].strip())


countid = []
countatm = []
countnonatm = []
tmmid = []
tmmatm = []
tmmnonatm = []
tmmnormid = []
tmmnormatm = []
tmmnormnonatm = []

with open(count, 'rb') as f1:
    for line1 in f1:
        line1_split = line1.split('\t')
        countid.append(line1_split[0])
        countatm.append(float(line1_split[1]))
        countnonatm.append(float(line1_split[2].strip('\n')))

with open(tmm, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        tmmid.append(line2_split[0])
        tmmatm.append(float(line2_split[1]))
        tmmnonatm.append(float(line2_split[2].strip('\n')))

with open(tmmnorm, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        tmmnormid.append(line3_split[0])
        tmmnormatm.append(float(line3_split[1]))
        tmmnormnonatm.append(float(line3_split[2].strip('\n')))


sys.stdout.write("Trinity_ID\
                \tAsTranID\
                \tcount.ATM\
                \tcount.nonATM\
                \tTMM.ATM\
                \tTMM.nonATM\
                \tTMMnorm.ATM\
                \tTMMnorm.nonATM\
                \td.count.ATM\
                \td.TMM.ATM\
                \td.TMMnorm.ATM\
                \tATMonly\n")

for x,tid in enumerate(trinity_id):
    tmp = tid+"\t"+astran_id[x]
    dcountatm = 0
    dtmmatm = 0
    dtmmmnormatm = 0

    if tid in countid:
        ind = countid.index(tid)
        tmp += "\t"+str(countatm[ind])+"\t"+str(countnonatm[ind])
        dcountatm = countatm[ind] - countnonatm[ind]

    if tid in tmmid:
        ind2 = tmmid.index(tid)
        tmp += "\t" + str(tmmatm[ind2]) + "\t" + str(tmmnonatm[ind2])
        dtmmatm = tmmatm[ind2] - tmmnonatm[ind2]

    if tid in tmmnormid:
        ind3 = tmmnormid.index(tid)
        tmp += "\t" + str(tmmnormatm[ind3]) + "\t" + str(tmmnormnonatm[ind3])
        dtmmnormatm = tmmnormatm[ind3] - tmmnormnonatm[ind3]

    tmp += "\t"+ str(dcountatm)+"\t"+str(dtmmatm)+"\t"+str(dtmmnormatm)
    atmonly = "-"

    if ((countatm[ind] > 0) or (tmmatm[ind2] > 0) or (tmmnormatm[ind3] > 0)) and ((countnonatm[ind] == 0) and (tmmnonatm[ind2] == 0) and (tmmnormnonatm[ind3] == 0)):
        atmonly="y"
    else:
        atmonly = "n"

    tmp += "\t"+atmonly

    sys.stdout.write(tmp+'\n')
