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

clstrfile = sys.argv[1]
clstrfile_read = open(clstrfile, 'r')
cluster_list = []

with open(clstrfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        rep = l1_split[1]
        total_mem = len(l1_split[2].rstrip('|').split('|'))
        count_atm01 = 0
        count_nonatm01 = 0
        count_atm02 = 0
        count_nonatm02 = 0
        count_atm03 = 0
        for m in l1_split[2].split('|'):
            atm01 = re.search(r'>PV_ATM01\w+', m)
            nonatm01 = re.search(r'>PV_ATM02\w+', m)
            atm02 = re.search(r'>PV_ATM03\w+', m)
            nonatm02 = re.search(r'>PV_ATM04\w+', m)
            atm03 = re.search(r'>PV_ATM05\w+', m)
            if atm01:
                count_atm01 += 1
            elif nonatm01:
                count_nonatm01 += 1
            elif atm02:
                count_atm02 += 1
            elif nonatm02:
                count_nonatm02 += 1
            elif atm03:
                count_atm03 += 1
        sys.stdout.write(l1_split[0]+"\t"+rep+"\t"+str(total_mem)+"\t"+str(count_atm03)+"\t"+str(count_atm02)+"\t"+str(count_nonatm02)+"\t"+str(count_atm01)+"\t"+str(count_nonatm01)+'\n')
