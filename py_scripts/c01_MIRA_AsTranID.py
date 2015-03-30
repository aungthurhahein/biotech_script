#! /usr/bin/env/ python
"""
# For c01_MIRA,it needs to generate AsTranID specially
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 25032015
"""
import sys
import argparse
from Bio import SeqIO

id_mapped_file = sys.argv[1]
id_mapped_2file = sys.argv[1]

open_id1_file = open(id_mapped_file, 'r')
open_id2_file = open(id_mapped_2file, 'r')
result_file = open(open_id1_file+"_result", 'w')
id2_trid = []
id2_miraid = []
id2_miracusomid = []
for line in open_id2_file:
    line_split = line.split('\t')
    id2_trid.append(line_split[0].strip())
    id2_miraid.append(line_split[1].strip())
    id2_miracusomid.append(line_split[2].strip())

for line in open_id1_file:
    id1_split = line.split('\t')
    if id1_split[1].strip() in id2_miracusomid:
        tmp_indx = id2_miracusomid.index()
        print id1_split[0].strip()+ '\t' + id2_trid[tmp_indx] + '\t' + id2_miraid[tmp_indx]+'\t' + id1_split[1].strip() + id1_split[2].strip() + '\t' + id1_split[3].strip() + '\n'
    # mira_id = mira_customid+ str(count).zfill(4)
    # clstr_trinity = line_split[0] + "\t" + line_split[1].strip() + "\t" + mira_id+ "\n"
    # new_custom_id = "{0}_{1}".format(AsTranID, str(count).zfill(5))
    # clstr_trinity = line_split[0] + "\t" + line_split[1].strip() + "\t" + new_custom_id + "\t" + AssemblyID + "\n"
    # count += 1
    # result_file.write(clstr_trinity)
