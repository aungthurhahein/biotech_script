__author__ = 'aung'
import sys

file="/home/aung/server_downloads/c01_split/Member_T.txt"
file_read= open(file,'r')
result_clst=[];result_id=[];result_count=[];

for i in file_read:
    line_split = i.split()
    print line_split[0],
    print " ",
    print line_split[1],
    print "\t",
    print line_split[2].strip('>')