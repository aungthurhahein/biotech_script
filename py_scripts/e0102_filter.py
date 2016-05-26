# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-25 18:06:45
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-27 13:54:06
import sys
matrix = sys.argv[1]

out = open(matrix+"_flt",'w')
out2 = open(matrix+"_unmap",'w')
with open(matrix,'rb') as f1:
    for l1 in f1:        
        l1_split = l1.split('\t')
        flag = 0
        for m in l1_split[1:]:            
            m = float(m.strip('\n'))
            if m <= 0:
                flag = 0                
            else:
                flag = 1                
                break
        # print "flag"+str(flag)
        if flag == 1:
            out.write(l1)
        else:
            out2.write(l1)
