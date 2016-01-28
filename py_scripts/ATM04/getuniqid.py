#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
infile = sys.argv[1]
id_list = []
xn = []
cat_group = []
with open(infile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        for i in l1_split[5].split(';'):
            if len(i.split('-')) == 3:
                id_list.append(i.split('-')[0].strip('\n')+'-'+i.split('-')[1].strip('\n'))
            else:
                id_list.append(i.split('-')[0].strip('\n'))
            if len(i.split('-')) == 3:
                xn.append(i.split('-')[2])            
            elif len(i.split('-')) > 1:
                xn.append(i.split('-')[1])            
            else:
                xn.append('-')
            cat_group.append(l1_split[0])

for i,x in enumerate(id_list):
    sys.stdout.write(x+'\t'+xn[i]+'\t'+cat_group[i]+"\n")

 # cat blastn-x.tophit.querycatx.genus_count.sct.id.sort | awk -F '\t' '{if($3=="D")print $0}' > blastn-x.tophit.querycatx.genus_count.sct.id.sort.D
 # cat blastn-x.tophit.querycatx.genus_count.sct.id.sort | awk -F '\t' '{if($3=="E")print $0}' > blastn-x.tophit.querycatx.genus_count.sct.id.sort.E
 # cat blastn-x.tophit.querycatx.genus_count.sct.id.sort | awk -F '\t' '{if($3=="I6")print $0}' > blastn-x.tophit.querycatx.genus_count.sct.id.sort.I6
 # cat blastn-x.tophit.querycatx.genus_count.sct.id.sort | awk -F '\t' '{if($3=="I8")print $0}' > blastn-x.tophit.querycatx.genus_count.sct.id.sort.I8
