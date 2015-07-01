#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
sourcecount = sys.argv[1]
matix = sys.argv[2]
blast_n = {}
blast_x = {}
cat_x = {}
cat_cx ={}
cat_cq = {}
cat_q = {}

matrixqueryid = []
atm80 = []
nonshrimp80 = []
matrix_record = []

def printstuff(dic_obj):
    keylist = dic_obj.keys()
    keylist.sort()
    for k in keylist:
        print k,'\t',dic_obj[k]

with open(matix,'rb') as openmatrix:
    for line in openmatrix:
        line_split = line.split('\t')
        matrixqueryid.append(line_split[0])
        atm80.append(line_split[6])
        nonshrimp80.append(line_split[11])
        matrix_record.append(line)

with open(sourcecount,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        qid = line_split[0]
        blastn = line_split[1]
        blastx = line_split[2]
        catx = line_split[3]
        catcx = line_split[4]
        catcq = line_split[5]
        catq = line_split[6]
        tmpind = -1
        if qid in matrixqueryid:
            tmpind = matrixqueryid.index(qid)
            print tmpind
        if atm80[tmpind] == 'y' and nonshrimp80[tmpind] == 'y':
            if blastn in blast_n:
                blast_n[blastn] += 1
            else:
                blast_n[blastn] = 1

            if blastx in blast_x:
                blast_x[blastx] += 1
            else:
                blast_x[blastx] = 1

            if catx in cat_x:
                cat_x[catx] += 1
            else:
                cat_x[catx] = 1

            if catcx in cat_cx:
                cat_cx[catcx] += 1
            else:
                cat_cx[catcx] = 1

            if catcq in cat_cq:
                cat_cq[catcq] += 1
            else:
                cat_cq[catcq] = 1

            if catq.strip('\n') in cat_q:
                cat_q[catq.strip('\n')] += 1
            else:
                cat_q[catq.strip('\n')] = 1

print "N"
printstuff(blast_n)
print "X"
printstuff(blast_x)
print "CATX"
printstuff(cat_x)
print "CATCX"
printstuff(cat_cx)
print "CATCQ"
printstuff(cat_cq)
print "CATQ"
printstuff(cat_q)