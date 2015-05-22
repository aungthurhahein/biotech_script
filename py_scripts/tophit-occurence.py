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
base = "/fs/home/card/LinWork/atm/blastnNT/NucSeq_blastn/task9_aung/AyInverGrps/"
G1 = base+"G1.Invertebrates.taxonList.6656.IDs.RV"
G2 = base+"G2.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RV"
G3 = base+"G3.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RV"
G4 = base+"G4.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RV"
G5 = base+"G5.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RV"
G6 = base+"G6.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RV"
G7 = base+"G7.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RV"
G8 = base+"G8.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RM"
mapfile = sys.argv[1]
idfile = sys.argv[2]
openmapfile = open(mapfile, 'r')
openidfile = open(idfile, 'r')

G1_list = codesnippets.file_read_line(G1)
G2_list = codesnippets.file_read_line(G2)
G3_list = codesnippets.file_read_line(G3)
G4_list = codesnippets.file_read_line(G4)
G5_list = codesnippets.file_read_line(G5)
G6_list = codesnippets.file_read_line(G6)
G7_list = codesnippets.file_read_line(G7)
G8_list = codesnippets.file_read_line(G8)

queryid = []
taxonid = []
division = []
for line in openmapfile:
    line_split = line.split('\t')
    queryid.append(line_split[0].strip())
    taxonid.append(line_split[2].strip())
    division.append(line_split[5].strip())

uniqid = []
for uniq_id in openidfile:
    uniqid.append(uniq_id.strip().strip('\n'))

for id in uniqid:
    indices = [i for i, x in enumerate(queryid) if x == id]
    sys.stdout.write(id)
    sys.stdout.write('\t')
    G1_count = 0
    G2_count = 0
    G3_count = 0
    G4_count = 0
    G5_count = 0
    G6_count = 0
    G7_count = 0
    G8_count = 0
    tmp = {}
    for x in indices:
        if division[x].lower() == "invertebrates":
            if taxonid[x] in G1_list:
                G1_count += 1
            if taxonid[x] in G2_list:
                G2_count += 1
            if taxonid[x] in G3_list:
                G3_count += 1
            if taxonid[x] in G4_list:
                G4_count += 1
            if taxonid[x] in G5_list:
                G5_count += 1
            if taxonid[x] in G6_list:
                G6_count += 1
            if taxonid[x] in G7_list:
                G7_count += 1
            if taxonid[x] in G8_list:
                G8_count += 1
        else:
            if tmp.has_key(division[x]) != 1:
                tmp[division[x]] = 1
            else:
                tmp[division[x]] += 1
    for key, value in tmp.iteritems():
        sys.stdout.write(key+"("+str(value)+")|")

    if G1_count > 0:
        sys.stdout.write('I1('+str(G1_count)+')|')
    if G2_count > 0:
        sys.stdout.write('I2(' + str(G2_count) + ')|')
    if G3_count > 0:
        sys.stdout.write('I3(' + str(G3_count) + ')|')
    if G4_count > 0:
        sys.stdout.write('I4(' + str(G4_count) + ')|')
    if G5_count > 0:
        sys.stdout.write('I5(' + str(G5_count) + ')|')
    if G6_count > 0:
        sys.stdout.write('I6(' + str(G6_count) + ')|')
    if G7_count > 0:
        sys.stdout.write('I7(' + str(G7_count) + ')|')
    if G8_count > 0:
        sys.stdout.write('I8(' + str(G8_count) + ')|')
    sys.stdout.write('\n')