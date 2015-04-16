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

three_cdhit = sys.argv[1]
unmap_ref = sys.argv[2]
cluster_file = sys.argv[3]


three_cdhit_list = codesnippets.file_read_line(open(three_cdhit, "r"))
unmap_cdhit_list = codesnippets.file_read_line(open(unmap_ref, "r"))
cluster_cdhit_list = codesnippets.file_read_line(open(cluster_file, "r"))

three_cdhit_count = 0
unmap_count = 0

for clust_mem in cluster_cdhit_list:
    clust_mem_split = clust_mem.split('\t')
    for member in clust_mem_split:
        if member in three_cdhit_list:
            three_cdhit_count += 1
        elif member in unmap_cdhit_list:
            unmap_count += 1

print three_cdhit_count
print unmap_count