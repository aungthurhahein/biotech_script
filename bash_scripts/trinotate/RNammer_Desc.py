#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import datetime
blast_desc = sys.argv[1]

xid = []
xdesc = []
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
DB = "Trinotate"

with open(blast_desc, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        if len(line2_split[1].strip(';').split('=')[1]) > 1:
            xid.append(line2_split[0].strip())
            xdesc.append(line2_split[1].strip(';').split('=')[1])

uniqid = list(set(xid))
uniqid.sort()

out = open("rnammer_desc.tsv.summary", 'w')
out.write("Trinity-ID\tDescription\tDatabase\tDate\n")
for mem in uniqid:
    xdes = ""
    pdes = ""
    xind = [x for x, e in enumerate(xid) if e == mem]
    for c,xi in enumerate(xind):
        if c == 0:
            xdes = xdesc[xi].strip('\n')
        else:
            xdes += xdesc[xi].strip('\n')+"|"
    if len(xind) == 0:
        xdes = "NaN"
    out.write(mem+'\t'+xdes+'\t'+DB+'\t'+date+'\n')




