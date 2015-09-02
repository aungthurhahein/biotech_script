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
file2 = sys.argv[1]
filecluster = sys.argv[2]

aid =[]
arecord=[]
with open(file2,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        if line_split[2] == "n":
            aid.append(line_split[1].strip('>'))
            arecord.append(line.strip('\n'))
allind= []
with open(filecluster,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        tmp_pm = ""
        tmp_con = 0
        for x in line2_split:
            cond1 = re.search(r'>PV_ATM01\w+', x)
            if cond1:
                if tmp_pm == "":
                    tmp_pm += x.strip('>').strip()
                else:
                    tmp_pm += "|" + x.strip('>').strip()

            if x.strip('>').strip() in aid:
                ind = aid.index(x.strip('>').strip())
                tmp_con = 1
            if tmp_con == 1:
                allind.append(ind)
                sys.stdout.write(arecord[ind]+'\t'+tmp_pm+'\n')

for x,line in enumerate(arecord):
    if x not in allind:
        sys.stdout.write(line)
