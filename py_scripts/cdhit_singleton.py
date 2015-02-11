#! /usr/bin/env python
"""
#--------------------------------------------------------------------------#
# cdhit file parser to get singleton members
# __author__ = 'atrx'
# Date: 13012015
#--------------------------------------------------------------------------#
"""
import sys
import linecache

usage= "Usage %s infile" % sys.argv[0] # specific massage for no input

try:
    statsfile = sys.argv[1]
    singletonfile = sys.argv[2]
except:
    print usage, sys.exit(1)

def rewind(f):
    f.seek(0)

statsfile = open(statsfile,'r')
count = 0

for line in statsfile:
    singfile = open(singletonfile,'r')
    count = count+1
    if ">Cluster" in line:
        for singleton in singfile:
            clst = singleton.split(":")
            if line.strip() == clst[0].strip():
                print line,
                print linecache.getline(sys.argv[1], count+1)
                print linecache.getline(sys.argv[1], count+2)
                print linecache.getline(sys.argv[1], count+3)
                print linecache.getline(sys.argv[1], count+4)
                print linecache.getline(sys.argv[1], count+5)
                print linecache.getline(sys.argv[1], count+6)