#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

featfile = sys.argv[1]
seqlenfile = sys.argv[2]

blastp = open(featfile+"_blastp",'w')
blastx = open(featfile+"_blastx",'w')

tr_id = []
tr_len = []
with open(seqlenfile,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        tr_id.append(line2_split[0])
        tr_len.append(line2_split[1])

with open(featfile, 'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        trid = line_split[0]  # Trinity_ID
        xorp = trid.split('|')
        tmp_row = ""
        query_cov = 0
        query_covall = 0
        for x, col in enumerate(line_split):
            if x == 0:
                tmp_row = col+'\t'
            elif x == 9:
                if xorp[0] in tr_id:
                    query_cov = abs(float(line_split[5]) - float(line_split[4])) - 1
                    seqlen = int(tr_len[tr_id.index(xorp[0])])
                    query_covall = query_cov/seqlen
                    print seqlen, query_cov, str(query_covall)
                    tmp_row += col+'\t'+str(query_covall)+'\t'
            elif len(line_split) == x+1:
                tmp_row += col
            else:
                tmp_row += col+"\t"

        if len(xorp) > 1:
            blastp.write(tmp_row)
        else:
            blastx.write(tmp_row)
