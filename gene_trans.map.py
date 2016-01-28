#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
gene_tran = sys.argv[1]
trgenes = "/home/aung/20151221_hoislx/FPKM/Trinity_genes_c01.TMM.EXPR.matrix"  
trtrans = "/home/aung/20151221_hoislx/FPKM/Trinity_trans_c01.TMM.EXPR.matrix"
kaligenes = "/home/aung/20151221_hoislx/FPKM/Trinity_kallisto_genes_c01.TMM.EXPR.matrix"
kalitrans = "/home/aung/20151221_hoislx/FPKM/Trinity_kallisto_trans_c01.TMM.EXPR.matrix"

tr_gene = []
tr_gene_record = []
tr_trans = []
tr_trans_record = []
with open(trgenes,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        tr_gene.append(l1_split[0])
        tr_gene_record.append(l1)
with open(trtrans,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        tr_trans.append(l2_split[0])
        tr_trans_record.append(l2)

kali_gene = []
kali_gene_record = []
kali_trans = []
kali_trans_record = []
with open(kaligenes,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        kali_gene.append(l3_split[0])
        kali_gene_record.append(l3)

with open(kalitrans,'rb') as f4:
    for l4 in f4:
        l4_split = l4.split('\t')
        kali_trans.append(l4_split[0])
        kali_trans_record.append(l4)

with open(gene_tran,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split()
        trid = l2_split[0].strip('\n')
        sys.stdout.write(">"+'\t'+trid+'\n')
        if trid in tr_gene:
            sys.stdout.write('RSEM'+'\t'+tr_gene_record[tr_gene.index(trid)])
        if trid in kali_gene:
            sys.stdout.write('KALI'+'\t'+kali_gene_record[kali_gene.index(trid)])




