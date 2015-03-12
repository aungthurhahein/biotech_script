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
both_side = []
Set1_Singleton = []
Set1_Multi = []  # ref
Set2_Singleton = []
Set2_Multi = []  # originalreads

for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    # multi
    if len(x_split) > 2:
        ref_id = re.search(r'>c\w+', x)  # fixed for cd-hit output
        org_id = re.search(r'>IJWSV\|\w+', x)  # it needs to be modified according to input header
        if ref_id and org_id:
            both_side.append(x)
        elif ref_id:
            Set1_Multi.append(x)
        elif org_id:
            Set2_Multi.append(x)
        else:
            print x
    # singleton
    else:
        ref_id = re.search(r'>c\w+', x_split[1])  # fixed for cd-hit output
        org_id = re.search(r'>IIJWSV\|\w+', x_split[1])  # it needs to be modified according to input header
        if ref_id:
            Set1_Singleton.append(x)
        elif org_id:
            Set2_Singleton.append(x)
codesnippets.write_file(both_side, "{0}_Both".format(clstrfile))
codesnippets.write_file(Set1_Multi, "{0}_Ref_Multi".format(clstrfile))
codesnippets.write_file(Set1_Singleton, "{0}_Ref_Singleton".format(clstrfile))
codesnippets.write_file(Set2_Multi, "{0}_Org_Multi".format(clstrfile))
codesnippets.write_file(Set2_Singleton, "{0}_Org_Singleton".format(clstrfile))

print "From both sets: " + str(len(both_side))
# only original reads
print "Multiple Refid: " + str(len(Set1_Multi))
print "Singleton Refid: " + str(len(Set1_Singleton))
# only original reads
print "Multiple orgid: " + str(len(Set2_Multi))
print "Singleton orgid: " + str(len(Set2_Singleton))