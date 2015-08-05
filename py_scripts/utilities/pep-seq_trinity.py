#! /usr/bin/env/ python

"""
# get peptide sequence by trinityID
# usage: python pep-seq_trinity.py pep.fasta trinity_id1,trinity_id2
# output: peptide sequnce from stdout
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import linecache

pep_orf = sys.argv[1]  # peptide file
trinity = sys.argv[2]  # comma seperated trinityID
count = 0
target = []

for x in trinity.split(','):
    target.append(x.strip())
with open(pep_orf, 'rb') as f1:
    for line in f1:
        count += 1
        if ">" in line:
            line_split = line.split()
            tid = line_split[0].split('|')[0].strip('>')
            if tid in target:
                sys.stdout.write(line)
                sys.stdout.write(linecache.getline(sys.argv[1], count + 1))