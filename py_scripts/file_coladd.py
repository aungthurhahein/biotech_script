#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
file = sys.argv[1]
openfile = open(file, 'r')

for x in openfile:
    x_split = x.split('\t')
    D_col = x_split[0]
    for k, i in enumerate(x_split):
        if D_col == "#D":
            col_38 = x_split[37].strip('\n')
            col_30 = x_split[30]
            col_31 = x_split[31]
            col_32 = x_split[32]
            col_33 = x_split[33]
            if k == 0:
                col_first = col_38.split('-')[0]
                if col_first == "6A":
                    sys.stdout.write("#D-NCal")
                elif col_first == "6B":
                    sys.stdout.write("#D-NC1")
                elif col_first == "6C":
                    sys.stdout.write("#D-NC2")
                sys.stdout.write("\t")
            elif k == 8:
                sys.stdout.write(i)
                sys.stdout.write("\t")
                sys.stdout.write(col_30)
                sys.stdout.write("\t")
                sys.stdout.write(col_31)
                sys.stdout.write("\t")
                sys.stdout.write(col_32)
                sys.stdout.write("\t")
                sys.stdout.write(col_33)
                sys.stdout.write("\t")
            else:
                sys.stdout.write(i.strip())
                sys.stdout.write("\t")
        else:
            sys.stdout.write(i.strip())
            sys.stdout.write("\t")
    sys.stdout.write("\n")
