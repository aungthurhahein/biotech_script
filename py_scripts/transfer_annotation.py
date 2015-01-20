#! /usr/bin/env python
#--------------------------------------------------------------------------#
# transfer annotation ids to MIRA
# Date: 9012015
# Usage: annotataion_map.py
# __author__ = 'atrx'
#--------------------------------------------------------------------------#
import sys

usage= "Usage %s infile" % sys.argv[0] #specific massage for no input

try:
    mira_cdhit_file = sys.argv[1]
    annnotation_file = sys.argv[2]
except:
    print usage, sys.exit(1)

cdhit_read = open(mira_cdhit_file,'r')
cdhit_list = file_into_list("cdhit_list",cdhit_read)

print cdhit_list
def file_into_list(list_name,file_name):
    list_name = []
    for i in file_name:
        list_name.append(i)
    return list_name
