#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-18 20:02:43
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-19 13:03:41

import sys
b25_file = sys.argv[1]
catx_file = sys.argv[2]
cap3idmap = sys.argv[3]

b25_list = []
with open(b25_file,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        b25_list.append(l1_split[1].strip('>'))

cap3_list = []
cap3_atm = []
with open(cap3idmap,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')        
        cap3_list.append(l2_split[2].strip('\n').strip('>'))        
        cap3_atm.append(l2_split[1].strip('>'))

withcatx = []
with open(catx_file,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        id_ = l3_split[0].strip('>') 
        if "CDF" in id_:                    
            indexes = [i for i,e in enumerate(cap3_list) if e == id_]
            for i in indexes:                
                if cap3_atm[i] in b25_list:
                    sys.stdout.write(cap3_atm[i]+'\t'+l3_split[3]+'\t'+id_+'\n')                
                    withcatx.append(cap3_atm[i])
        else:
            if id_ in b25_list:
                sys.stdout.write(id_+'\t'+l3_split[3]+'\t'+"-"+'\n')                        
                withcatx.append(id_)

for i in b25_list:
    if i not in withcatx:
        if i in cap3_atm:
            ind = cap3_atm.index(i)
            sys.stdout.write(i+'\t'+"-"+'\t'+cap3_list[ind]+'\n')                        
        else:
            sys.stdout.write(i+'\t'+"-"+'\t'+"-"+'\n')                        
