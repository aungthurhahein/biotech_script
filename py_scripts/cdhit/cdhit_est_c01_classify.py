#! /usr/bin/env/ python
"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 27032015
"""
import sys
import codesnippets

type1_id = sys.argv[1]  # unmapped refid
type2_id = sys.argv[2]  # cdhit representative id
cluster_file = sys.argv[3]  # cluster file
open_t1id = open(type1_id, 'r')
open_t2id = open(type2_id, 'r')
open_cluster = open(cluster_file, 'r')

t1_id_list = []
t2_id_list = []
clst_list = []
S11 = []
S12 = []
S21 = []
S22 = []
G1 = []
for id1 in open_t1id:
    t1_id_list.append(id1.strip())
for id2 in open_t2id:
    t2_id_list.append(id2.strip())
for cluster in open_cluster:
    clst_list.append(cluster.strip())

for x in clst_list:
    x_split = x.split('\t')
    # singleton
    if len(x_split) == 2:
        if x_split[1].strip() in t1_id_list:
            S11.append(x)
        elif x_split[1].strip() in t2_id_list:
            S12.append(x)
    else:
        id1_flag = range(len(x_split))  # * for unmap and # for rep
        for x_count, mem in enumerate(x_split):
            print x_count, mem
            if mem.strip() in t1_id_list:  # in unmap
                id1_flag[x_count] = "*"
            elif mem.strip() in t2_id_list:  # in rep
                id1_flag[x_count] = "#"

        id1_count = 0
        id2_count = 0

        for y in id1_flag:
           if y == "*":
                id1_count += 1
           elif y == "#":
                id2_count += 1

        print x_split[0],id1_flag, id1_count , id2_count
        if id1_count >= 1 and id2_count >= 1:  # G1
            G1.append(x)
        elif id1_count >= 1 and id2_count == 0:  # 21
            S21.append(x)
        elif id1_count == 0 and id2_count >= 1:  # 22
            S22.append(x)

codesnippets.write_file(S11, "{0}_S11".format(cluster_file))
codesnippets.write_file(S12, "{0}_S12".format(cluster_file))
codesnippets.write_file(G1, "{0}_G2".format(cluster_file))
codesnippets.write_file(S21, "{0}_S21".format(cluster_file))
codesnippets.write_file(S22, "{0}_S22".format(cluster_file))

