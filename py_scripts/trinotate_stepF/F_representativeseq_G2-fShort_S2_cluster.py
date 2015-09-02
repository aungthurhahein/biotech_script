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

clstrep2 = sys.argv[1]
clstfile = sys.argv[2]
group = sys.argv[3]     # string of clstgroup(glong,gshort)

clstid = []
clstrep = []
with open(clstrep2,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        clstid.append(line_split[0].strip())
        clstrep.append(line_split[1].strip())

with open(clstfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        cid = l2_split[0]
        tr_count = 0
        fknow_count = 0
        tr_mem = ""
        mem = ""

        for x in l2_split[1:]:
            if mem == "":
               mem = x
            else:
               mem += ";" + x

            trinity = re.search(r'>c\w+', x)
            Fknow = re.search(r'>PM_\w+', x)
            if trinity:
                tr_count += 1
                if tr_mem == "":
                    tr_mem = x
                else:
                    tr_mem += ";"+x
            elif Fknow:
                fknow_count += 1

        sys.stdout.write(cid+'\t'+str(group)+'\t'+str(len(l2_split[1:]))+'\t'+str(fknow_count)+'\t'+str(tr_count)+'\t'+clstrep[clstid.index(cid.strip())].strip('\n')+'\t'+mem.strip('\n')+'\t'+tr_mem+'\n')
