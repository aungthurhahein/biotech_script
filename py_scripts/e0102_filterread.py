# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-11 15:09:20
# @Last Modified by:   aung
# @Last Modified time: 2016-05-11 16:10:22
import sys
matrix = sys.argv[1]
glw = open(matrix+"_glw","w")
hew = open(matrix+"_hev","w")
hpw = open(matrix+"_hpw","w")
other = open(matrix+"_other","w")

with open(matrix, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        # GL-W
        if (float(l1_split[2]) > 0 and float(l1_split[1]) == 0):
            glw.write(l1)
        # HE-W
        elif (float(l1_split[4]) > 0 and float(l1_split[3]) == 0):
            hew.write(l1)
        # HP-W
        elif (float(l1_split[6]) > 0 and  float(l1_split[5]) == 0):        
            hpw.write(l1)
        else:
            other.write(l1)