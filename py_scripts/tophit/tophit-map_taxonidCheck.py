#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

mapfile = sys.argv[1]

group = []
queryid = []
taxonid = []
division = []
record = []
same1 = open(mapfile+"_sametaxonid_c1", 'w')
same2 = open(mapfile+"_sametaxonid_c2", 'w')
diff1 = open(mapfile+"_difftaxonid_sameDiv_c1", 'w')
diff2 = open(mapfile+"_difftaxonid_diffDiv_c1", 'w')
diff3 = open(mapfile+"_difftaxonid_sameDiv_c2", 'w')
diff4 = open(mapfile+"_difftaxonid_diffDiv_c2", 'w')
diff5 = open(mapfile+"_difftaxonid_diffDiv_onlycal", 'w')

with open(mapfile, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        group.append(line_split[0])
        queryid.append(line_split[1])
        taxonid.append(line_split[3])
        division.append(line_split[5])
        record.append(line)

uniqid = list(set(queryid))

for qid in uniqid:
    qindxes = [i for i,e in enumerate(queryid) if e == qid]

    c1_taxonid = []
    c2_taxonid = []
    cal_taxonid = []
    c1_division = []
    c2_division = []
    cal_division = []

    for i in qindxes:
        group_i = group[i]
        if group_i == "#XC1":
            c1_taxonid.append(taxonid[i])
            c1_division.append(division[i])
        elif group_i == "#XC2":
            c2_taxonid.append(taxonid[i])
            c2_division.append(division[i])
        else:
            cal_taxonid.append(taxonid[i])
            cal_division.append(division[i])

        res= -1
        if len(c1_taxonid) > 0 or len(c2_taxonid) > 0:
            if set(c1_taxonid) == set(cal_taxonid):
                res = 1
            elif set(c2_taxonid) == set(cal_taxonid):
                res = 2
            else:
                res = 0
        else:
            res = 0

    if res == 1:
        for ind in qindxes:
            same1.write(record[ind])
    elif res == 2 and len(c1_taxonid) == 0:
        for ind in qindxes:
            same2.write(record[ind])
    else:
        res_2 = -1
        if set(c1_division) == set(cal_division):
            res_2 = 1
        elif set(c2_division) == set(cal_division):
            res_2 = 2
        else:
            res_2 = 0

        if res_2 == 1:
            for ind in qindxes:
                diff1.write(record[ind])
        elif res_2 == 2 and len(c1_taxonid) == 0:
            for ind in qindxes:
                diff3.write(record[ind])
        else:
            for ind in qindxes:
                if len(c1_taxonid) > 0:
                    diff2.write(record[ind])
                elif len(c2_taxonid) > 0:
                    diff4.write(record[ind])
                else:
                    diff5.write(record[ind])







