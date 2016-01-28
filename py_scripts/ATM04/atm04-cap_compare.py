#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]
task27 = sys.argv[2]
task27b = sys.argv[3]

atmid = []
capid = []
with open(mapfile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        atmid.append(l1_split[1])
        capid.append(l1_split[2].strip('\n').strip('>'))

atm0427B_id = []
atm0427B_catx = []
with open(task27b, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        atm0427B_id.append(l2_split[0])
        atm0427B_catx.append(l2_split[3].split('(')[0])

o1 = open('ASame','write')
o2 = open('PSame','write')
o3 = open('Diff','write')
with open(task27, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        qid = l3_split[0].strip()
        qcatx = l3_split[3].split('(')[0]
        if 'CDF' in qid:
            tmpid = []
            tmpcatx = []
            tmpid2 = []
            if qid in capid:
                indexes = [i for i,e in enumerate(capid) if e == qid]
                for i in indexes:
                    tmpid.append(atmid[i])
                for aid in tmpid:
                    if aid in atm0427B_id:
                        ind = atm0427B_id.index(aid)
                        tmpcatx.append(atm0427B_catx[ind])
                        tmpid2.append(atm0427B_id[ind])
                tmpval = 0
                for tmpx in tmpcatx:
                    if tmpx == qcatx:
                        tmpval = 1      #all
                    else:
                        tmpval = 0      #none
                if (tmpval == 0) and (qcatx in tmpcatx):
                        tmpval = 2      #subset

                print tmpid,tmpid2,qid,tmpcatx,qcatx,tmpval
                # print qid+'\t'+qcatx+'\t'+';'.join(tmpid2)+'\t'+';'.join(tmpcatx)
                if tmpval == 1:
                    o1.write(qid+'\t'+qcatx+'\t'+';'.join(tmpid)+'\t'+';'.join(tmpid2)+'\t'+';'.join(tmpcatx)+'\n')
                elif tmpval == 2: 
                    o2.write(qid+'\t'+qcatx+'\t'+';'.join(tmpid)+'\t'+';'.join(tmpid2)+'\t'+';'.join(tmpcatx)+'\n')
                else:
                    o3.write(qid+'\t'+qcatx+'\t'+';'.join(tmpid)+'\t'+';'.join(tmpid2)+'\t'+';'.join(tmpcatx)+'\n')
