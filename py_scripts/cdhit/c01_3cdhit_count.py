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

control_id = sys.argv[1]  # control
mature_id = sys.argv[2]  # mature
survival_id = sys.argv[3]  # survival
mapped_ref_id = sys.argv[4]  # mapped ref
unmapped_ref_id = sys.argv[5]  # unmapped ref
clst_group = sys.argv[6]

control_list = codesnippets.file_read_line(open(control_id, 'r'))
mature_list = codesnippets.file_read_line(open(mature_id, 'r'))
survival_list = codesnippets.file_read_line(open(survival_id, 'r'))
mapped_ref_list = codesnippets.file_read_line(open(mapped_ref_id, 'r'))
unmapped_ref_list = codesnippets.file_read_line(open(unmapped_ref_id, 'r'))
clst_group_list = codesnippets.file_read_line(open(clst_group, 'r'))

# enumerate and get number of sequences
clean_clust = []
to_remove = ['\'', '[', ']']
for cluster in clst_group_list:
    tmp_clst = []
    cluster_split = cluster.split(',')
    for x in cluster_split:
        clean_x = x.translate(None, ''.join(to_remove))
        if clean_x not in tmp_clst:
            tmp_clst.append(clean_x)
    clean_clust.append(tmp_clst)

for clean_cluster in clean_clust:
    control_count = 0
    mature_count = 0
    survival_count = 0
    mapped_count = 0
    unmapped_count = 0
    for member in clean_cluster:
        if member.strip() in control_list:
            control_count += 1
        elif member.strip() in mature_list:
            mature_count += 1
        elif member.strip() in survival_list:
            survival_count += 1
        elif member.strip() in mapped_ref_list:
            mapped_count += 1
        elif member.strip() in unmapped_ref_list:
            unmapped_count += 1
    print clean_cluster[0] + '\t' + str(control_count) + '\t' + str(mature_count) +'\t'+str(survival_count)+'\t'+str(mapped_count)+'\t'+str(unmapped_count)


