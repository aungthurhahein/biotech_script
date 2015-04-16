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
    print new_expand_clst
    clstr_expand.append(new_expand_clst)
for x in clstr_expand:
    print x


