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
base = "/fs/home/card/taxon_divlist/up520mis/"
G1 = base+"I1.upate5.missed20div.6656.IDs.RV"
G2 = base+"I2.upate5.missed20div.6656.IDs.RM.6231.IDs.RV"
G3 = base+"I3.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RV"
G4= base+"I4.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RV"
G5 = base+"I5.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RV"
G6 = base+"I6.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RV"
G7 = base+"I7.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RV"
G8 = base+"I8.upate5.missed20div.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RM"

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
record = []
f = open("newid.log",'w')
for line in openv1file:
    line_split = line.split('\t')
    taxon_id.append(line_split[0])
    division.append(line_split[4].strip('\n'))
    record.append(line.strip('\n'))

for x,taxid in enumerate(taxon_id):
    tmp = record[x].rstrip('\t-')+"\t"
    if taxid in G1_list:
        sys.stdout.write(tmp+'I1'+"\n")
    elif taxid in G2_list:
        sys.stdout.write(tmp+'I2'+"\n")
    elif taxid in G3_list:
        sys.stdout.write(tmp+'I3'+"\n")
    elif taxid in G4_list:
        sys.stdout.write(tmp+'I4'+"\n")
    elif taxid in G5_list:
        sys.stdout.write(tmp+'I5'+"\n")
    elif taxid in G6_list:
        sys.stdout.write(tmp+'I6'+"\n")
    elif taxid in G7_list:
        sys.stdout.write(tmp+'I7'+"\n")
    elif taxid in G8_list:
        sys.stdout.write(tmp+'I8'+"\n")
    # elif division[x].lower() == "mammals":
    #     sys.stdout.write(tmp+'Mammals'+"\n")
    # elif division[x].lower() == "primates":
    #     sys.stdout.write(tmp+'Primates'+"\n")
    # elif division[x].lower() == "rodents":
    #     sys.stdout.write(tmp+'Rodents'+"\n")
    # elif division[x].lower() == "vertebrates":
    #     sys.stdout.write(tmp+'Vertebrates'+"\n")
    # elif division[x].lower() == "plants":
    #     sys.stdout.write(tmp+'Plants'+"\n")
    # elif division[x].lower() == "bacteria":
    #     sys.stdout.write(tmp+'Bacteria'+"\n")
    # elif division[x].lower() == "viruses":
    #     sys.stdout.write(tmp+'Viruses'+"\n")
    # elif division[x].lower() == "phages":
    #     sys.stdout.write(tmp+'Phages'+"\n")
    # elif division[x].lower() == "\'environmental":
    #     sys.stdout.write(tmp+'\'Environmental'+"\n")
    # elif division[x].lower() == "synthetic":
    #     sys.stdout.write(tmp+'Synthetic'+"\n")
    # elif division[x].lower() == "noinfo":
    #     sys.stdout.write(tmp+'NOINFO'+"\n")
    # elif division[x].lower() == "unassigned":
    #     sys.stdout.write(tmp+'Unassigned'+"\n")
    else:
        # f.write('-' + '\n')
        sys.stdout.write(tmp+"\n")
