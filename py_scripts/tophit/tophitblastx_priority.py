#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
map = sys.argv[1]
openmap = open(map, 'r')

cat = []
queryid = []
record = []

f1 = open("tophit-blastx.map_6B",'w') # C1
f2 = open("tophit-blastx.map_6C",'w') # C2
f3 = open("tophit-blastx.map_6A",'w') #Cal
log = open('priority_log','w')

for line in openmap:
    line_split = line.split('\t')
    cat.append(line_split[0].strip())
    queryid.append(line_split[1].strip())
    record.append(line)

uniqueid_list = [e for i, e in enumerate(queryid) if queryid.index(e) == i ]  # get unique records

for qid in uniqueid_list:
    indexes = [ i for i, e in enumerate(queryid) if e == qid]  # get all indexes with same value
    xc1_ind = []
    xc2_ind = []
    xcal_ind = []

    for ind in indexes:
        if cat[ind] == "#XC1":
            xc1_ind.append(ind)
        elif cat[ind] == "#XC2":
            xc2_ind.append(ind)
        elif cat[ind] == "#XCal":
            xcal_ind.append(ind)

    print qid,xc1_ind,xc2_ind,xcal_ind
    for i in indexes:
        print record[i]

    if len(xc1_ind) > 0:
        for x1 in xc1_ind:
            f1.write(record[x1])
            log.write(qid+"\t"+'B1'+'\n')
    elif len(xc2_ind) > 0 and len(xc1_ind) == 0:
        for x2 in xc2_ind:
            f2.write(record[x2])
            log.write(qid + "\t" + 'C1' + '\n')
    elif len(xcal_ind) > 0 and len(xc1_ind) == 0 and len(xc2_ind) == 0:
        for x3 in xcal_ind:
            f3.write(record[x3])
            log.write(qid + "\t" + 'A1' + '\n')

    # for ind2 in indexes:
    #     del cat[ind2]
    #     del queryid[ind2]
    #     del record[ind2]
