#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
sheet = sys.argv[1]
mapfile = sys.argv[2]

allid = []
allid2 = []
allrecord = []
with open(sheet,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        allid.append(l1_split[2])            
        allid2.append(l1_split[7])            
        allrecord.append(l1.strip('\n').strip())    
allid = list(set(allid))
allid2 = list(set(allid2))

with open(mapfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        cid = l2_split[0]
        ind1 = [i for i,e in enumerate(allid) if e == cid]
        ind2 = [i for i,e in enumerate(allid2) if e == cid]
        for ind in ind1:            
            sys.stdout.write(cid+'\t'+l2)
        for ind2 in ind2:                        
            sys.stdout.write(cid+'\t'+l2)
        # else:
        #     sys.stdout.write(allrecord[ind]+'\n')




 cat blast2vh0/KritSSH01-Vh020150913.megablast.bls2seq.qc95.map blast2vh0/KritSSH01-Vh020150913.megablast.bls2seq.qcL95.map > blast2vhall/krit.all
 cat blast2vhs1/KritSSH01-vhs1.megablast.bls2seq.qc95.map  blast2vhs1/KritSSH01-vhs1.megablast.bls2seq.qcL95.map >> blast2vhall/krit.all
 cat blast2vh0/rescreESTs-Vh020150913.megablast.bls2seq.qc95.map blast2vh0/rescreESTs-Vh020150913.megablast.bls2seq.qcL95.map > blast2vhall/rescre.all
 cat blast2vhs1/rescreESTs-vhs1.megablast.bls2seq.qc95.map blast2vhs1/rescreESTs-vhs1.megablast.bls2seq.qcL95.map >> blast2vhall/rescre.all
