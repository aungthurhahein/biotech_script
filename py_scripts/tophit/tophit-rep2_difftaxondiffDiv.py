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
catgroup = []
division20 = []
qid = []
mapfile_record = []
group_priortiy = {'-':0, 'I1': 1, 'I2': 2, 'I4': 3, 'I7': 4, 'I6': 5, 'I5': 6, 'I3': 6, 'Mammals': 6, 'Primates': 6,
                  'Rodents': 6,'Vertebrates': 6, 'I8': 7, 'Plants': 8, 'Bacteria': 9, 'Viruses': 10, 'Phages': 10,
                  '\'Environmental': 11, 'Synthetic': 11, 'NOINFO': 12, 'NaN': 12,'Unassigned':12}

with open(mapfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        catgroup.append(line_split[0])
        qid.append(line_split[1])
        division20.append(line_split[5])
        mapfile_record.append(line)

uniq_qid = list(set(qid))
for queryid in uniq_qid:
    indexes = [i for i,e in enumerate(qid) if e == queryid]
    tmp_c1 = []
    tmp_c2 = []
    tmp_cal = []
    tmp_c1div = []
    tmp_c2div = []
    tmp_caldiv = []
    for i in indexes:
        if catgroup[i] == "#XC1":
            tmp_c1.append(i)
            tmp_c1div.append(division20[i])
        elif catgroup[i] == "#XC2":
            tmp_c2.append(i)
            tmp_c2div.append(division20[i])
        elif catgroup[i] == "#XCal":
            tmp_cal.append(i)
            tmp_caldiv.append(division20[i])

    if len(tmp_c1) > 0:
        c1div = list(set(tmp_c1div))
        caldiv = list(set(tmp_caldiv))
        tmp_c1max = []
        tmp_calmax = []
        for c1M in c1div:
            tmp_c1max.append(group_priortiy[c1M])
        for calM in caldiv:
            tmp_calmax.append(group_priortiy[calM])

        if max(tmp_c1max) < max(tmp_calmax):
            for c1 in tmp_c1:
                sys.stdout.write(mapfile_record[c1])
        elif max(tmp_calmax) < max(tmp_c1max):
            for cal in tmp_cal:
                sys.stdout.write(mapfile_record[cal])
        elif max(tmp_calmax) == max(tmp_c1max):
            for cal in tmp_cal:
                sys.stdout.write(mapfile_record[cal])

    elif len(tmp_c1) == 0 and len(tmp_c2) > 0:
        c2div = list(set(tmp_c2div))
        caldiv = list(set(tmp_caldiv))
        tmp_c2max = []
        tmp_calmax = []
        for c2M in c2div:
            tmp_c2max.append(group_priortiy[c2M])
        for calM in caldiv:
            tmp_calmax.append(group_priortiy[calM])
        if max(tmp_c2max) < max(tmp_calmax):
            for c2 in tmp_c2:
                sys.stdout.write(mapfile_record[c2])
        elif max(tmp_calmax) < max(tmp_c2max):
            for cal in tmp_cal:
                sys.stdout.write(mapfile_record[cal])
        elif max(tmp_calmax) == max(tmp_c2max):
            for cal in tmp_cal:
                sys.stdout.write(mapfile_record[cal])


