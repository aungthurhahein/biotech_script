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
        trig = 0

        if len(l_split) == 6:
            for line in l_split[1:]:
                line = line.replace(".", "-")
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line and 'N' not in line and '|' not in line:
                    print line
                else:
                    newline.append(l)
                    break
        elif len(l_split) == 7:
            for line in l_split[2:]:
                line = line.replace(".", "-")
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line and 'N' not in line and '|' not in line:
                    print line
                else:
                    newline.append(l)
                    break
        elif len(l_split) == 8:
            for line in l_split[3:]:
                line = line.replace(".", "-")
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line and 'N' not in line and '|' not in line:
                    print line
                else:
                    newline.append(l)
                    break
        elif len(l_split) < 6 and len(l_split) > 1:
            for line in l_split[1:]:
                line = line.replace(".", "-")
                if '-' in line and 'A' not in line and 'G' not in line and 'C' not in line and 'T' not in line and 'N' not in line and '|' not in line:
                    print line
                else:
                    newline.append(l)
                    break
        else:
            newline.append(l)

for x in newline:
    o.write(x.replace(".", "-"))