#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

atmcdhit = sys.argv[1]
atmspecific = sys.argv[2]
v1query = sys.argv[3]
v2query = sys.argv[4]

openatmcdhit = open(atmcdhit, 'r')
openatmspecific = open(atmspecific, 'r')
openv1query = open(v1query, 'r')
openv2query = open(v2query, 'r')

atm_id = []
atmsp_id = []
v1_id = []
v2_id = []
atm_records = []
atmsp_records = []
v1_records = []
v2_records = []

for line in openatmcdhit:
    line_split = line.split('\t')
    atm_id.append(line_split[0].strip('>'))
    atm_records.append(line_split)

for line2 in openatmspecific:
    line2_split = line2.split('\t')
    atmsp_id.append(line2_split[0].strip('>'))
    atmsp_records.append(line2_split[2:])

for line3 in openv1query:
    line3_split = line3.split('\t')
    v1_id.append(line3_split[0].strip())
    v1_records.append(line3_split[1].strip('\n'))
for line4 in openv2query:
    line4_split = line4.split('\t')
    v2_id.append(line4_split[0].strip())
    v2_records.append(line4_split[1].strip('\n'))

print"ID\tLen\tATM98\tATM95\tATM90\tATM85\tATM80\tNonShrimp98\tNonShrimp95\tNonShrimp90\tNonShrimp85\tNonShrimp80\tv1Group\tv2Group"

for x, atmid in enumerate(atm_id):
    for atm_cdhit in atm_records[x]:
        if atm_cdhit != " ":
            sys.stdout.write(atm_cdhit.strip('\n'))  # atm cdhit
            sys.stdout.write('\t')
        else:
            sys.stdout.write('-\t')
    if atmid in atmsp_id:
        indx = atmsp_id.index(atmid)
        for h in atmsp_records[indx]:
            if h != " ":
                sys.stdout.write(h.strip('\n'))  # atm sp
                sys.stdout.write('\t')
            else:
                sys.stdout.write('-\t')
    else:
        sys.stdout.write('-\t-\t-\t-\t-\t')
    if atmid in v1_id:
        indx2 = v1_id.index(atmid)
        sys.stdout.write(str(v1_records[indx2]))  # v1
        sys.stdout.write('\t')
    else:
        sys.stdout.write('-')
        sys.stdout.write('\t')
    if atmid in v2_id:
        indx3 = v2_id.index(atmid)
        sys.stdout.write(str(v2_records[indx3]))  # v2
    else:
        sys.stdout.write('-')
        sys.stdout.write('\t')
    sys.stdout.write('\n')