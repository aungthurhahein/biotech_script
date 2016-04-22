# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-29 10:43:57
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-29 12:45:16
import sys
idlist = sys.argv[1]
countmatrix = sys.argv[2]
fpkmmatrix= sys.argv[3]
fpkmnomrmatrix = sys.argv[4]

count_id = []
count_C = []
count_M = []
count_S = []
with open(countmatrix,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')                
        count_id.append(l1_split[0])
        count_C.append(l1_split[1])
        count_M.append(l1_split[2])
        count_S.append(l1_split[3].strip('\n'))

fpkm_id = []       
fpkm_C = []
fpkm_M = []
fpkm_S = []
with open(fpkmmatrix,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')                
        fpkm_id.append(l2_split[0])
        fpkm_C.append(l2_split[1])
        fpkm_M.append(l2_split[2])
        fpkm_S.append(l2_split[3].strip('\n'))

fpkmnorm_id = []
fpkmnorm_C = []
fpkmnorm_M = []
fpkmnorm_S = []
with open(fpkmnomrmatrix,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')              
        fpkmnorm_id.append(l3_split[0])
        fpkmnorm_C.append(l3_split[1])
        fpkmnorm_M.append(l3_split[2])
        fpkmnorm_S.append(l3_split[3].strip('\n'))  

with open(idlist,'rb') as f4:
    for l4 in f4:
        id_ = l4.strip('>').strip('\n')
        tmp = id_
        if id_ in count_id:
            ind1 = count_id.index(id_)
            tmp += '\t'+count_C[ind1]+'\t'+count_M[ind1]+'\t'+count_S[ind1]
        else:
            tmp += "\t-\t-\t-"
        if id_ in fpkm_id:
            ind2 = fpkm_id.index(id_)
            tmp += '\t'+fpkm_C[ind2]+'\t'+fpkm_M[ind2]+'\t'+fpkm_S[ind2]
        else:
            tmp += "\t-\t-\t-"
        if id_ in fpkmnorm_id:
            ind3 = fpkmnorm_id.index(id_)
            tmp += '\t'+fpkmnorm_C[ind3]+'\t'+fpkmnorm_M[ind3]+'\t'+fpkmnorm_S[ind3]
        else:
            tmp += "\t-\t-\t-"
        sys.stdout.write(tmp+'\n')
