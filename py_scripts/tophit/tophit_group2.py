#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import re

infile = sys.argv[1]
open_infile = open(infile, 'r')

f = open(infile+"_v2Cat", 'w')
def check_cat(str_obj):
    # Invert
    group_I1 = re.search(r'[\w+\s+]*i1[\w+\s+]*', str_obj.lower())
    group_I2 = re.search(r'[\w+\s+]*i2[\w+\s+]*', str_obj.lower())
    group_I4 = re.search(r'[\w+\s+]*i4[\w+\s+]*', str_obj.lower())
    group_I7 = re.search(r'[\w+\s+]*i7[\w+\s+]*', str_obj.lower())
    group_I6 = re.search(r'[\w+\s+]*i6[\w+\s+]*', str_obj.lower())

    # U
    group_I5 = re.search(r'[\w+\s+]*i5[\w+\s+]*', str_obj.lower())
    group_I3 = re.search(r'[\w+\s+]*i3[\w+\s+]*', str_obj.lower())
    Mammals = re.search(r'[\w+\s+]*mammals[\w+\s+]*', str_obj.lower())
    Primates = re.search(r'[\w+\s+]*primates[\w+\s+]*', str_obj.lower())
    Rodents = re.search(r'[\w+\s+]*rodents[\w+\s+]*', str_obj.lower())
    Vertebrates = re.search(r'[\w+\s+]*vertebrates[\w+\s+]*', str_obj.lower())

    group_I8 = re.search(r'[\w+\s+]*i8[\w+\s+]*', str_obj.lower())

    # C
    Plants = re.search(r'[\w+\s+]*plants[\w+\s+]*', str_obj.lower())

    # D
    Bacteria = re.search(r'[\w+\s+]*bacteria[\w+\s+]*', str_obj.lower())

    # E
    Viruses = re.search(r'[\w+\s+]*viruses[\w+\s+]*', str_obj.lower())
    Phages = re.search(r'[\w+\s+]*phages[\w+\s+]*', str_obj.lower())

    #F
    Environmental = re.search(r'[\w+\s+]*environmental[\w+\s+]*', str_obj.lower())
    Synthetic = re.search(r'[\w+\s+]*synthetic[\w+\s+]*', str_obj.lower())

    #G
    Noinfo = re.search(r'[\w+\s+]*noinfo[\w+\s+]*', str_obj.lower())
    unassign = re.search(r'[\w+\s+]*unassigned[\w+\s+]*', str_obj.lower())

    if group_I1:
        return "I1"
    elif group_I2:
        return "I2"
    elif group_I4:
        return "I4"
    elif group_I7:
        return "I7"
    elif group_I6:
        return "I6"
    elif Mammals or Primates or Rodents or Vertebrates or group_I5 or group_I3:
        return "U"
    elif group_I8:
        return "I8"
    elif Plants:
        return "C"
    elif Bacteria:
        return "D"
    elif Viruses or Phages:
        return "E"
    elif Environmental or Synthetic:
        return "F"
    elif Noinfo or unassign:
        return "G"
    else:
        return "NaN"

for line in open_infile:
    line_split = line.split('\t')
    cal = line_split[5].strip()
    res = check_cat(str(cal))
    tmp = line.strip('\n') + '\t' + res + '\n'
    f.write(tmp)