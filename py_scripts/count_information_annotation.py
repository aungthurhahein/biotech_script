#! /usr/bin/env python
"""
# --------------------------------------------------------------------------#
# count information
# Date: 9012015
# Usage: annotataion_map.py
# __author__ = 'Aung'
#--------------------------------------------------------------------------#
"""
import sys
import linecache

file1 = "/home/aung/server_downloads/c01_MIRA_DE/T1_DE.txt"
file2 = "/home/aung/server_downloads/c01_MIRA_DE/c01MIRA_AnnotationTransfer.tsv"
file3 = "/home/aung/server_downloads/c01_MIRA_CDHIT/mira_org_trinity.txt"
file_read = open(file1, 'r')
file2_read = open(file2, 'r')
file3_read = open(file3, 'r')
# result_clst=[];result_id=[];result_count=[];
DE_file = [];
Annotation_file = [];
mira_org = [];
mira_trinity = [];

for i in file_read:
    DE_file.append(i)
for j in file2_read:
    Annotation_file.append(j)
for k in file3_read:
    k_split = k.split('\t')
    trinity_tempid = k_split[1].split()
    mira_org.append(k_split[0].strip())
    mira_trinity.append(trinity_tempid[0].strip('>'))

for de_line in DE_file:
    de_split = de_line.split('\t')
    de_trans = de_split[0].strip()
    if de_trans in mira_trinity:
        tempindex = mira_trinity.index(de_trans)
        mira_org_id = mira_org[tempindex].strip()
    else:
        mira_org_id = "null"
    # print mira_org_id
    for annot_line in Annotation_file:
        annot_split = annot_line.split('\t')
        annot_trans = annot_split[0].strip('>')
        # print mira_org_id.strip('>'),annot_trans.strip()
        if mira_org_id.strip('>') == annot_trans.strip():
            print de_line.strip('\n'), '\t', annot_line

