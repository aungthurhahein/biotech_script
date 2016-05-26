# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-27 14:06:46
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-27 16:41:00
import sys
idlist = sys.argv[1]
cluster = sys.argv[2]

rep_id = []
mem  = []
with open(cluster,'rb') as f1:
    for l1 in f1:        
        l1_split = l1.split('\t')
        rep_id.append(l1_split[1])    
        mem.append(l1_split[2])

unmap_id = []
with open(idlist,'rb') as f2:
    for l2 in f2:                
        unmap_id.append(l2.strip('\n'))

out = open("rep.id","w")
for x,m in enumerate(mem):
    flag = 0    
    for i in m.rstrip('|').split('|'):
        id_ = i.strip('>').strip('\n')
        if id_ != "":
            if id_ in unmap_id:            
                flag = 1
            else:
                flag = 0    
    if flag == 1:
        out.write(rep_id[x]+'\n')



