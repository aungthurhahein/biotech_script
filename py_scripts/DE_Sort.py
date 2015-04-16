#! /usr/bin/env/ python

"""
# sort annotation file by expression values
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

DE_file = sys.argv[1]
open_DE = open(DE_file,'r')
DE_list = []
sort_list = []
for line in open_DE:
    DE_list.append(line.strip())

del DE_list[0]

def print_pop(int_obj):
    delete_indx = []
    for indx, de_records in enumerate(DE_list):
        record_split = de_records.split(',')
        if record_split[int_obj].strip() == "1":
            sort_list.append(de_records)
            delete_indx.append(indx)
    for x in reversed(delete_indx):
        del DE_list[x]


print_pop(12)  # S
print_pop(13)  # MS
print_pop(6)   # MC
print_pop(8)   # SC
print_pop(9)   # SM
print_pop(7)   # MS
print_pop(5)  # CS
print_pop(4)  # CM
# The rest
for de_records in DE_list:
    sort_list.append(de_records)

# printing out
for x in sort_list:
    print x
