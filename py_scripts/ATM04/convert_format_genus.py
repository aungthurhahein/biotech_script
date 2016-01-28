#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
genuslist = sys.argv[1]
catx = sys.argv[2]

genus_list = []
id_list = []
with open(genuslist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        for x in l1_split[5].split(';'):
            genus_list.append(l1_split[1])
            id_list.append(x.strip().strip('\n').strip('-XN'))

uniq_id = list(set(id_list))
for id_ in uniq_id:
    tmp_genus = ""
    indexes = [i for i,e in enumerate(id_list) if e == id_]        
    for i in indexes:
        if tmp_genus == "":
            tmp_genus= genus_list[i]
        else:
            tmp_genus += ";"+genus_list[i]
    sys.stdout.write(catx+"\t"+id_+"\t"+tmp_genus+"\n")



