#! /usr/bin/env python
#--------------------------------------------------------------------------#
# simple file reader template without argparse module
# __author__ = 'atrx'
#--------------------------------------------------------------------------#

import sys

usage= "Usage %s infile" % sys.argv[0] #specific massage for no input

try:
    infile = sys.argv[1]
except:
    print usage, sys.exit(1)

ifile = open(infile,'r') #open file read

for line in ifile:
    yvalue = line.split()
    if len(yvalue) == 0: continue #skipping blank lines

