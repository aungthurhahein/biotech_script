#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys


matrix = sys.argv[1]
cluster = sys.argv[2]
cdhitparse = sys.argv[3]

atm02id = []
atm02records = []

with open(matrix,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        atm02id.append(line_split[0])
        atm02records.append(line)

clust_mem = {}
with open(cdhitparse, 'r') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        for x in line3_split[1:]:
            if line3_split[0].strip() not in clust_mem:
                clust_mem[line3_split[0].strip()] = x.strip('\n')+","
            else:
                clust_mem[line3_split[0].strip()] += x.strip('\n')+","

clustmematm02gt50 = {}
with open(cluster,'r') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        if line2_split[0].strip() in clust_mem.keys():
            clustmematm02gt50[line2_split[0].strip()] = clust_mem[line2_split[0].strip()]

for x,atmid in enumerate(atm02id):
    ATM019895 = "n"
    for key, value in clustmematm02gt50.iteritems():
        val_split = value.split(',')
        for m in val_split:
            if m == atmid:
                ATM019895 = "y"
    res_split = atm02records[x].split('\t')
    sys.stdout.write(res_split[0]+'\t'+res_split[1]+'\t'+res_split[2]+'\t'+ATM019895+'\t'+res_split[3]+'\t'+res_split[4]+'\t'+res_split[5]+'\t'+res_split[6]+'\t'+res_split[7]+'\n')