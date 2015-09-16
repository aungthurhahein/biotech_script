#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
import re

clstfile = sys.argv[1]  # parse cluster file G2
lenfile = sys.argv[2]  # lenfile

clstid = []
memid = []
with open(clstfile, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        clstid.append(line_split[0])
        memid.append(line_split[1:])

qid = []
qlen = []
with open(lenfile, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        qid.append(">"+line2_split[0].strip())
        qlen.append(int(line2_split[1].strip('\n')))

kshort = open(clstfile+"_G2_fshrot",'w')
klong = open(clstfile+"_G2_flong",'w')

for x, clst in enumerate(clstid):
    trlen = []
    liblen = []
    tempmem = ""
    for l,mem in enumerate(memid[x]):
        lib_id = re.search(r'>c\w+', mem)       # trinity
        tr_id = re.search(r'>PM_\w+', mem)      # FKnown
        tr_id2 = re.search(r'>MR_\w+', mem)  # FKnown
        tr_id3 = re.search(r'>SO_\w+', mem)  # FKnown

        if len(memid[x]) == (l+1):
            tempmem += mem
        else:
            tempmem += mem + "\t"
        if mem.strip('\n').strip() in qid:
            ind = qid.index(mem.strip('\n').strip())
            if tr_id or tr_id2 or tr_id3:
                trlen.append(qlen[ind])
            elif lib_id:
                liblen.append(qlen[ind])
    print trlen, liblen
    # g2-kshort
    if max(liblen) < max(trlen):
        kshort.write(clst + "\t" + tempmem)
    elif max(liblen) >= max(trlen):
        klong.write(clst + "\t" + tempmem)


