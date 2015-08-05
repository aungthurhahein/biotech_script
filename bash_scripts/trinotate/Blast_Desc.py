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
blastp_desc = sys.argv[1]
blastx_desc = sys.argv[2]

pid = []
pdesc = []
xid = []
xdesc = []
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
DB = "Trinotate"

with open(blastp_desc, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        print line_split
        pid.append(line_split[0].split('|')[0].strip())
        pdesc.append(line_split[17].strip(';').split('=')[1])

with open(blastx_desc, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        print line2_split
        xid.append(line2_split[0].strip())
        xdesc.append(line2_split[17].strip(';').split('=')[1])

uniqid = list(set(pid+xid))
uniqid.sort()
print len(uniqid)
out = open("BlastDescription.tsv_blasxp.tophit.summary",'w')
out.write("Trinity-ID\tBlastx\tBlastp\tDatabase\tDate\n")
for mem in uniqid:
    xdes = ""
    pdes = ""
    xind = [x for x, e in enumerate(xid) if e == mem]
    pind = [x2 for x2, e2 in enumerate(pid) if e2 == mem]
    for c,xi in enumerate(xind):
        if c == 0:
            xdes = xdesc[xi]
        else:
            xdes += xdesc[xi]+"|"
    for cp, pi in enumerate(pind):
        if cp == 0:
            pdes = pdesc[pi]
        else:
            pdes += pdesc[pi] + "|"
    if len(xind) == 0:
        xdes = "NaN"
    if len(pind) == 0:
        pdes = "NaN"
    out.write(mem+'\t'+xdes+'\t'+pdes+'\t'+DB+'\t'+date+'\n')




