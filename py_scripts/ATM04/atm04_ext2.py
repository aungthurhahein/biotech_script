 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-19 13:03:06
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-23 16:47:29
import sys
idmap = sys.argv[1]
catx_map = sys.argv[2]

trinity_id = []
atm_id = []
with open(idmap,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        trinity_id.append(l1_split[1].strip('>').strip('\n'))
        atm_id.append(l1_split[2].strip('>'))

with open(catx_map,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        id_ = l2_split[0].strip('>')        
        if id_ in atm_id:
            ind = atm_id.index(id_)
            sys.stdout.write(l2_split[0]+'\t'+trinity_id[ind]+'\t'+l2_split[1]+'\t'+l2_split[2])
