#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import codesnippets

v1file = sys.argv[1]
# v2file = sys.argv[2]
base = "/fs/home/card/taxon_divlist/taxdiv_info/"
G1 = base+"I1.update7_missing.id.div.Inv.6656.IDs.RV"
G2 = base+"I2.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RV"
G3 = base+"I3.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RV"
G4 = base+"I4.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RV"
G5 = base+"I5.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RV"
G6 = base+"I6.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RV"
G7 = base+"I7.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RV"
G8 = base+"I8.update7_missing.id.div.Inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RM"

G1_list = codesnippets.file_read_line(G1)
G2_list = codesnippets.file_read_line(G2)
G3_list = codesnippets.file_read_line(G3)
G4_list = codesnippets.file_read_line(G4)
G5_list = codesnippets.file_read_line(G5)
G6_list = codesnippets.file_read_line(G6)
G7_list = codesnippets.file_read_line(G7)
G8_list = codesnippets.file_read_line(G8)

openv1file = open(v1file, 'r')
# openv2file = open(v2file, 'r')

v1_id = []
v1_taxon = []
v1_division = []
# v2_id = []
v1_record = []
# v2_group = []

for line in openv1file:
    line_split = line.split('\t')
    v1_id.append(line_split[0].strip().strip('>'))
    v1_taxon.append(line_split[1].strip())
    v1_division.append(line_split[4].strip())
    v1_record.append(line.strip().strip('\n'))

# for line2 in openv2file:
#     line2_split = line2.split('\t')
#     v2_id.append(line2_split[0].strip().strip('>'))
#     v2_group.append(line2_split[1].strip().strip('\n'))

for x, v1id in enumerate(v1_id):
        sys.stdout.write(v1_record[x])
        sys.stdout.write('\t')
        if v1_division[x].lower() == "invertebrates":
            if v1_taxon[x] in G1_list:
                sys.stdout.write('I1')
            if v1_taxon[x] in G2_list:
                sys.stdout.write('I2')
            if v1_taxon[x] in G3_list:
                sys.stdout.write('I3')
            if v1_taxon[x] in G4_list:
                sys.stdout.write('I4')
            if v1_taxon[x] in G5_list:
                sys.stdout.write('I5')
            if v1_taxon[x] in G6_list:
                sys.stdout.write('I6')
            if v1_taxon[x] in G7_list:
                sys.stdout.write('I7')
            if v1_taxon[x] in G8_list:
                sys.stdout.write('I8')
        else:
            sys.stdout.write(v1_division[x])
        sys.stdout.write('\n')