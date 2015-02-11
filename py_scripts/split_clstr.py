#! /usr/bin/env python
#--------------------------------------------------------------------------#
# split file cdhit clstr filr into Cluster-MIRA,Cluster-Trinity
# Date: 02022015
# __author__ = 'atrx'
#--------------------------------------------------------------------------#

import sys
import re
file = "/home/aung/server_downloads/c01_mapping/Member1_table.txt"

file_read = open(file,'r')
file_list=[]
f = open("Member1_T.txt","w")
f2 = open("Member1_M.txt","w")

for i in file_read:
  file_list.append(i)

for x in file_list:
  id_split = x.split('\t')
  for line in id_split:
    line =line.replace('.','')
    id = re.search(r'c01_PM\w+',line)
    if id:
      writeline= id_split[0] +id.group().strip(".")+"\n"
      f2.write(writeline)
    else:
      if 'Cluster' not in line:
        writeline2= id_split[0]+line+"\n"
        f.write(writeline2)







