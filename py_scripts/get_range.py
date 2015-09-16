#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

fileObj = sys.argv[1]
uniqid = sys.argv[2]

qallid = []
start=[]
end = []
with open(fileObj,'rb') as f1:
    for line in  f1:
        line_split = line.split('\t')
        qid = line_split[0]
        qallid.append(qid)
        start.append(int(line_split[1]))
        end.append(int(line_split[2]))

o = open(fileObj+"_out",'write')
uniqallqid = list(set(qallid))
for qid in uniqallqid:
    startind = [i for i,e in enumerate(qallid) if e == qid]
    ts = ""
    te = ""
    count = 0
    for x in startind:
        s = start[x]
        e = end[x]
        if count == 0:
            ts = s
            te = e
            count = 1
        print "bf", ts, te
        # if ts > s and te > e:    # both out of range
        #      print "r",s,e
        #      ts = s
        #      te = e
        if ts > s and ts > e:  # both out of range at start side
            sys.stdout.write(qid + '\t' + str(s) + '\t' + str(e) + "\t" + "x" + '\n')
        elif te < s and te < e:  # both out of range at end side
            sys.stdout.write(qid+'\t'+str(s)+'\t'+str(e)+"\t"+"y"+'\n')
        elif ts > s and te >= e:  # start out of range
            print "s", s, e
            ts = s
        elif ts <= s and te < e:  # end out of range
            print "e", s, e
            te = e
        else:                     # both in range #ignore
            print "na", s, e
        print "af",ts, te
        print "\n"
    o.write(qid+'\t'+str(ts)+'\t'+str(te)+'\n')





