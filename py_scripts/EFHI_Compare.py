#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-24 13:31:49
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-25 10:51:40
import sys
efhi = sys.argv[1]
hi = sys.argv[2]
ef = sys.argv[3]

ef_list =[]
hi_list =[]

with open(ef,'rb') as f3:
    for l3 in f3:
        ef_list.append(l3.strip('>'))

with open(hi,'rb') as f2:
    for l2 in f2:
        hi_list.append(l2.split()[0].strip('>'))

with open(efhi,'rb') as f1:
    for l1 in f1:
        id_ = l1.split()[0].strip('>')        
        if (id_ not in ef_list) and (id_ not in hi_list):
            sys.stdout.write(l1);