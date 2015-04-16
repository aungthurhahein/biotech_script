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

A_id = sys.argv[1]  # A
L_id = sys.argv[2]  # L
C_id = sys.argv[3]  # C
cluster_file = sys.argv[4]  # cluster parsed file
open_Aid = open(A_id, 'r')
open_Lid = open(L_id, 'r')
open_Cid = open(C_id, 'r')
open_cluster = open(cluster_file, 'r')

A_id_list = []
L_id_list = []
C_id_list = []
clst_list = []
S1A = []
S1L = []
S1C = []
S2A = []
S2L = []
S2C = []
G3 = []
G2AL = []
G2AC = []
G2LC = []

for id1 in open_Aid:
    A_id_list.append(id1.strip())
for id2 in open_Lid:
    L_id_list.append(id2.strip())
for id3 in open_Cid:
    C_id_list.append(id3.strip())
for cluster in open_cluster:
    clst_list.append(cluster.strip())

for x in clst_list:
    x_split = x.split('\t')
    # singleton
    if len(x_split) == 2:
        if x_split[1].strip() in A_id_list:  # S1A
            S1A.append(x)
        elif x_split[1].strip() in L_id_list:  # S1L
            S1L.append(x)
        elif x_split[1].strip() in C_id_list:  # S1C
            S1C.append(x)
    else:
        id_flag = range(len(x_split))  # * for A and # for L and & for C
        idA_count = 0
        idL_count = 0
        idC_count = 0
        print x_split[0], id_flag,idA_count,idL_count,idC_coun
        for x_count, mem in enumerate(x_split):
            if mem.strip() in A_id_list:  # in A
                id_flag[x_count] = "*"
            elif mem.strip() in L_id_list:  # in L
                id_flag[x_count] = "#"
            elif mem.strip() in C_id_list:  # in C
                id_flag[x_count] = "&"

        for y in id_flag:
            if y == "*":
                idA_count += 1
            elif y == "#":
                idL_count += 1
            elif y == "&":
                idC_count += 1

        print x_split[0], id_flag,idA_count,idL_count,idC_count
        if idA_count >= 1 and idL_count >= 1 and idC_count >= 1:  # G3
            G3.append(x)
        elif idA_count >= 1 and idL_count >= 1 and idC_count == 0:  # G2AL
            G2AL.append(x)
        elif idA_count >= 1 and idL_count == 0 and idC_count >= 1:  # G2AC
            G2AC.append(x)
        elif idA_count == 0 and idL_count >= 1 and idC_count >= 1:  # G2LC
            G2LC.append(x)
        elif idA_count >= 1 and idL_count == 0 and idC_count == 0:  # S2A
            S2A.append(x)
        elif idA_count == 0 and idL_count >= 1 and idC_count == 0:  # S2L
            S2L.append(x)
        elif idA_count == 0 and idL_count == 0 and idC_count >= 1:  # S2C
            S2C.append(x)


codesnippets.write_file(S1A, "{0}_S1A".format(cluster_file))
codesnippets.write_file(S1L, "{0}_S1L".format(cluster_file))
codesnippets.write_file(S1C, "{0}_S1C".format(cluster_file))
codesnippets.write_file(S2A, "{0}_S2A".format(cluster_file))
codesnippets.write_file(S2L, "{0}_S2L".format(cluster_file))
codesnippets.write_file(S2C, "{0}_S2C".format(cluster_file))
codesnippets.write_file(G2AL, "{0}_G2AL".format(cluster_file))
codesnippets.write_file(G2AC, "{0}_G2AC".format(cluster_file))
codesnippets.write_file(G2LC, "{0}_G2LC".format(cluster_file))
codesnippets.write_file(G3, "{0}_G3".format(cluster_file))