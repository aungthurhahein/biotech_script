#! /usr/bin/env python

"""
# parse cdhist_clstr_paser output by samples
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_classifer_bysamples.py xxxCluster.stat.parse
# output: 5 files are written at line 45
# Dev: Aung
# Date: 10032015
"""

import sys
import re
import codesnippets

clstrfile = sys.argv[1]
clstrfile_read = open(clstrfile, 'r')

controlfile = sys.argv[2]
controlfile_read = open(controlfile, 'r')

survivalfile = sys.argv[3]
survivalfile_read = open(survivalfile, 'r')

maturefile = sys.argv[4]
maturefile_read = open(maturefile, 'r')

def readfile(file_handle):
    tmp_list = []
    for x in file_handle:
        tmp_list.append(x.strip('@>').strip())
    return tmp_list

cluster_list = []
cluster_replace = []
control_list = readfile(controlfile_read)
mature_list = readfile(maturefile_read)
survival_list = readfile(survivalfile_read)

for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    print x_split
    temp_record = " "
    for line in x_split:
        line = line.strip('@>').strip()
        print line
        if 'Cluster' in line:
            temp_record += line.strip()+'\t'
        if line in control_list:
            temp_record += "C" + "\t"
        elif line in mature_list:
            temp_record += "M" + "\t"
        elif line in survival_list:
            temp_record += "S" + "/t"
        else:
            temp_record += "O" + "\t"

    cluster_replace.append(temp_record)
    print temp_record,cluster_replace
codesnippets.write_file(cluster_replace, "{0}_bysample".format(clstrfile))

CMS_list = []
CM_list = []
CS_list = []
MS_list = []
for res in cluster_replace:
    C_flag = re.search(r'C', res)
    M_flag = re.search(r'M', res)
    S_flag = re.search(r'S', res)
    if C_flag and M_flag and S_flag:
        CMS_list.append(res)
    elif C_flag and M_flag:
        CM_list.append(res)
    elif C_flag and S_flag:
        CS_list.append(res)
    elif M_flag and S_flag:
        MS_list.append(res)
codesnippets.write_file(CMS_list, "{0}_CMS".format(clstrfile))
codesnippets.write_file(CM_list, "{0}_CM".format(clstrfile))
codesnippets.write_file(CS_list, "{0}_CS".format(clstrfile))
codesnippets.write_file(MS_list, "{0}_MS".format(clstrfile))

print "CMS:" "" + str(len(CMS_list))
print "CM:" "" + str(len(CM_list))
print "CS:" "" + str(len(CS_list))
print "MS:" "" + str(len(MS_list))
