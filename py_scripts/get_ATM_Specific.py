"""
# parse cdhist_clstr_paser output into groups
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_classifer.py xxxCluster.stat.parse
# output: 5 files are written at line 45
# Dev: Aung
# Date: 10022015
"""
import sys
import re
import codesnippets

clstrfile = sys.argv[1]
clstrfile_read = open(clstrfile, 'r')
cluster_list = []
Set1_Singleton = []
Set1_Multi = []
for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    # multi
    if len(x_split) > 2:
        tmp_list = []
        for mem in x_split[1:]:
            ref_id = re.search(r'>PV_ATM01\w+', mem)  # ATM
            if ref_id:
                tmp_list.append('ATM')
        count = 0
        for atm_mem in tmp_list:
            if atm_mem == 'ATM':
                count += 1
        if count == len(x_split)-1:
            Set1_Multi.append(x)
    # singleton
    else:
        ref_id = re.search(r'>PV_ATM01\w+', x_split[1])  # ATM
        if ref_id:
            Set1_Singleton.append(x)
codesnippets.write_file(Set1_Multi, "{0}_ATM_Multi".format(clstrfile))
codesnippets.write_file(Set1_Singleton, "{0}_ATM_Singleton".format(clstrfile))

