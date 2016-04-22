#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-23 10:52:55
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-23 10:59:35

import sys
tophitfmt_file = sys.argv[1]
I8C_id = sys.argv[2]

I8C_list = []
with open(I8C_id,'rb') as f1:
    for l1 in f1:        
        I8C_list.append(l1.strip('>').strip('\n'))


with open(tophitfmt_file,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        id_ = l2_split[0]
        if id_ in I8C_list:
            sys.stdout.write(l2)


