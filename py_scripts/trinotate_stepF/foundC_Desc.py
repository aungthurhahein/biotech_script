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
        qid.append(line2_split[0].strip().strip('>'))
        qlen.append(int(line2_split[1].strip('\n')))

descid = []
desc = []

with open(descfile, 'rb') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        descid.append(line3_split[0].strip('>'))
        desc.append(line3_split[1])

for x, clst in enumerate(clstid):
    trid = []
    trclust = []
    liblen = {}
    for l, mem in enumerate(memid[x]):
        lib_id = re.search(r'>PM\w+', mem)
        lib_id2 = re.search(r'>MR\w+', mem)
        lib_id3 = re.search(r'>SO_PAO\w+', mem)
        tr_id = re.search(r'>c\w+', mem)

        if mem.strip('\n').strip('>').strip() in qid:
            ind = qid.index(mem.strip('\n').strip('>').strip())
            if lib_id or lib_id2 or lib_id3:
                liblen[int(qlen[ind])] = mem.strip('\n').strip('>').strip()

        if tr_id:
            trid.append(mem.strip('\n').strip('>').strip())
            trclust.append(clst.strip('\n'))

    # d_sorted = dict(sorted(zip(liblen.values(), liblen.keys()), reverse=True))

    for x, tid in enumerate(trid):
        tmp = tid
        db = "FKNOWN20150820"
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d")
        descrec = ""
        longdesc = ""
        count = 0
        for k in sorted(liblen.iterkeys(),reverse=True):
            if liblen[k].strip() in descid:
                if count == 0:
                    longdesc = desc[descid.index(liblen[k].strip())].strip('\n')
                elif count == 1:
                    descrec += desc[descid.index(liblen[k].strip())].strip('\n')
                else:
                    descrec += desc[descid.index(liblen[k].strip())].strip('\n') + ';'
            count += 1
        sys.stdout.write(tmp.strip(">") + '\t' + longdesc + '\t' + db + '\t' + date + '\t' + descrec + '\n')


