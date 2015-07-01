#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
blastn = sys.argv[1]
blastx = sys.argv[2]
matrix = sys.argv[3]
target = sys.argv[4]

openblastn = open(blastn, 'r')
openblastx = open(blastx, 'r')
openmatrix = open(matrix, 'r')
opentarget = open(target, 'r')

blastn_id = []
blastn_record = []
for line in openblastn:
    line_split = line.split('\t')
    DorNot = line_split[0].split('-')[0]
    if DorNot == "#D":
        blastn_id.append(line_split[3])
        blastn_record.append(line)

blastx_id = []
blastx_record = []
for line2 in openblastx:
    line2_split = line2.split('\t')
    blastx_id.append(line2_split[3])
    blastx_record.append(line2)

matrix_id = []
matrix_record = []
for line3 in openmatrix:
    line3_split = line3.split('\t')
    matrix_id.append(line3_split[0].strip('>'))
    matrix_record.append(line3)

target_id = []
target_record = []
for line4 in opentarget:
    line4_split = line4.split('\t')
    target_id.append(line4_split[0].strip('>'))
    target_record.append(line4)

for k,tid in enumerate(target_id):
    sys.stdout.write(">"+tid+"\n")
    blastn_ind = [i for i, e in enumerate(blastn_id) if e == tid]
    blastx_ind = [i for i, e in enumerate(blastx_id) if e == tid]
    matrix_ind = [i for i, e in enumerate(matrix_id) if e == tid]

    for mid in matrix_ind:
        sys.stdout.write("#A\t"+ matrix_record[mid])
    sys.stdout.write("#B\t" + target_record[k])
    for nind in blastn_ind:
        sys.stdout.write("#D\t" + blastn_record[nind])
    for xind in blastx_ind:
        sys.stdout.write("#X\t" + blastx_record[xind])
    sys.stdout.write("//\n")



