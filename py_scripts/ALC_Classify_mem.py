#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
A_id = sys.argv[1]  # A
L_id = sys.argv[2]  # L
C_id = sys.argv[3]  # C
Cu_id = sys.argv[4]  # C Unmap
cluster_file = sys.argv[5]  # cluster parsed file

open_Aid = open(A_id, 'r')
open_Lid = open(L_id, 'r')
open_Cid = open(C_id, 'r')
open_Cuid = open(Cu_id, 'r')
open_cluster = open(cluster_file, 'r')

A_id_list = []
L_id_list = []
C_id_list = []
Cu_id_list = []
clst_list = []

for id1 in open_Aid:
    A_id_list.append(id1.strip())
for id2 in open_Lid:
    L_id_list.append(id2.strip())
for id3 in open_Cid:
    C_id_list.append(id3.strip())
for id4 in open_Cuid:
    Cu_id_list.append(id4.strip())
for cluster in open_cluster:
    clst_list.append(cluster.strip())

for x in clst_list:
    x_split = x.split('\t')
    A_count = 0
    L_count = 0
    C_count = 0
    Cu_count = 0
    for mem in x_split[1:]:
        if mem.strip() in A_id_list:
            A_count += 1
        elif mem.strip() in L_id_list:
            L_count += 1
        elif mem.strip() in C_id_list:
            C_count += 1
        elif mem.strip() in Cu_id_list:
            Cu_count += 1

    print x_split[0] + '\t' + str(A_count) +'\t' + str(L_count) +'\t' + str(C_count) +'\t' + str(Cu_count)
