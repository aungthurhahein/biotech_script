#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
# idlist = sys.argv[1]
maplist = sys.argv[1]

# cdflist = []
# atmlist = []
# record = []
with open(maplist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        # cdflist.append(l1_split[12].strip('\n'))   
        atmlist = float(l1_split[8])
        # record.append(l1)
        if atmlist > 0:
            sys.stdout.write(l1)

# removeid = []
# o = open('noblast.id.fpkm.map.lte0.cond','w')
# with open(idlist,'rb') as f2:
#     for l2 in f2:
#         l2_split = l2.strip('\n')        
#         indexes = [i for i,e in enumerate(cdflist) if e == l2_split]                        
#         if len(indexes) > 0:
#             trg = 0
#             for i in indexes:
#                 if atmlist[i] > 0.0:
#                     trg = 1
#                 else:
#                     trg = 0
#             if trg == 1:
#                 for i in indexes:
#                     sys.stdout.write(record[i])
#             else:                
#                 for i in indexes:
#                     o.write(record[i])

# for x,it in enumerate(record):    
#     if cdflist[x] == " ":
#         if atmlist[x] > 0.0:
#             sys.stdout.write(it)
#         else:
#             o.write(it)


    
        