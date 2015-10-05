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
        pid.append(line_split[0].split('|')[0].strip())
        pdesc.append(line_split[17].strip(';').split('=')[1].strip('|'))

with open(blastx_desc, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        xid.append(line2_split[0].strip())
        xdesc.append(line2_split[17].strip(';').split('=')[1].strip('|'))

uniqid = list(set(pid+xid))
uniqid.sort()
out = open("BlastDescription.tsv_blasxp.tophit.summary",'w')
out.write("Trinity-ID\tBlastx\tBlastp\tDatabase\tDate\n")
for mem in uniqid:
    xdes = []
    pdes = []
    xind = [x for x, e in enumerate(xid) if e == mem]
    pind = [x2 for x2, e2 in enumerate(pid) if e2 == mem]
    for c,xi in enumerate(xind):
        if c == 0:
            xdes.append(xdesc[xi])
        else:
            xdes.append(xdesc[xi])
    for cp, pi in enumerate(pind):
        if cp == 0:
            pdes.append(pdesc[pi])
        else:
            pdes.append(pdesc[pi])
    if len(xind) == 0:
        xdes.append("NaN")
    if len(pind) == 0:
        pdes.append("NaN")
    uniqxdes = list(set(xdes))
    uniqpdes = list(set(pdes))
    tmp1 = ""
    for m in uniqxdes:
        if tmp1 == "":
            tmp1 = m.split("{")[0].strip("|")
        else:
            tmp1 += "|"+m.split("{")[0].strip("|")

    tmp2 = ""
    for m2 in uniqpdes:
        if tmp2 == "":
            tmp2 = m2.split("{")[0].strip("|")
        else:
            tmp2 += "|" + m2.split("{")[0].strip("|")
    out.write(mem+'\t'+tmp1+'\t'+tmp2+'\t'+DB+'\t'+date+'\n')




