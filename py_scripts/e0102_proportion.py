# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-04 16:26:11
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-10 14:41:21
import sys
matrixfile = sys.argv[1]
total = [20457,575,23767,403,17798,313]

with open(matrixfile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        id_ = l1_split[0]
        tmp = id_+"\t"
        for x,m in enumerate(l1_split[1:]):
            # get total by indexes and divide non-zero cells
            m_ = float(m.strip().strip('\n'))
            if m_ != 0:                         
                tmp += "\t"+str(m_/total[int(x)])
            else:            
                tmp += "\t"+"0"
        sys.stdout.write(tmp+"\n")