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
base = "/colossus/home/anuphap/taxon_divlist/20120225/"
G1 = base+"I1.missing.taxonid.sort.div.inv.6656.IDs.RV"
G2 = base+"I2.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RV"
G3 = base+"I3.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RV"
G4= base+"I4.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RV"
G5 = base+"I5.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RV"
G6 = base+"I6.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RV"
G7 = base+"I7.missing.taxonid.sort.div.inv.6656.IDs.RM.6231.IDs.RM.7711.IDs.RM.6447.IDs.RM.33511.IDs.RM.6157.IDs.RM.33317.IDs.RV"
CK = base+"C-K.missing.taxonid.sort.div.C.33090.IDs.RM.4751.IDs.RM.33630.IDs.RV"
CL = base+"C-L.missing.taxonid.sort.div.C.33090.IDs.RM.4751.IDs.RM.33630.IDs.RM"
CN = base+"C-N.missing.taxonid.sort.div.C.33090.IDs.RM.4751.IDs.RV"
CP = base+"C-P.missing.taxonid.sort.div.C.33090.IDs.RV"
I8k = base+"I8K.missing.taxonid.sort.div.inv.I8.33208.IDs.RM.33154.IDs.RM"
I8M = base+ "I8M.missing.taxonid.sort.div.inv.I8.33208.IDs.RV"
I8O = base+ "I8O.missing.taxonid.sort.div.inv.I8.33208.IDs.RM.33154.IDs.RV"

G1_list = codesnippets.file_read_line(G1)
G2_list = codesnippets.file_read_line(G2)
G3_list = codesnippets.file_read_line(G3)
G4_list = codesnippets.file_read_line(G4)
G5_list = codesnippets.file_read_line(G5)
G6_list = codesnippets.file_read_line(G6)
G7_list = codesnippets.file_read_line(G7)
CK_list = codesnippets.file_read_line(CK)
CL_list = codesnippets.file_read_line(CL)
CN_list = codesnippets.file_read_line(CN)
CP_list = codesnippets.file_read_line(CP)
I8K_list = codesnippets.file_read_line(I8k)
I8M_list = codesnippets.file_read_line(I8M)
I8O_list = codesnippets.file_read_line(I8O)

taxon_id = []
v1_line = []
division = []
div20 = []
f = open("newid.log",'w')
for line in openv1file:
    line_split = line.split('\t')
    taxon_id.append(line_split[1])
    division.append(line_split[4].strip('\n'))
    v1_line.append(line.strip('\n'))

for x,taxid in enumerate(taxon_id):
    record_split = v1_line[x].split('\t')
    sys.stdout.write(record_split[0])
    sys.stdout.write('\t')
    sys.stdout.write(record_split[1])
    sys.stdout.write('\t')
    sys.stdout.write(record_split[2])
    sys.stdout.write('\t')
    sys.stdout.write(record_split[3])
    sys.stdout.write('\t')
    sys.stdout.write(record_split[4])
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
    elif taxid in I8M_list:
        sys.stdout.write('M')
    elif taxid in CN_list:
        sys.stdout.write('N')
    elif taxid in I8O_list:
        sys.stdout.write('O')
    elif taxid in I8K_list:
        sys.stdout.write('K')
    elif taxid in CK_list:
        sys.stdout.write('K')
    elif taxid in CP_list:
        sys.stdout.write('P')
    elif taxid in CL_list:
        sys.stdout.write('L')
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
        f.write('-'+'\n')
        sys.stdout.write('-')
    sys.stdout.write('\n')
    