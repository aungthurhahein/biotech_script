#! /usr/bin/env python
# --------------------------------------------------------------------------#
# cdhit file parser to see existence of data sets
# __author__ = 'atrx'
# Date: 13012015
#--------------------------------------------------------------------------#

import sys
import linecache
import re

usage = "Usage %s infile" % sys.argv[0]  #specific massage for no input

try:
    statsfile = sys.argv[1]
except:
    print usage, sys.exit(1)

statsfile = open(statsfile, 'r')
count = 0
set_count = 0

count = count + 1
if ">Cluster" in line:
    line1 = linecache.getline(sys.argv[1], count + 1)
    id1 = line1.split(" ")
    line2 = linecache.getline(sys.argv[1], count + 3)
    id2 = line2.split(" ")
    line3 = linecache.getline(sys.argv[1], count + 5)
    id3 = line3.split(" ")
    line4 = linecache.getline(sys.argv[1], count + 7)
    id4 = line4.split(" ")
    line5 = linecache.getline(sys.argv[1], count + 9)
    id5 = line5.split(" ")

    cond1 = re.search(r'c01_PM\w+', str(id1[1]))
    cond2 = re.search(r'c\w+_g\w+_i\w+', str(id1[1]))
    cond3 = re.search(r'c01_PM\w+', str(id2[1]))
    cond4 = re.search(r'c\w+_g\w+_i\w+', str(id2[1]))
    cond5 = re.search(r'c01_PM\w+', str(id3[1]))
    cond6 = re.search(r'c\w+_g\w+_i\w+', str(id3[1]))
    cond7 = re.search(r'c01_PM\w+', str(id4[1]))
    cond8 = re.search(r'c\w+_g\w+_i\w+', str(id4[1]))
    cond9 = re.search(r'c01_PM\w+', str(id5[1]))
    cond10 = re.search(r'c\w+_g\w+_i\w+', str(id5[1]))

    if cond1 and cond4:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond2 and cond3:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond1 and cond6:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond2 and cond5:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond3 and cond6:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond4 and cond5:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond1 and cond8:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond2 and cond7:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond3 and cond8:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond4 and cond7:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond5 and cond8:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond6 and cond7:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond1 and cond10:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond2 and cond9:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond3 and cond10:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond4 and cond9:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond5 and cond10:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond6 and cond9:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond7 and cond10:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
    elif cond8 and cond9:
        print line.strip(),
        print "\t",
        print id1[1],
        print "\t",
        print id2[1],
        print "\t",
        print id3[1],
        print "\t",
        print id4[1],
        print "\t",
        print id5[1]
        set_count = set_count + 1
print set_count