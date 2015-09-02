#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import re

atm03lst = sys.argv[1]
atmall = sys.argv[2]
clst = sys.argv[3]
clstgroup = sys.argv[4]

atm03id = []
atm03lng = []
with open(atm03lst,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        atm03id.append(line_split[0])
        atm03lng.append(line_split[1].strip('\n'))

atmallid = []
atmalllng = []
with open(atmall, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        atmallid.append(line2_split[0])
        atmalllng.append(line2_split[1].strip('\n'))

clst_id = []
clst_group = []
with open(clstgroup, 'rb') as f5:
    for line5 in f5:
        line5_split = line5.split('\t')
        clst_id.append(line5_split[0])
        clst_group.append(line5_split[1].strip('\n'))

record = []
with open(clst,'rb') as f3:
    for line7 in f3:
        record.append(line7)

o = open("atm03.matrix", 'w')

output = []
for line3 in record:
    line3_split = line3.split('\t')
    clstid = line3_split[0]

    tmp_atm01 = []
    tmp_nonatm01 = []
    tmp_atm02 = []
    tmp_nonatm02 = []
    tmp_atm03 = []

    tmpln_atm01 = []
    tmpln_nonatm01 = []
    tmpln_atm02 = []
    tmpln_nonatm02 = []
    tmpln_atm03 = []

    for x in line3_split[1:]:
        x = x.strip('>').strip()
        atm01 = re.search(r'PV_ATM01\w+', x)
        nonatm01 = re.search(r'PV_ATM02\w+', x)
        atm02 = re.search(r'PV_ATM03\w+', x)
        nonatm02 = re.search(r'PV_ATM04\w+', x)
        atm03 = re.search(r'PV_ATM05\w+', x)
        if atm01:
            tmp_atm01.append(x)
            ind = atmallid.index(x)
            tmpln_atm01.append(int(atmalllng[ind]))
        elif nonatm01:
            tmp_nonatm01.append(x)
            ind = atmallid.index(x)
            tmpln_nonatm01.append(int(atmalllng[ind]))
        elif atm02:
            tmp_atm02.append(x)
            ind = atmallid.index(x)
            tmpln_atm02.append(int(atmalllng[ind]))
        elif nonatm02:
            tmp_nonatm02.append(x)
            ind = atmallid.index(x)
            tmpln_nonatm02.append(int(atmalllng[ind]))
        elif atm03:
            tmp_atm03.append(x)
            ind = atm03id.index(x)
            tmpln_atm03.append(int(atm03lng[ind]))

    for k,mem in enumerate(tmp_atm03):
        if clstid in clst_id:
            outgroup = clst_group[clst_id.index(clstid)]

        if len(tmpln_atm01) > 0:
            atm01max = max(tmpln_atm01)
        else:
            atm01max = "NaN"

        if len(tmpln_nonatm01) > 0:
            nonatm01max = max(tmpln_nonatm01)
        else:
            nonatm01max = "NaN"

        if len(tmpln_atm02) > 0:
            atm02max = max(tmpln_atm02)
        else:
            atm02max = "NaN"

        if len(tmpln_nonatm02) > 0:
            nonatm02max = max(tmpln_nonatm02)
        else:
            nonatm02max = "NaN"

        sys.stdout.write(mem+'\t'+str(tmpln_atm03[k])+'\t'+outgroup+'\t'+clstid+'\t'+str(atm01max)+'\t'+str(nonatm01max)+'\t'+str(atm02max)+'\t'+str(nonatm02max)+'\n')
        output.append(mem+'\t'+str(tmpln_atm03[k])+'\t'+outgroup+'\t'+clstid+'\t'+str(atm01max)+'\t'+str(nonatm01max)+'\t'+str(atm02max)+'\t'+str(nonatm02max)+'\n')

for res in output:
    o.write(res)

