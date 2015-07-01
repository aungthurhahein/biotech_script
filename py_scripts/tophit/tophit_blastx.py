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
openv1file = open(v1file, 'r')
base = "/fs/home/card/LinWork/atm/blastnNT/NucSeq_blastn/task9_aung/AyInverGrps/"
G1 = base+"G1.Invertebrates.taxonList.6656.IDs.RV"
G2 = base+"G2.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RV"
G3 = base+"G3.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RV"
G4 = base+"G4.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RV"
G5 = base+"G5.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RV"
G6 = base+"G6.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RV"
G7 = base+"G7.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RV"
G8 = base+"G8.Invertebrates.taxonList.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RM"

G1_list = codesnippets.file_read_line(G1)
G2_list = codesnippets.file_read_line(G2)
G3_list = codesnippets.file_read_line(G3)
G4_list = codesnippets.file_read_line(G4)
G5_list = codesnippets.file_read_line(G5)
G6_list = codesnippets.file_read_line(G6)
G7_list = codesnippets.file_read_line(G7)
G8_list = codesnippets.file_read_line(G8)

taxon_id = []
division = []
for line in openv1file:
    line_split = line.split('\t')
    taxon_id.append(line_split[0])
    division.append(line_split[1].strip())
for x, taxid in enumerate(taxon_id):
    sys.stdout.write(taxid)
    sys.stdout.write('\t')
    sys.stdout.write(division[x])
    sys.stdout.write('\t')

    if taxid in G1_list:
        sys.stdout.write('I1')
    elif taxid in G2_list:
        sys.stdout.write('I2')
    elif taxid in G3_list:
        sys.stdout.write('I3')
    elif taxid in G4_list:
        sys.stdout.write('I4')
    elif taxid in G5_list:
        sys.stdout.write('I5')
    elif taxid in G6_list:
        sys.stdout.write('I6')
    elif taxid in G7_list:
        sys.stdout.write('I7')
    elif taxid in G8_list:
        sys.stdout.write('I8')
    elif division[x].lower() == "mammals":
        sys.stdout.write('Mammals')
    elif division[x].lower() == "primates":
        sys.stdout.write('Primates')
    elif division[x].lower() == "rodents":
        sys.stdout.write('Rodents')
    elif division[x].lower() == "vertebrates":
        sys.stdout.write('Vertebrates')
    elif division[x].lower() == "plants":
        sys.stdout.write('Plants')
    elif division[x].lower() == "bacteria":
        sys.stdout.write('Bacteria')
    elif division[x].lower() == "viruses":
        sys.stdout.write('Viruses')
    elif division[x].lower() == "phages":
        sys.stdout.write('Phages')
    elif division[x].lower() == "\'environmental":
        sys.stdout.write('\'Environmental')
    elif division[x].lower() == "synthetic":
        sys.stdout.write('Synthetic')
    elif division[x].lower() == "noinfo":
        sys.stdout.write('NOINFO')
    elif division[x].lower() == "unassigned":
        sys.stdout.write('Unassigned')
    else:
        sys.stdout.write('-')
    sys.stdout.write('\n')