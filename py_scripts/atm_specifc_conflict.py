#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
Hid = sys.argv[1]
nonshrimp = sys.argv[2]
open_H = open(Hid, 'r')
open_Non = open(nonshrimp, 'r')

H_id = []
Non_id = []
for line in open_H:
    H_id.append(line.strip())

for lines in open_Non:
    Non_id.append(lines.strip())
f = open("hremove.txt", 'w')

for nonind in Non_id:
    if nonind not in H_id:
        print nonind
    else:
        f.write(nonind+'\n')

# H_specifc = sys.argv[1]
# A_specifc = sys.argv[2]
# open_H = open(H_specifc, 'r')
# open_A = open(A_specifc, 'r')
# H_id = []
# A_id = []
# onlyin_h = []
# common = []
#
#
# def print_list(list_obj,str_obj):
#     f = open(str(str_obj), 'w')
#     for x in list_obj:
#         f.write(x+'\n')
#
# for line in open_H:
#     H_id.append(line.strip())
#
# for lines in open_A:
#     A_id.append(lines.strip())
#
# for hid in H_id:
#     print hid
#     if hid in A_id:
#         common.append(hid)
#         A_id.remove(hid)
#     else:
#         onlyin_h.append(hid)
#
# print_list(A_id, "aonly")
# print_list(onlyin_h,"honly")
# print_list(common,"common")
