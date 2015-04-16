#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

DE_file = sys.argv[1]  # DE
PW_DE = sys.argv[2]  # PWDE
Annotation = sys.argv[3]  # PWDE

open_DE = open(DE_file, 'r')
open_PW = open(PW_DE, 'r')
open_Annotation = open(Annotation, 'r')

DE_list = []
PW_ID = []
PW_Record = []
Annotation_ID = []
Annotation_Records = []

# data preparation
for line in open_DE:
    DE_list.append(line.strip())

# 2S
for line2 in open_PW:
    line_split = line2.split(',')
    PW_ID.append(line_split[2].strip())
    del line_split[2]
    line_split.insert(0, "2S")
    PW_Record.append(line_split)

# 3S
for line3 in open_Annotation:
    line3_split = line3.split('\t')
    Annotation_ID.append(line3_split[0].strip())
    del line3_split[0]
    line3_split.insert(0, "An")
    Annotation_Records.append(line3_split)

for DE3_record in DE_list:
    DE3_split = DE3_record.split(',')

    DE_ID = DE3_split[0].strip()
    DE3_split.insert(1, "3S")
    DE3_split.insert(2, "-")
    DE3_split.insert(3, "-")
    # 3S
    for x, record in enumerate(DE3_split):
        if x != len(DE3_split)-1:
            print record.strip() + '\t',
        else:
            print record.strip()

    Annotation_indices = [i for i, x in enumerate(Annotation_ID) if x == DE_ID]
    PW_indices = [i for i, x in enumerate(PW_ID) if x == DE_ID]

    # An
    for an_in in Annotation_indices:
        Annotation_Records[an_in].insert(0, DE_ID)
        for xc, cell in enumerate(Annotation_Records[an_in]):
            if xc != len(Annotation_Records[an_in])-1:
                print cell.strip()+'\t',
            else:
                print cell.strip()
    # 3S
    for pw_in in PW_indices:
        PW_Record[pw_in].insert(0, DE_ID)
        PW_Record[pw_in].insert(6, "-")
        for x2, cell2 in enumerate(PW_Record[pw_in]):
            if x2 != len(PW_Record[pw_in]) - 1:
                print cell2.strip() + '\t',
            else:
                print cell2.strip()