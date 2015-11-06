#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

allidlist = sys.argv[1]

species_list = ["Callinectes_sapidus.fasta.hdr",
                "Carcinus_maenas.fasta.hdr",
                "Cherax_quadricarinatus_pchum.fasta.hdr",
                "Cherax_quadricarinatus.fasta.hdr",
                "Fenneropenaeus_chinensis.fasta.hdr",
                "Fenneropenaeus_indicus.fasta.hdr",
                "Homarus_americanus.fasta.hdr",
                "Litopenaeus_setiferus.fasta.hdr",
                "Macrobrachium_rosenbergii.fasta.hdr",
                "Marsupenaeus_japonicus.fasta.hdr",
                "Pacifastacus_leniusculus.fasta.hdr",
                "Scylla_olivacea.fasta.hdr",
                "Scylla_paramamosain.fasta.hdr",
                "Penaeus_monodon.fasta.hdr"
                ]

with open(allidlist, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        oldID = l1_split[0]+"|"+l1_split[1]+"|"+l1_split[2]
        newID = l1_split[0]
        if l1_split[3].strip('\n') in species_list:
            sys.stdout.write(oldID+'\t'+newID+'\n')
