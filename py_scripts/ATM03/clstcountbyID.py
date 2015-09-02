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
clst = sys.argv[1]

atm01count = 0
nonatm01count = 0
atm02count = 0
nonatm02count = 0
atm03count = 0
with open(clst, 'rb') as f5:
    for line5 in f5:
        line5_split = line5.split('\t')
        for x in line5_split[1:]:
            atm01 = re.search(r'>PV_ATM01\w+', x)
            nonatm01 = re.search(r'>PV_ATM02\w+', x)
            atm02 = re.search(r'>PV_ATM03\w+', x)
            nonatm02 = re.search(r'>PV_ATM04\w+', x)
            atm03 = re.search(r'>PV_ATM05\w+', x)
            if atm01:
                atm01count +=1
            elif nonatm01:
                nonatm01count +=1
            elif atm02:
                atm02count +=1
            elif nonatm02:
                nonatm02count +=1
            elif atm03:
                atm03count +=1


print "ATM01"+"\t"+str(atm01count)
print "NonATM01"+"\t"+str(nonatm01count)
print "ATM02"+"\t"+str(atm02count)
print "NonATM02"+"\t"+str(nonatm02count)
print "ATM03"+"\t"+str(atm03count)