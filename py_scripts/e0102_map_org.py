# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-11 12:51:02
# @Last Modified by:   aung
# @Last Modified time: 2016-05-11 13:21:33
import sys

mapref = sys.argv[1]
mapcount = sys.argv[2]

aung_id = []
aung_count = []
with open(mapcount, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        aung_id.append(l1_split[0])
        aung_count.append(int(l1_split[1].strip('\n')))

ref_id = []
ref_mapread = []
with open(mapref, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        ref_id.append(l2_split[0])
        ref_mapread.append(l2_split[1].strip('>\n'))

uniq_refid = set(list(ref_id))
out = open(mapref+".refmapcount","w")
for uref in uniq_refid:
    ind = [i for i,e in enumerate(ref_id) if e == uref]
    tmp_read = ""
    tmp_count = 0
    for i in ind:
        if tmp_read == "":
            tmp_read = ref_mapread[i]
        else:
            tmp_read += ";"+ref_mapread[i]        
        if ref_mapread[i] in aung_id:
            ind2 = aung_id.index(ref_mapread[i])
            tmp_count += aung_count[ind2]
    out.write(uref+"\t"+tmp_read+"\t"+str(tmp_count)+"\n")

