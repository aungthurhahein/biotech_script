# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-20 13:31:01
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-20 14:53:42
import sys

idlist = sys.argv[1]
blast = sys.argv[2]
cdesc = sys.argv[3]

blast_id = []
blast_desc = []
with open(blast,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        blast_id.append(l1_split[0])
        blast_desc.append(l1_split[1].strip('\n'))

cdesc_id = []
cdesc_desc = []
with open(cdesc, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        for m in l2_split[0].split(';'):        
            cdesc_id.append(m.strip())
            cdesc_desc.append(l2_split[1].strip('\n'))

with open(idlist,'rb') as f1:
    for l1 in f1:
        id_ = l1.strip('\n')
        tmp_desc = ""
        if id_ in blast_id:
            ind = blast_id.index(id_)
            if tmp_desc =="":
                tmp_desc = blast_desc[ind].strip().rstrip('|')
            else:
                tmp_desc += "|"+blast_desc[ind].strip().rstrip('|')
        if id_ in cdesc_id:
            ind = cdesc_id.index(id_)
            if tmp_desc =="":
                tmp_desc = cdesc_desc[ind].strip().rstrip('|')
            else:
                tmp_desc += "|"+blast_desc[ind].strip().rstrip('|')
        sys.stdout.write(id_+"\t"+tmp_desc+"\n")