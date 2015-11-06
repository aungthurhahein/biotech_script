#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import re
import sys
allidlist = sys.argv[1]

estfile = open(allidlist+"_siest",'w')
e0102file = open(allidlist+"_e0102",'w')
contigfile = open(allidlist+"_contigv22",'w')
nuclfile = open(allidlist+"_nucleotide3",'w')
protfile = open(allidlist+"_proteinV22",'w')
countfile = open(allidlist+"_count",'w')

with open(allidlist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        mem = l1_split[2].split(';')
        est_id = ""
        contig_id = ""
        e0102_id = ""
        nucl_id = ""
        prot_id = ""
        memcount = str(len(mem))
        # print memcount,mem
        for m in mem:
            m = m.strip('\n')
            est = re.search(r'V3_SIEST01_\w+', m)
            contig = re.search(r'Pool_contigsV22_\w+', m)
            e0102 = re.search(r'Prot_PVPM_E0102_\w+', m)
            nucl = re.search(r'Pool_nucleotide3_\w+', m)
            prot = re.search(r'20150902Aung_\w+', m)

            if est:
                if est_id == "":
                    est_id = m
                else:
                    est_id += ";"+ m
            elif contig:
                if contig_id == "":
                    contig_id = m
                else:
                    contig_id += ";" + m
            elif e0102:
                if e0102_id == "":
                    e0102_id = m.split('_')[1]+"_"+m.split('_')[2]+"_"+m.split('_')[3]
                else:
                    e0102_id += ";" + m.split('_')[1]+"_"+m.split('_')[2]+"_"+m.split('_')[3]
            elif nucl:
                if nucl_id == "":
                    nucl_id = m
                else:
                    nucl_id += ";" + m
            elif prot:
                if prot_id == "":
                    prot_id = m
                else:
                    prot_id += ";" + m
        estlen = "0"
        contiglen = "0"
        e0102len = "0"
        nuclen = "0"
        protlen = "0"

        if est_id != "":
            estlen = str(len(est_id.split(';')))
            estfile.write(l1_split[0]+'\t'+l1_split[1]+'\t'+est_id+'\n')
        if contig_id != "":
            contiglen = str(len(contig_id.split(';')))
            contigfile.write(l1_split[0]+'\t'+l1_split[1]+'\t'+contig_id+'\n')
        if e0102_id != "":
            e0102len = str(len(e0102_id.split(';')))
            e0102file.write(l1_split[0]+'\t'+l1_split[1]+'\t'+e0102_id+'\n')
        if nucl_id != "":
            nuclen = str(len(nucl_id.split(';')))
            nuclfile.write(l1_split[0]+'\t'+l1_split[1]+'\t'+nucl_id+'\n')
        if prot_id != "":
            protlen = str(len(prot_id.split(';')))
            protfile.write(l1_split[0]+'\t'+l1_split[1]+'\t'+prot_id+'\n')

        countfile.write(l1_split[0]+'\t'+l1_split[1]+'\t'+memcount+'\t'+estlen+'\t'+contiglen+'\t'+e0102len+'\t'+nuclen+'\t'+protlen+'\n')