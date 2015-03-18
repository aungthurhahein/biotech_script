"""
# parse cd-hite cluster file into the following format
    # #cluser id    #member1....#memberN
# usage: python cdhit-clstr_parser.py .clstr
# Dev: Aung
# Date: 03022015
"""
import sys

file1 = sys.argv[1]
file_read = open(file1, 'r')
cluster_list = []
for i in file_read:
    cluster_list.append(i)

for clst_line in cluster_list:
    if ">Cluster" in clst_line:
        print '\n'
        print clst_line.strip(), "\t",
    else:
        clst_split = clst_line.split()
        print clst_split[2].strip("."), "\t",