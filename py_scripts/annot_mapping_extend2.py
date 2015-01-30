#! /usr/bin/env python
#--------------------------------------------------------------------------#
# add more information from another report with mapping annotation file
# __author__ = 'atrx'
# usage: annot_mapping_extend.py annot_report c01_annotation.tsv
# Date: 26012015
#--------------------------------------------------------------------------#
import sys
import linecache
import re
import csv

usage= "Usage %s infile" % sys.argv[0] #specific massage for no input

try:
    annotationfile = sys.argv[1]
    tsvfile = sys.argv[2]
except:
    print usage, sys.exit(1)

def file_to_list(filename):
    listname=[]
    for line in filename:
        listname.append(line)
    return listname

def check_in_list(listname,item):
    if item in listname:
        return "true"
    else:
        return "false"

annotlist=[]; tsvlist=[];final_list=[]
annot = open(annotationfile,'r')
tsv = open(tsvfile,'r')
annotlist = file_to_list(annot)
tsvlist = file_to_list(tsv)
print "ID\tC\tM\tS\tCM\tCS\tMC\tMS\tSC\tSM\tC\tM\tS\tMS\tgene-id\tTranscript-id\tBLASTX-FLAG\tsprot-Top-BLASTX-hit\tTrEMBL-Top-BLASTX-hit\tRNAMMER\tprot-id\tprot-coords\tBLASTP-FLAG\tsprot-Top-BLASTP-hit\tTrEMBL-Top-BLASTP-hit\tPfam\tSignalP\tTmHMM\teggnog\tgene-ontology-blast\tgene-ontology-pfam\ttranscript\tpeptide"
for annot_line in annotlist:
    annot_split= annot_line.split('\t')
    annot_id= annot_split[1].strip()
    for tsv_line in tsvlist:
        tsv_split = tsv_line.split('\t')
        tsv_id = tsv_split[0].strip()
        if tsv_id == annot_id:
            for i in range(1,len(tsv_split)):
                if tsv_split[i] == '.':
                    print tsv_split[i], annot_split[i-14]
                    tsv_split[i] = annot_split[i-14]
                    flag =check_in_list(final_list,tsv_split)
                    if flag == "false":
                        if annot_split[3] != ".":
                            tsv_split[16] = "E-03"
                        if annot_split[8] != ".":
                            tsv_split[22] = "E-03"
                        final_list.append(tsv_split)
        else:
            flag =check_in_list(final_list,tsv_split)
            if flag == "false":
                final_list.append(tsv_split)
#
# for x in final_list:
#     for k in x:
#         print k,
#         print "\t",


