#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]
countmatrix = sys.argv[2]
exprmatrix = sys.argv[3]
crossform = sys.argv[4]

countid = []
count_res = []
with open(countmatrix, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        countid.append(l2_split[0])
        count_res.append(l2)

exprid = []
expr_res = []
with open(exprmatrix, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        exprid.append(l3_split[0])
        expr_res.append(l3)


crossformid = []
crossform_res = []
with open(crossform, 'rb') as f4:
    for l4 in f4:
        l4_split = l4.split('\t')
        crossformid.append(l4_split[0])
        crossform_res.append(l4)

with open(mapfile, 'rb') as f1:
    for l1 in f1:
        tmp = ""
        l1_split = l1.split('\t')
        orgid = l1_split[1]
        astranid = l1_split[2].strip('\n')        
        tmp = orgid+"\t"+astranid

        if orgid in countid:
            ind = countid.index(orgid)
            tmp += "\t"+count_res[ind].strip('\n')
        if orgid in exprid:
            ind = exprid.index(orgid)
            tmp += "\t"+expr_res[ind].strip('\n')
        if orgid in crossformid:
            ind = crossformid.index(orgid)
            tmp += "\t"+crossform_res[ind].strip('\n')
        col9 = float(count_res[ind].strip('\n').split("\t")[1]) - float(count_res[ind].strip('\n').split("\t")[2])
        col10 = float(expr_res[ind].strip('\n').split("\t")[1]) - float(expr_res[ind].strip('\n').split("\t")[2])
        col11 = float(crossform_res[ind].strip('\n').split("\t")[1]) - float(crossform_res[ind].strip('\n').split("\t")[2])
        if float(count_res[ind].strip('\n').split("\t")[1]) > 0 and float(count_res[ind].strip('\n').split("\t")[2]) == 0:
            col12= "y"
        else:
            col12= "n"

        sys.stdout.write(tmp+"\t"+str(col9)+"\t"+str(col10)+"\t"+str(col11)+"\t"+col12+"\n")
