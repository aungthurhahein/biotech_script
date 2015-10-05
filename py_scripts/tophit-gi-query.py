#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
catx = sys.argv[1]
blastx = sys.argv[2]
blastn = sys.argv[3]

x_id = []
n_id = []
x_cat = []
n_cat = []
with open(catx,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        xn = l1_split[3].split('(')[1].strip('\n')
        if xn == "X)":
            x_id.append(l1_split[0].strip('>'))
            x_cat.append(l1_split[2])
        elif xn == "N)":
            n_id.append(l1_split[0].strip('>'))
            n_cat.append(l1_split[1])

blastx_group = []
blastx_id = []
blastx_gi = []
blastx_taxon = []

with open(blastx,'rb') as f2:
    for l2 in f2:
        gp =" "
        l2_split = l2.split('\t')
        if l2_split[0] == "#XC1":
            gp = "6B"
        elif l2_split[0] == "#XC2":
            gp = "6C"
        elif l2_split[0] == "#XCal":
            gp = "6A"
        blastx_group.append(gp+"-"+l2_split[6])
        blastx_id.append(l2_split[1])
        blastx_gi.append(l2_split[2])
        blastx_taxon.append(l2_split[3])

blastn_group = []
blastn_id = []
blastn_gi = []
blastn_taxon = []

with open(blastn,'rb') as f3:
    for l3 in f3:
        gp = " "
        l3_split = l3.split('\t')
        if l3_split[0] == "#XC1":
            gp = "6B"
        elif l3_split[0] == "#XC2":
            gp = "6C"
        elif l3_split[0] == "#XCal":
            gp = "6A"
        blastn_group.append(gp+"-"+l3_split[6])
        blastn_id.append(l3_split[1])
        blastn_gi.append(l3_split[2])
        blastn_taxon.append(l3_split[3])

for n, nid in enumerate(n_id):
    ncat = n_cat[n]
    nind = [n for n, e in enumerate(blastn_id) if e == nid]
    for i in nind:
        if blastn_group[i] == ncat:
            sys.stdout.write(blastn_id[i]+'\t'+ncat+'\t'+"N"+'\t'+blastn_gi[i]+'\t'+blastn_taxon[i]+'\n')

for x, xid in enumerate(x_id):
    xcat = x_cat[x]
    xind = [x for x, e in enumerate(blastx_id) if e == xid]
    for i in xind:
        if blastx_group[i] == xcat:
            sys.stdout.write(blastx_id[i]+'\t'+xcat+'\t'+"X"+'\t'+blastx_gi[i]+'\t'+blastx_taxon[i]+'\t'+'\n')
