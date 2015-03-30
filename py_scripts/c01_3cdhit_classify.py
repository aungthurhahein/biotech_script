#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 30032015
"""
import sys
import codesnippets

# control_id = sys.argv[1]  # control
# mature_id = sys.argv[2]  # mature
# survival_id = sys.argv[3]  # survival
# mapped_ref_id = sys.argv[4]  # mapped ref
# unmapped_ref_id = sys.argv[5]  # unmapped ref

# control_list = codesnippets.file_read_line(control_id)
# mature_list = codesnippets.file_read_line(mature_id)
# survival_list = codesnippets.file_read_line(survival_id)
# mapped_ref_list = codesnippets.file_read_line(mapped_ref_id)
# unmapped_ref_list = codesnippets.file_read_line(unmapped_ref_id)

two_cdhit_clst = sys.argv[1]
clst_group = sys.argv[2]  # clusters

two_cdhit_clst_list = codesnippets.file_read_line(open(two_cdhit_clst, 'r'))
clst_group_list = codesnippets.file_read_line(open(clst_group, 'r'))

clstr_expand = []
# expand representative sequences from second cdhit
for cluster in clst_group_list:
    cluster_split = cluster.split('\t')
    new_expand_clst = []
    new_expand_clst.append(cluster_split[0])
    for member in cluster_split:
        # print member
        for two_cluster in two_cdhit_clst_list:
            two_cluser_split = two_cluster.split('\t')
            # unique members
            cluster_list = []
            for i in two_cluser_split:
                if i not in cluster_list:
                    cluster_list.append(i)

            for two_member in cluster_list[1:]:
                if member.strip() == two_member.strip():
                    for x_list in cluster_list[1:]:
                        new_expand_clst.append(x_list)
                else:
                    if member not in new_expand_clst:
                        new_expand_clst.append(member)
    clstr_expand.append(new_expand_clst)

for x in clstr_expand:
    print x
# enumerate and get number of sequences



