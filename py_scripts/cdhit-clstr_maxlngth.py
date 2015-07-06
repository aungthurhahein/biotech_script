#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

cdhitparse = sys.argv[1]
atm01_lngth = sys.argv[2]
atm02_lngth = sys.argv[3]

clustername = []
member = []
with open(cdhitparse,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        clustername.append(line_split[0])
        member.append(line_split[1:])

atm01id = []
atm01lngth = []
with open(atm01_lngth) as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        atm01id.append(line2_split[0])
        atm01lngth.append(line2_split[1].strip('\n'))

atm02id = []
atm02lngth = []
with open(atm02_lngth) as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        atm02id.append(line3_split[0])
        atm02lngth.append(line3_split[1].strip('\n'))

sys.stdout.write("Cluster\t#ofMemmber\t#ofATM01\t#ofATM02\t#Max(ATM01)\tMax(ATM02)\tATM01-ATM02\n")
for x, clust in enumerate(clustername):
    tmp_atm01 = []
    tmp_atm02 = []
    for mem in member[x]:
        if mem.strip('>').strip() in atm01id:
            ind = atm01id.index(mem.strip('>').strip())
            tmp_atm01.append(atm01lngth[ind])
        elif mem.strip('>').strip() in atm02id:
            ind = atm02id.index(mem.strip('>').strip())
            tmp_atm02.append(atm02lngth[ind])
    sys.stdout.write(clust+"\t"+str(len(member[x]))+"\t"+str(len(tmp_atm01))+"\t"+str(len(tmp_atm02))+"\t"+str(max(tmp_atm01)).strip('\n')+"\t"+str(max(tmp_atm02)).strip('\n')+"\t"+str(int(max(tmp_atm01))-int(max(tmp_atm02))).strip('\n')+"\n")

