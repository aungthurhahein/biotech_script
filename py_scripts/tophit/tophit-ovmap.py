#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

divquery = sys.argv[1]
map = sys.argv[2]

opendivquery = open(divquery, 'r')
openmap = open(map, 'r')

fA = open(divquery+"_A", 'w')
fB = open(divquery+"_B", 'w')
fC = open(divquery+"_C", 'w')
fD = open(divquery+"_D", 'w')
fE = open(divquery+"_E", 'w')
fF = open(divquery+"_F", 'w')

div_id = []
div_group = []
div_record = []
for line in opendivquery:
    line_split = line.split('\t')
    div_id.append(line_split[0].strip())
    div_record.append(line.strip('\n'))
    div_group.append(line_split[5].strip())

map_id = []
map_list = []
for line2 in openmap:
    line2_split = line2.split('\t')
    map_id.append(line2_split[0].strip())
    map_list.append(line2.strip('\n'))

for y, divid in enumerate(div_id):
    indices = [i for i, x in enumerate(map_id) if x == divid]
    for ind in indices:
        tmp = map_list[ind]+'\t'+div_group[y].strip()+'\n'
        print tmp
        if div_group[y] == 'A':
            fA.write(tmp)
        elif div_group[y] == 'B':
            fB.write(tmp)
        elif div_group[y] == 'C':
            fC.write(tmp)
        elif div_group[y] == 'D':
            fD.write(tmp)
        elif div_group[y] == 'E':
            fE.write(tmp)
        elif div_group[y] == 'F':
            fF.write(tmp)


