#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

matrixfile = sys.argv[1]
queryfile = sys.argv[2]
openmatrix = open(matrixfile, 'r')
openquery = open(queryfile, 'r')

matrixqueryid = []
atm80 = []
nonshrimp80 = []
matrix_record = []

for line in openmatrix:
    line_split = line.split('\t')
    matrixqueryid.append(line_split[0])
    atm80.append(line_split[6])
    nonshrimp80.append(line_split[11])
    matrix_record.append(line)

QueryID = []
BlastN  = []
BlastX  = []
QueryCatX = []
QueryCatCX = []
QueryCatCQ = []
QueryCatQ = []
queryrecord = []
for line2 in openquery:
    line2_split = line2.split('\t')
    QueryID.append(line2_split[0])
    BlastN.append(line2_split[1])
    BlastX.append(line2_split[2])
    QueryCatX.append(line2_split[3])
    QueryCatCX.append(line2_split[4])
    QueryCatCQ.append(line2_split[5])
    QueryCatQ.append(line2_split[6])
    queryrecord.append(line2)

i66b = open("I66A", 'w')
i66c = open("I66B", 'w')
i66d = open("I66C", 'w')

i86b = open("I86A", 'w')
i86c = open("I86B", 'w')
i86d = open("I86C", 'w')

D6b = open("D6A", 'w')
D6c = open("D6B", 'w')
D6d = open("D6C", 'w')

E6b = open("E6A", 'w')
E6c = open("E6B", 'w')
E6d = open("E6C", 'w')
log = open("else.log",'w')

for x, qid in enumerate(matrixqueryid):
    if atm80[x] == "y" and nonshrimp80[x] == "y":
        if qid in QueryID:
            ind = QueryID.index(qid)
            # I6-6B, I6-6C, I6-6D
            if BlastN[ind] == "6A-I6" or BlastX[ind] == "6A-I6" or QueryCatX[ind] == "6A-I6" or QueryCatCX[ind] == "6A-I6" or QueryCatCQ[ind] == "6A-I6" or QueryCatQ[ind] == "6A-I6":
                i66b.write(qid+"\n")
                i66b.write(matrix_record[x])
                i66b.write(queryrecord[ind])
                i66b.write("//"+"\n")
            elif BlastN[ind] == "6B-I6" or BlastX[ind] == "6B-I6" or QueryCatX[ind] == "6B-I6" or QueryCatCX[ind] == "6B-I6" or QueryCatCQ[ind] == "6B-I6" or QueryCatQ[ind] == "6B-I6":
                i66c.write(qid+"\n")
                i66c.write(matrix_record[x])
                i66c.write(queryrecord[ind])
                i66c.write("//"+"\n")
            elif BlastN[ind] == "6C-I6" or BlastX[ind] == "6C-I6" or QueryCatX[ind] == "6C-I6" or QueryCatCX[ind] == "6C-I6" or QueryCatCQ[ind] == "6C-I6" or QueryCatQ[ind] == "6C-I6":
                i66d.write(qid+"\n")
                i66d.write(matrix_record[x])
                i66d.write(queryrecord[ind])
                i66d.write("//"+"\n")
            elif BlastN[ind] == "6A-I8" or BlastX[ind] == "6A-I8" or QueryCatX[ind] == "6A-I8" or QueryCatCX[ind] == "6A-I8" or QueryCatCQ[ind] == "6A-I8" or QueryCatQ[ind] == "6A-I8":
                i86b.write(qid+"\n")
                i86b.write(matrix_record[x])
                i86b.write(queryrecord[ind])
                i86b.write("//"+"\n")
            elif BlastN[ind] == "6B-I8" or BlastX[ind] == "6B-I8" or QueryCatX[ind] == "6B-I8" or QueryCatCX[ind] == "6B-I8" or QueryCatCQ[ind] == "6B-I8" or QueryCatQ[ind] == "6B-I8":
                i86c.write(qid+"\n")
                i86c.write(matrix_record[x])
                i86c.write(queryrecord[ind])
                i86c.write("//"+"\n")
            elif BlastN[ind] == "6C-I8" or BlastX[ind] == "6C-I8" or QueryCatX[ind] == "6C-I8" or QueryCatCX[ind] == "6C-I8" or QueryCatCQ[ind] == "6C-I8" or QueryCatQ[ind] == "6C-I8":
                i86d.write(qid+"\n")
                i86d.write(matrix_record[x])
                i86d.write(queryrecord[ind])
                i86d.write("//"+"\n")
            elif BlastN[ind] == "6A-D" or BlastX[ind] == "6A-D" or QueryCatX[ind] == "6A-D" or QueryCatCX[ind] == "6A-D" or QueryCatCQ[ind] == "6A-D" or QueryCatQ[ind] == "6A-D":
                D6b.write(qid+"\n")
                D6b.write(matrix_record[x])
                D6b.write(queryrecord[ind])
                D6b.write("//"+"\n")
            elif BlastN[ind] == "6B-D" or BlastX[ind] == "6B-D" or QueryCatX[ind] == "6B-D" or QueryCatCX[ind] == "6B-D" or QueryCatCQ[ind] == "6B-D" or QueryCatQ[ind] == "6B-D":
                D6c.write(qid+"\n")
                D6c.write(matrix_record[x])
                D6c.write(queryrecord[ind])
                D6c.write("//"+"\n")
            elif BlastN[ind] == "6C-D" or BlastX[ind] == "6C-D" or QueryCatX[ind] == "6C-D" or QueryCatCX[ind] == "6C-D" or QueryCatCQ[ind] == "6C-D" or QueryCatQ[ind] == "6C-D":
                D6d.write(qid+"\n")
                D6d.write(matrix_record[x])
                D6d.write(queryrecord[ind])
                D6d.write("//"+"\n")
            elif BlastN[ind] == "6A-E" or BlastX[ind] == "6A-E" or QueryCatX[ind] == "6A-E" or QueryCatCX[ind] == "6A-E" or QueryCatCQ[ind] == "6A-E" or QueryCatQ[ind] == "6A-E":
                E6b.write(qid+"\n")
                E6b.write(matrix_record[x])
                E6b.write(queryrecord[ind])
                E6b.write("//"+"\n")
            elif BlastN[ind] == "6B-E" or BlastX[ind] == "6B-E" or QueryCatX[ind] == "6B-E" or QueryCatCX[ind] == "6B-E" or QueryCatCQ[ind] == "6B-E" or QueryCatQ[ind] == "6B-E":
                E6c.write(qid+"\n")
                E6c.write(matrix_record[x])
                E6c.write(queryrecord[ind])
                E6c.write("//"+"\n")
            elif BlastN[ind] == "6C-E" or BlastX[ind] == "6C-E" or QueryCatX[ind] == "6C-E" or QueryCatCX[ind] == "6C-E" or QueryCatCQ[ind] == "6C-E" or QueryCatQ[ind] == "6C-E":
                E6d.write(qid+"\n")
                E6d.write(matrix_record[x])
                E6d.write(queryrecord[ind])
                E6d.write("//"+"\n")
            else:
                log.write(qid+'\n')
        else:
            log.write(qid + '\n')
