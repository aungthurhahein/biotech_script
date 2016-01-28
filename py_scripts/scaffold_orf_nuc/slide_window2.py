#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
inputfile = sys.argv[1] 

sid_list = []
start_list = []
end_list = []
with open(inputfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        sid = l1_split[0]
        start = l1_split[2]
        end = l1_split[3]
        sid_list.append(sid)
        start_list.append(start)
        end_list.append(end)

uniqid = list(set(sid_list))

for x in uniqid:
    indexes = [i for i,e in enumerate(sid_list) if e == x]
    tmp_list = []
    tmp_st = []
    tmp_end = []
    for i in indexes:
        xid = sid_list[i]
        stid = start_list[i]        
        enid = end_list[i]    
        tmp_list.append(stid)
        tmp_st.append(stid)
        tmp_end.append(enid)

    stchunk = 0
    endchunk = 0 
    finalst_chunk = []
    finalen_chunk = []    
    for i,k in enumerate(tmp_list):
        print nexts,k
        nexts = int(tmp_list[int(i)+1])+1
        
        if i == 0:
            stchunk = k
        if k == nexts:            
            print k,nexts,'+'
        else:
            finalen_chunk.append(stchunk)
            finalen_chunk.append(k)
            stchunk = k
            print k,nexts,'*'

    print finalst_chunk
    print finalen_chunk
