# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-10 12:04:59
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-16 14:04:23
import sys
idmapfile = sys.argv[1]
matrix = sys.argv[2]

astran_id = []
org_id = []
with open(idmapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        astran_id.append(l1_split[2].strip('\n').strip('>'))
        org_id.append(l1_split[1])

with open(matrix,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        id_ = l2_split[0]
        if id_ in org_id:
            ind = org_id.index(id_)
            sys.stdout.write(astran_id[ind]+"\t"+l2)