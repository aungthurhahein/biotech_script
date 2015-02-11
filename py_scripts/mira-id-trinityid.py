#! /usr/bin/env python
#--------------------------------------------------------------------------#
# map 2 medium files of mira id. mira_org_id<--->customid<---->trinityid
# output: mira_org_id<----->trinityid
# Date: 04022015
# __author__ = 'atrx'
#--------------------------------------------------------------------------#
import sys
import linecache

file1="/home/aung/server_downloads/c01_MIRA_CDHIT/c01_PM_out.unpadded.fmt.fasta.hdr"
file2="/home/aung/server_downloads/c01_MIRA_CDHIT/clstrtrinitymap.txt"
file_read= open(file1,'r')
file2_read=open(file2,'r')
mira_buffer=[];buffer_trinity=[];


for i in file_read:
    mira_buffer.append(i)
for j in file2_read:
    buffer_trinity.append(j)

for mira_buff in mira_buffer:
    mira_split = mira_buff.split()
    mira_buf= mira_split[0].strip()
    for buffer_trin in buffer_trinity:
        buffer_trin_split = buffer_trin.split('\t')
        buff_trin= buffer_trin_split[1].strip()
        if mira_buf == buff_trin:
            print mira_split[1],'\t',buffer_trin_split[0]
