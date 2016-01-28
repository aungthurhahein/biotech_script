#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
rsem_fpkmmatrix = sys.argv[1]
kallisto_fpkmmatrix = sys.argv[2]
astran_id = []
rsem_id = []
rsem_record = []
kallisto_id = []
kallisto_record = []

with open(rsem_fpkmmatrix,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        astran_id.append(l1_split[1])
        rsem_id.append(l1_split[1])
        rsem_record.append(l1)

with open(kallisto_fpkmmatrix,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        astran_id.append(l2_split[1])
        kallisto_id.append(l2_split[1])
        kallisto_record.append(l2)

uniq_astranid = set(list(astran_id))

for id_ in uniq_astranid:
    if id_ in rsem_id and id_ in kallisto_id:
        rsem_ind = rsem_id.index(id_)
        kallisto_ind = kallisto_id.index(id_)
        sys.stdout.write(">"+id_+"\n")
        sys.stdout.write("RSEM\t"+rsem_record[rsem_ind])
        sys.stdout.write("KALS\t"+kallisto_record[kallisto_ind])
