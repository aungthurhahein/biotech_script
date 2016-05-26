# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-22 17:40:56
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-22 18:05:55
import sys

clstid = "Hi.clstid.uniq"
file_1= "HI.all.txt"

clst_id = []
clst_mem = []
clst_desc = []
with open(file_1, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        clst_id.append(l3_split[0].strip('>').strip())
        clst_mem.append(l3_split[3])
        clst_desc.append(l3_split[4].strip('\n'))

with open(clstid, 'rb') as f1:
    for l1 in f1:
        id_ = l1.strip('>').strip('\n')
        indexes = [i for i,e in enumerate(clst_id) if e == id_]
        tmp_mem = ""
        tmp_desc = ""
        for i in indexes:
            if tmp_mem == "":
                tmp_mem = clst_mem[i]
            else:
                tmp_mem += ";"+clst_mem[i]

            if tmp_desc == "":
                tmp_desc = clst_desc[i]
            else:
                tmp_desc += ";"+clst_desc[i]
        sys.stdout.write(id_+'\t'+tmp_mem+'\t'+tmp_desc)                
            


