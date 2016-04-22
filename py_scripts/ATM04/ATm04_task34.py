# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-10 13:55:34
# @Last Modified by:   aung
# @Last Modified time: 2016-03-10 14:43:18
import sys
rsemdefile = sys.argv[1]
kaldefile = sys.argv[2]
infile = sys.argv[3]

rsem_id = []
rsem_record = []
with open(rsemdefile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        rsem_id.append(l1_split[0])
        tmp=""
        for i in l1_split[2:]:
            if tmp == "":
                tmp =i
            else:
                tmp +="\t"+i
        rsem_record.append(tmp.strip('\n'))

kal_id = []
kal_record = []
with open(kaldefile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        tmp=""
        for i in l2_split[2:]:
            if tmp == "":
                tmp =i
            else:
                tmp +="\t"+i
        kal_id.append(l2_split[0])
        kal_record.append(tmp.strip('\n'))

with open(infile,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        id_ = l3_split[0]
        if id_ in rsem_id:
            ind = rsem_id.index(id_)
        if id_ in kal_id:
            ind2 = kal_id.index(id_)
        sys.stdout.write(l3.strip('\n')+"\t"+rsem_record[ind]+"\t"+kal_record[ind2]+"\n")