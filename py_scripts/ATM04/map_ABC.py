#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

fileC = sys.argv[1] #nonshrimp cluster
fileB = sys.argv[2] #nonshrimp matrix
fileA = sys.argv[3] # a clst group


c_clust = []
c_rep = []
c_mem = []
with open(fileC,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        c_clust.append(l1_split[0].strip('>').strip().strip('\n'))
        c_rep.append(l1_split[1].strip('>').strip().strip('\n'))
        tmp_m = l1_split[1].strip('>').strip().strip('\n')
        for m in l1_split[3].split('|'):
            tmp_m += ";" + m.strip('>').strip().strip('\n')
        c_mem.append(tmp_m)

b_id = []
b_nonshrimp = []
with open(fileB,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        b_id.append(l2_split[0].strip('>').strip().strip('\n'))
        b_nonshrimp.append(l2_split[1].strip('>').strip().strip('\n'))


with open(fileA,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        atmid = l1_split[0].strip('>').strip().strip('\n')
        if atmid in b_id:
            ind = b_id.index(atmid)
            nonshrimp = b_nonshrimp[ind]
        else:
            nonshrimp = "NaN"
        Cclust = "NaN"
        Crep = "NaN"
        for m in c_mem:
            m_split = m.split(';')
            for m2 in m_split:
                if m2 == atmid:
                    ind2 = c_mem.index(m)
                    Cclust = c_clust[ind2]
                    Crep = c_rep[ind2]
                    break

        sys.stdout.write(l1.strip('\n')+'\t'+nonshrimp+'\t'+Cclust+'\t'+Crep+'\n')

# python map_ABC.py ATM04_nonShrimp.matrix_y.fasta_out.clstr.rep ATM04_nonShrimp.matrix ATMlen_group_clst.matrix.ATM06_ATM
