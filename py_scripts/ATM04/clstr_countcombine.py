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

atm04clst = sys.argv[1]
atm03matrix = sys.argv[2]

repid = []
rep_atm03 = []
ATM_set02 = []
nonATM_set02 = []
ATM_set01 = []
nonATM_set01 = []

with open(atm03matrix,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        repid.append(l2_split[1].strip('>').strip())
        rep_atm03.append(int(l2_split[3]))
        ATM_set02.append(int(l2_split[4]))
        nonATM_set02.append(int(l2_split[5]))
        ATM_set01.append(int(l2_split[6]))
        nonATM_set01.append(int(l2_split[7].strip('\n')))

with open(atm04clst,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        atm04clstid = l1_split[0]

        atm04_count = 0
        atm03_count = 0
        nonatm01 = 0
        nonatm02 = 0
        atm02 = 0
        atm01 = 0

        for m in l1_split[1:]:
            m = m.strip('\n').strip().strip('>')
            atm04 = re.search(r'PV_ATM06\w+', m)

            if atm04:
                atm04_count += 1

            if m in repid:
                ind = repid.index(m)
                repatm01 = re.search(r'PV_ATM01\w+', m)
                repnonatm01 = re.search(r'PV_ATM02\w+', m)
                repatm02 = re.search(r'PV_ATM03\w+', m)
                repnonatm02 = re.search(r'PV_ATM04\w+', m)
                repatm03 = re.search(r'PV_ATM05\w+', m)

                if repatm01:
                    atm01 += 1
                elif repnonatm01:
                    nonatm01 += 1
                elif repatm02:
                    atm02 += 1
                elif repnonatm02:
                    nonatm02 += 1
                elif repatm03:
                    atm03_count += 1
                atm03_count += rep_atm03[ind]
                nonatm01 += nonATM_set01[ind]
                nonatm02 += nonATM_set02[ind]
                atm01 += ATM_set01[ind]
                atm02 += ATM_set02[ind]

        sys.stdout.write(atm04clstid+"\t"+str(atm04_count)+"\t"+str(atm03_count)+"\t"+str(nonatm02)+"\t"+str(atm02)+"\t"+str(nonatm01)+"\t"+str(atm01)+"\n")


