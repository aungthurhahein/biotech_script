# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-29 13:21:29
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-29 13:32:08

import sys
matrix = sys.argv[1]
DEoutput = sys.argv[2]

de_id = []
de_rec = []
with open(DEoutput,'rb') as f0:
    for l0 in f0:
        l0_split = l0.split('\t')
        de_id.append(l0_split[0])
        de_rec.append(l0.strip('\n'))

with open(matrix,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split()
        matrix_id = l1_split[0]
        matrix_rec =l1.strip('\n')
        if matrix_id in de_id:
            ind = de_id.index(matrix_id)
            sys.stdout.write(matrix_rec+"\t"+de_rec[ind]+"\n")
        else:
            sys.stdout.write(matrix_rec+"\t-\t-\t-\t-\t-"+"\n")

