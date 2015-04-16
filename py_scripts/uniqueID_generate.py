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
open_file = open(mapfile, 'r')

for line in open_file:
    line_split = line.split(',')
    print ">e01pm_unm01Aung_"+line_split[0].strip('\"'), '\t', line_split[1].strip('\n').strip('\"')