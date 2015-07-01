"""
# cdhit parser that give three columns output(Cluster-Representative Sequence-Member1|Member2...MemberN)
# usage: cdhit-parser file.clsr
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

file1 = sys.argv[1]
file_read = open(file1, 'r')
cluster_list = []

for i in file_read:
    cluster_list.append(i)

clster = ""
rep = ""
member = []


def print_mem(list_obj):
    final_string = ""
    for x in list_obj:
        final_string += x+"|"
    return final_string

for x, clst_line in enumerate(cluster_list):
    if ">Cluster" in clst_line:
        print clster+"\t"+rep+'\t', print_mem(member)
        clster = ""
        rep = ""
        member = []
        clster = clst_line.strip()
    elif "*" in clst_line:
        clst_split = clst_line.split()
        rep = clst_split[2].strip(".")
    else:
        clst_split = clst_line.split()
        member.append(clst_split[2].strip("."))
    if x + 1 == len(cluster_list):
        print clster + "\t" + rep + '\t', print_mem(member)