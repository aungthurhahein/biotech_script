#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
A = "/fs/home/card/Aung/Ortho_20151125_overlap/RepSeq_EF.txt"
B = "/fs/home/card/Aung/Ortho_20151125_overlap/RepSeq_HI.txt"
C = "/fs/home/card/Aung/Ortho_20151125_overlap/RepSeq_EFHI.txt"

A_List = []
with open(A,'rb') as f1:
    for l1 in f1:
        A_List.append(l1.strip('\n'))

B_List = []
with open(B,'rb') as f2:
    for l2 in f2:
        B_List.append(l2.strip('\n'))

C_List = []
with open(C,'rb') as f3:
    for l3 in f3:
        C_List.append(l3.strip('\n'))

c1 = (set(A_List) & set(B_List)) - set(C_List)
# c6 = set(B_List) - set(A_List) - set(C_List)
# c7 = set(C_List) - set(B_List) - set(A_List)
# print len(c5),len(c6),len(c7)

o1= open("c4",'w')
# o2= open("Bonly",'w')
# o3= open("Conly",'w')
for x in list(c1):
    o1.write(x+'\n')
# for x in list(c6):
#     o2.write(x+'\n')
# for x in list(c7):
#     o3.write(x+'\n')
