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

iblastn = open("g4_blastN", 'w')
iblastx = open("g4_blastX", 'w')
iblastcatx = open("g4_blastcatX", 'w')
iblastcatcx = open("g4_blastCX", 'w')
iblastcatcq = open("g4_blastCQ", 'w')
iblastcatq = open("g4_blastQ", 'w')
log = open("else.log",'w')

for x, qid in enumerate(matrixqueryid):
    if atm80[x] == "y" and nonshrimp80[x] == "y":
        if qid in QueryID:
            ind = QueryID.index(qid)
            blastn_split = BlastN[ind].split('-')[1].split('(')[0]
            blastx_split = BlastX[ind].split('-')[1].split('(')[0]
            QueryCatX_split = QueryCatX[ind].split('-')[1].split('(')[0]
            QueryCatCX_split = QueryCatCX[ind].split('-')[1].split('(')[0]
            QueryCatCQ_split = QueryCatCQ[ind].split('-')[1].split('(')[0]
            QueryCatQ_split = QueryCatQ[ind].split('-')[1].strip('\n').split('(')[0]
            if blastn_split == "I6" or blastn_split == "I8" or blastn_split == "D" or blastn_split == "E":
                iblastn.write(qid+"\t"+BlastN[ind]+'\n')
            if blastx_split == "I6" or blastx_split == "I8" or blastx_split == "D" or blastx_split == "E":
                iblastx.write(qid+"\t"+BlastX[ind]+'\n')
            if QueryCatX_split == "I6" or QueryCatX_split == "I8" or QueryCatX_split == "D" or QueryCatX_split == "E":
                iblastcatx.write(qid+"\t"+QueryCatX[ind]+'\n')
            if QueryCatCX_split == "I6" or QueryCatCX_split == "I8" or QueryCatCX_split == "D" or QueryCatCX_split == "E":
                iblastcatcx.write(qid+"\t"+QueryCatCX[ind]+'\n')
            if QueryCatCQ_split == "I6" or QueryCatCQ_split == "I8" or QueryCatCQ_split == "D" or QueryCatCQ_split == "E":
                iblastcatcq.write(qid+"\t"+QueryCatCQ[ind]+'\n')
            if QueryCatQ_split == "I6" or QueryCatQ_split == "I8" or QueryCatQ_split == "D" or QueryCatQ_split == "E":
                iblastcatq.write(qid+"\t"+QueryCatQ[ind]+'\n')




