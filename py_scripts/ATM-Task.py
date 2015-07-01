#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
rsem = sys.argv[1]
task11_file = sys.argv[2]
open_rsem = open(rsem, 'r')
open_task11 = open(task11_file, 'r')

rsem_astran = []
rsem_record = []

for line in open_rsem:
    line_split = line.split('\t')
    rsem_astran.append(line_split[0])
    rsem_record.append(line.strip('\n'))

for line in open_task11:
    line_split = line.split('\t')
    col_1 = line_split[0]
    #for record #G
    if col_1 == "#G":
        sys.stdout.write("//"+"\n")
        sys.stdout.write(">"+line_split[1].replace(" ", "_")+"\n")
        sys.stdout.write(line)
        tmp_astranid = []
        rm_record = []
        astr = line_split[3].split(';')
        for ast in astr:
            tmp_astranid.append(ast.strip())
        for rec in tmp_astranid:
            if rec in rsem_astran:
                ind = rsem_astran.index(rec)
                rm_record.append(rsem_record[ind])
            else:
                rm_record.append("No records in RSEM")
    else:
        col_3 = line_split[3]
        if col_3 in tmp_astranid:
            asind = tmp_astranid.index(col_3)
            sys.stdout.write("#RM"+"\t"+rm_record[asind]+"\n")
            del tmp_astranid[asind]
            del rm_record[asind]
            sys.stdout.write(line)
        else:
            sys.stdout.write(line)


