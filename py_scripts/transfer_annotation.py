#! /usr/bin/env python
#--------------------------------------------------------------------------#
# transfer annotation ids to MIRA
# Date: 9012015
# Usage: annotataion_map.py
# __author__ = 'atrx'
#--------------------------------------------------------------------------#
import sys
import re
usage= "Usage %s cdhit.clstr annot.txt" % sys.argv[0] #specific massage for no input

try:
    annnotation_file = sys.argv[1]
    mira_cdhit_file = sys.argv[2]
except:
    print usage, sys.exit(1)

# loop file and put into list by line
def file_into_list(list_name,file_name):
    list_name = []
    for i in file_name:
        list_name.append(i)
    return list_name

cdhit_read = open(mira_cdhit_file,'r')
cdhit_list = file_into_list("cdhit_list",cdhit_read)

annot_read = open(annnotation_file,'r')
annot_list = file_into_list("annot_list",annot_read)


for cdhit_line in cdhit_list:
    # mira cluster id
    id = re.search(r'c01_PM\w+',cdhit_line)
    if id:
        mira_id = id.group()
        # id from annotation file
        for annot_line in annot_list:
            annot_mira_id = annot_line.split()
            if mira_id.strip() == annot_mira_id[0].strip():
                print mira_id, annot_line





