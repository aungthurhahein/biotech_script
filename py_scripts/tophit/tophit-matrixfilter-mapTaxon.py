#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

blastn = sys.argv[1]
blastx = sys.argv[2]
ifile = sys.argv[3]

n_cat = []
n_id = []
n_species = []
n_gi = []
n_taxon = []
n_div = []
with open(blastn,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        n_cat.append(line_split[0])
        n_id.append(line_split[1])
        n_species.append(line_split[6].strip('\n'))
        n_gi.append(line_split[2])
        n_taxon.append(line_split[3])
        n_div.append(line_split[5])

x_cat = []
x_id = []
x_species = []
x_gi = []
x_taxon = []
x_div = []
with open(blastx,'r') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        x_cat.append(line2_split[0])
        x_id.append(line2_split[1])
        x_species.append(line2_split[6].strip('\n'))
        x_gi.append(line2_split[2])
        x_taxon.append(line2_split[3])
        x_div.append(line2_split[5])

idfile = []
cat = []
NX = []
div = []
with open(ifile,'r') as f3:
    for line3 in f3:
        line3_split = line3.split('\t')
        idfile.append(line3_split[0].strip('>'))
        cat.append(line3_split[1].split('(')[0].strip('\n'))
        div.append(line3_split[1].split('-')[1].split('(')[0].strip('\n'))
        NX.append(line3_split[1].split('(')[1].strip(")").strip('\n'))

for x,tid in enumerate(idfile):
    group = cat[x].split('-')[0]
    tmp_group = ""
    if NX[x] == "N)":
        n_indexes = [i for i, e in enumerate(n_id) if e == tid]
        for nind in n_indexes:
            if n_cat[nind] == "#XC1":
                tmp_group = "6B"
            elif n_cat[nind] == "#XC2":
                tmp_group = "6C"
            elif n_cat[nind] == "#XCal":
                tmp_group = "6A"
            if tmp_group == group:
                if n_div[nind] == "Viruses" or n_div[nind] == "Phages":
                    tmpdiv = "E"
                elif n_div[nind] == "Bacteria":
                    tmpdiv = "D"
                else:
                    tmpdiv = n_div[nind]

                if div[x] == tmpdiv:
                    sys.stdout.write(idfile[x]+"\t"+cat[x]+"\t"+NX[x].split(')')[0]+"\t"+n_gi[nind]+"\t"+n_taxon[nind]+"\t"+n_species[nind]+"\n")
            # else:
            #     print idfile[x]
            #     print tmp_group, group
            #     print n_cat[nind], div[x], tmpdiv
    elif NX[x] == "X)":
        x_indexes = [i for i, e in enumerate(x_id) if e == tid]
        for xind in x_indexes:
            if x_cat[xind] == "#XC1":
                tmp_group = "6B"
            elif x_cat[xind] == "#XC2":
                tmp_group = "6C"
            elif x_cat[xind] == "#XCal":
                tmp_group = "6A"
            if tmp_group == group:
                if x_div[xind] == "Viruses" or x_div[xind] == "Phages":
                    tmpdiv = "E"
                elif x_div[xind] == "Bacteria":
                    tmpdiv = "D"
                else:
                    tmpdiv = x_div[xind]
                if div[x] == tmpdiv:
                    sys.stdout.write(idfile[x] + "\t" + cat[x] + "\t" + NX[x].split(')')[0] + "\t" + x_gi[xind] + "\t" + x_taxon[xind] + "\t" + x_species[xind] + "\n")
            # else:
            #     print idfile[x]
            #     print tmp_group, group
            #     print x_cat[xind], div[x], tmpdiv