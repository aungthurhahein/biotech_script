#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
infile = sys.argv[1]
newline=[]
o = open(infile+"_strip.out", 'w')

with open(infile, 'rb') as f1:
    for l in f1:
        l_split = l.split()
        # print l_split
        trig = 0
        # l_split= l_split.replace(".", "-")
        if len(l_split) == 6:
            for line in l_split[1:]:
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line:
                    print line
                else:
                    if l not in newline:
                        newline.append(l)
                    break
        elif len(l_split) == 7:
            for line in l_split[2:]:
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line:
                    print line
                else:
                    if l not in newline:
                        newline.append(l)
                    break
        elif len(l_split) == 8:
            for line in l_split[3:]:
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line:
                    print line
                else:
                    if l not in newline:
                        newline.append(l)
                    break
        else:
            newline.append(l)

for x in newline:
    o.write(x.replace(".", "-"))