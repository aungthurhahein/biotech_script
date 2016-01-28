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
genelist = sys.argv[2]

gene_list = []
with open(genelist,'rb') as f2:
    for l2 in f2:
        l2_split = l2.strip('\n')
        gene_list.append(l2_split)
        
with open(gene_tran,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        if l1_split[0] not in gene_list:
            sys.stdout.write(l1)        
        
