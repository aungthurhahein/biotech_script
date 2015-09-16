#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

taxon_div_list = sys.argv[1]
taxon_gi_list = sys.argv[2]
tophit_list = sys.argv[3]

taxonid = []
giid = []
with open(taxon_gi_list, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        taxonid.append(l1_split[1].strip('\n'))
        giid.append(l1_split[0])

div_taxon = []
div_species = []
div = []
div20 = []
with open(taxon_div_list, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        div_taxon.append(l2_split[0])
        div_species.append(l2_split[2].strip('\n'))
        div.append(l2_split[4])
        div20.append(l2_split[5])


with open(tophit_list, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        tmp = "XCal"+"\t"+l3_split[0]+"\t"+l3_split[4]

        if l3_split[4] in giid:
            ind = giid.index(l3_split[4])
            tax = taxonid[ind]
            if tax in div_taxon:
                ind2 = div_taxon.index(tax)
                tmp += '\t'+ div_taxon[ind2]+'\t'+div[ind2]+'\t'+div20[ind2].strip('\n')+'\t'+div_species[ind2]+'\n'
            sys.stdout.write(tmp)
