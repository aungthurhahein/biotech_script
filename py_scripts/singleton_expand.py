#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import codesnippets
two_cdhit_clst = sys.argv[1]
clst_group = sys.argv[2]  # clusters id

two_cdhit_clst_list = codesnippets.file_read_line(open(two_cdhit_clst, 'r'))
clst_group_list = codesnippets.file_read_line(open(clst_group, 'r'))

# expand representative sequences from second cdhit
for clusterid in clst_group_list:
    cluster_split = clusterid.split('\t')
    for two_cluster in two_cdhit_clst_list:
        two_cluser_split = two_cluster.split('\t')
        if len(two_cluser_split) >= 2 :
            if cluster_split[1].strip() == two_cluser_split[1].strip():
                # unique members
                cluster_list = []
                for i in two_cluser_split:
                    i_split = i.split('|')
                    for x in i_split:
                        if x not in cluster_list:
                            cluster_list.append(x)
                print cluster_split[0] + ',\t' + str(cluster_list[1:])

