#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""

#16 files input
A1="/home/aung/combine_id/A1.id"
A2="/home/aung/combine_id/A2.id"
B3="/home/aung/combine_id/B3.id"
B4="/home/aung/combine_id/B4.id"
B5="/home/aung/combine_id/B5.id"
B6="/home/aung/combine_id/B6.id"
B7="/home/aung/combine_id/B7.id"
B8="/home/aung/combine_id/B8.id"
B9="/home/aung/combine_id/B9.id"
C10="/home/aung/combine_id/B10.id"
C11="/home/aung/combine_id/C11.id"
C12="/home/aung/combine_id/C12.id"
D13="/home/aung/combine_id/D13.id"
E14="/home/aung/combine_id/E14.id"
E15="/home/aung/combine_id/E15.id"
E16="/home/aung/combine_id/E16.id"
ATM03="/home/aung/combine_id/ATM03.fasta.id"

def file_list(fileinput):
    with open(fileinput,'rb') as f:
        tmp_list = []
        for line in f:
            tmp_list.append(line.strip('\n').strip())
    return tmp_list

A1_list = file_list(A1)
A2_list = file_list(A2)
B3_list = file_list(B3)
B4_list = file_list(B4)
B5_list = file_list(B5)
B6_list = file_list(B6)
B7_list = file_list(B7)
B8_list = file_list(B8)
B9_list = file_list(B9)
C10_list = file_list(C10)
C11_list = file_list(C11)
C12_list = file_list(C12)
D13_list = file_list(D13)
E14_list = file_list(E14)
E15_list = file_list(E15)
E16_list = file_list(E16)
ATM03_list = file_list(ATM03)

o = open("ATM03_nonShrimp.matrix", 'w')

for x in ATM03_list:
    tmp_str = ""
    col = "-"
    if (x in A1_list) and (x in A2_list) and (x in B3_list) and (x in B4_list) and (x in B5_list) and (x in B6_list) and (x in B7_list) and (x in B8_list) and (x in B9_list) and (x in C10_list) and (x in C11_list) and (x in C12_list) and (x in D13_list) and (x in E14_list) and (x in E15_list) and (x in E16_list):
        col = "y"
    elif (x in A1_list) or (x in A2_list) or (x in B3_list) or (x in B4_list) or (x in B5_list) or (x in B6_list) or (x in B7_list) or (x in B8_list) or (x in B9_list) or (x in C10_list) or (x in C11_list) or (x in C12_list) or (x in D13_list) or (x in E14_list) or (x in E15_list) or (x in E16_list):
        col = "n"
    else:
        col = "-"
        print x

    tmp_str = x+'\t'+col

    if (x in A1_list):
        tmp_str+= "\t"+"y"
    else:
        tmp_str += "\t"+"n"

    if (x in A2_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B3_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B4_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B5_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B6_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B7_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B8_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in B9_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in C10_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in C11_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in C12_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in D13_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in E14_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in E15_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"
    if (x in E16_list):
        tmp_str += "\t" + "y"
    else:
        tmp_str += "\t" + "n"

    o.write(tmp_str+'\n')
