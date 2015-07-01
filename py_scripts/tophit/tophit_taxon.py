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
taxon = "/fs/home/card/LinWork/atm/blastnNT/NucSeq_blastn/task9_aung/aung_taxongroups/all_uniq"
divquery = sys.argv[1]
opentaxon = open(taxon, 'r')
opendivquery = open(divquery, 'r')

G1_list = codesnippets.file_read_line(G1)
G2_list = codesnippets.file_read_line(G2)
G3_list = codesnippets.file_read_line(G3)
G4_list = codesnippets.file_read_line(G4)
G5_list = codesnippets.file_read_line(G5)
G6_list = codesnippets.file_read_line(G6)
G7_list = codesnippets.file_read_line(G7)
G8_list = codesnippets.file_read_line(G8)

f1 = open(divquery+'_INV1', 'w')
f2 = open(divquery+'_INV2', 'w')
f3 = open(divquery+'_INV3', 'w')
f4 = open(divquery+'_INV4', 'w')
f5 = open(divquery+'_INV5', 'w')
f6 = open(divquery+'_INV6', 'w')
f7 = open(divquery+'_INV7', 'w')
f8 = open(divquery+'_INV8', 'w')

taxon_seqid = []
taxon_id = []
for line in opentaxon:
    line_split = line.split('\t')
    taxon_seqid.append(line_split[0].strip())
    taxon_id.append(line_split[1].strip())

for line2 in opendivquery:
    line2_split = line2.split('\t')
    div_seqid = line2_split[0].strip()
    sys.stdout.write(line2_split[0]+'\t'+line2_split[1]+'\t'+line2_split[2]+'\t'+line2_split[3]+'\t'+line2_split[4]+'\t')
    if div_seqid in taxon_seqid:
        ind = taxon_seqid.index(div_seqid)
        taxon_target = taxon_id[ind].strip().strip('\n')
        if taxon_target in G1_list:
            sys.stdout.write("A1"+'\n')
            f1.write(line2)
        elif taxon_target in G2_list:
            sys.stdout.write("A2" + '\n')
            f2.write(line2)
        elif taxon_target in G3_list:
            sys.stdout.write("A3" + '\n')
            f3.write(line2)
        elif taxon_target in G4_list:
            sys.stdout.write("A4" + '\n')
            f4.write(line2)
        elif taxon_target in G5_list:
            sys.stdout.write("A5" + '\n')
            f5.write(line2)
        elif taxon_target in G6_list:
            sys.stdout.write("A6" + '\n')
            f6.write(line2)
        elif taxon_target in G7_list:
            sys.stdout.write("A7" + '\n')
            f7.write(line2)
        elif taxon_target in G8_list:
            sys.stdout.write("A8" + '\n')
            f8.write(line2)
        else:
            sys.stdout.write(line2_split[5].strip()+'\n')