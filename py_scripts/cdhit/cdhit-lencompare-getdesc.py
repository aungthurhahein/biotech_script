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
import datetime
clstfile = sys.argv[1]  # parse cluster file
lenfile = sys.argv[2]  # lenfile
descfile = sys.argv[3]

database = []
clstid = []
memid = []
with open(clstfile, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        database.append(line_split[0])
        clstid.append(line_split[1])
        memid.append(line_split[1:])

qid = []
qlen = []
with open(lenfile, 'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        qid.append(">"+line2_split[0].strip())
        qlen.append(int(line2_split[1].strip('\n')))

descid = []
desc = []
with open(descfile, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        descid.append(line3_split[0])
        desc.append(line3_split[3])
for x, clst in enumerate(clstid):
    trid = []
    trclust = []
    liblen = {}
    for l, mem in enumerate(memid[x]):
        lib_id = re.search(r'>gpat\w+', mem)
        tr_id = re.search(r'>PM_\w+', mem)
        if mem.strip('\n').strip() in qid:
            ind = qid.index(mem.strip('\n').strip())
            if lib_id:
                liblen[mem.strip('>')] = qlen[ind]
        if tr_id:
            trid.append(mem.strip('\n').strip())
            trclust.append(clst)

    d_sorted = dict(sorted(zip(liblen.values(), liblen.keys()), reverse=True))
    for x, tid in enumerate(trid):
        tmp = tid
        db = database[clstid.index(trclust[x])]
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        descrec = ""
        longdesc = ""
        count = 0
        for k,v in d_sorted.iteritems():
            if v.strip() in descid:
                if count == 0:
                    longdesc = desc[descid.index(v.strip())]
                elif count == 1:
                    descrec += desc[descid.index(v.strip())]
                else:
                    descrec += desc[descid.index(v.strip())]+'|'
            count += 1
        sys.stdout.write(tmp.strip(">")+'\t'+longdesc+'\t'+db+'\t'+date+'\t'+descrec+'\n')


