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
atm04mix = open(clstrfile+"_clusterwith3sets",'w')
atm04multi = open(clstrfile+"_multi",'w')
atm04else = open(clstrfile+"_elsemulti",'w')
atm04singleton = open(clstrfile+"_singleton",'w')
atm04elsesin = open(clstrfile+"_elsesingleton",'w')
with open(clstrfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clst = l1_split[0]
        atm01 = re.search(r'>PV_ATM01\w+', l1)
        nonatm01 = re.search(r'>PV_ATM02\w+', l1)
        atm02 = re.search(r'>PV_ATM03\w+', l1)
        nonatm02 = re.search(r'>PV_ATM04\w+', l1)
        atm03 = re.search(r'>PV_ATM05\w+', l1)
        atm04 = re.search(r'>PV_ATM06\w+', l1)
        if len(l1_split) > 3:
            if (atm01 or nonatm01 or atm02 or nonatm02 or atm03) and atm04:
                atm04mix.write(l1)
            elif atm04:
                atm04multi.write(l1)
            else:
                atm04else.write(l1)
        else:
            if atm04:
                atm04singleton.write(l1)
            else:
                atm04elsesin.write(l1)




