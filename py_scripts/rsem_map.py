#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

rsem = sys.argv[1]
lst = sys.argv[2]

pv001 = "/fs/home/card/Aung/kw01/DE_Analysis_genes/diffExpr.P0.001_C1.matrix"
pv050 = "/fs/home/card/Aung/kw01/DE_Analysis_genes/diffExpr.P0.050_C1.matrix"
pv01 = "/fs/home/card/Aung/kw01/DE_Analysis_genes/diffExpr.P0.1_C1.matrix"
pv05 = "/fs/home/card/Aung/kw01/DE_Analysis_genes/diffExpr.P0.5_C1.matrix"
pv1 = "/fs/home/card/Aung/kw01/DE_Analysis_genes/diffExpr.P1_C1.matrix"


lspv001 = []
lspv050 = []
lspv05 = []
lspv1 = []
lspv01 = []
with open(pv001, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        lspv001.append(line_split[0].strip())

with open(pv050, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        lspv050.append(line2_split[0].strip())

with open(pv05, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        lspv05.append(line3_split[0].strip())
with open(pv01, 'rb') as f8:
    for line8 in f8:
        line8_split = line8.split('\t')
        lspv01.append(line8_split[0].strip())

with open(pv1, 'rb') as f4:
    for line4 in f4:
        line4_split = line4.split('\t')
        lspv1.append(line4_split[0].strip())

rsemid = []
rsemC = []
rsemM = []
rsemS = []
with open(rsem,'rb') as f5:
    for line5 in f5:
        line5_split = line5.split('\t')
        rsemid.append(line5_split[0])
        rsemC.append(line5_split[1])
        rsemM.append(line5_split[2])
        rsemS.append(line5_split[3].strip('\n'))

o = open(lst+".final", 'w')
with open(lst, 'rb') as fl:
    for linel in fl:
        linel_split = linel.split('\t')
        tranid = linel_split[2].strip().split('_')
        lstid = tranid[0]+"_"+tranid[1]
        if lstid in rsemid and linel_split[1] == "trinity":
            tmp = ''
            ind = rsemid.index(lstid)
            print lstid
            if lstid in lspv001:
                tmp += "0.001,"
            if lstid in lspv01:
                tmp += "0.1,"
            if lstid in lspv050:
                tmp += "0.50,"
            if lstid in lspv05:
                tmp += "0.5,"
            if lstid in lspv1:
                tmp += "1"
            o.write(linel.strip('\n') + '\t' + rsemC[ind] + '\t' + rsemM[ind] + '\t' + rsemS[ind] + '\t' + tmp + '\n')
        else:
            o.write(linel)

