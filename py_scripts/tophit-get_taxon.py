#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
file6A = sys.argv[1]
file6B = sys.argv[2]
file6C = sys.argv[3]
fileid = sys.argv[4]

open6A = open(file6A, 'r')
open6B = open(file6B, 'r')
open6C = open(file6C, 'r')
openid = open(fileid, 'r')

id_6A = []
record_6A = []
id_6B = []
record_6B = []
id_6C = []
record_6C = []

for line in open6A:
    line_split = line.split('\t')
    id_6A.append(line_split[0].strip())
    record_6A.append(line.strip('\n'))

for line2 in open6B:
    line2_split = line2.split('\t')
    id_6B.append(line2_split[0].strip())
    record_6B.append(line2.strip('\n'))

for line3 in open6C:
    line3_split = line3.split('\t')
    id_6C.append(line3_split[0].strip())
    record_6C.append(line3.strip('\n'))

for queryid in openid:
    id_clean = queryid.strip().strip('\n').strip('>')
    A6_indices = [i for i, x in enumerate(id_6A) if x == id_clean]
    B6_indices = [i for i, x in enumerate(id_6B) if x == id_clean]
    C6_indices = [i for i, x in enumerate(id_6C) if x == id_clean]
    for A6 in A6_indices:
        print record_6A[A6] + '\t' + '6A' + '\t' + fileid
    for B6 in B6_indices:
        print record_6B[B6] + '\t' + '6B' + '\t' + fileid
    for C6 in C6_indices:
        print record_6C[C6] + '\t' + '6C' + '\t' + fileid