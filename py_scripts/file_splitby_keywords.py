__author__ = 'aung'

import sys
import re

targetfile = sys.argv[1]
fileopen = open(targetfile, 'r')
file_list = []

microsatellite_file = open(targetfile+"_microsatellite", 'w')
mitochondrial_file = open(targetfile+"_mitochondrial", 'w')
ribosomal_file = open(targetfile + "_ribosomal", 'w')
AFLP_file = open(targetfile + "_AFLP", 'w')
miRNA_file = open(targetfile + "_miRNA", 'w')
cytochrome_file = open(targetfile + "_cytochrome", 'w')
lectin_file = open(targetfile + "_lectin", 'w')
caspase_file = open(targetfile + "_caspase", 'w')
heat_file = open(targetfile + "_heat", 'w')
actin_file = open(targetfile + "_actin", 'w')
tubulin_file = open(targetfile + "_tubulin", 'w')
myosin_file = open(targetfile + "_myosin", 'w')
hemocyanin_file = open(targetfile + "_hemocyanin", 'w')
histone_file = open(targetfile + "_histone", 'w')
internal_file = open(targetfile + "_internalTranscribedSpacer", 'w')
SRAP_file = open(targetfile + "_SrapMaker", 'w')
Penelope_file = open(targetfile + "_penelope", 'w')

other_file = open(targetfile+"_Other", 'w')
new_file = open(targetfile+"_keyword_col", 'w')

for line in fileopen:
    file_list.append(line)

def update_record(record,keyword):
    rec = record.strip()
    rec += "\t" + keyword + "\n"
    new_file.write(rec)

for record in file_list:
    record_split = record.split('\t')
    definition = record_split[3].strip()

    # condition
    microsatellite_id = re.search(r'[\w+\s+]*satellite[\w+\s+]*', definition)
    mitochondrial_id = re.search(r'[\w+\s+]*mitochond[\w+\s+]*', definition)
    ribosomal_id = re.search(r'[\w+\s+]*ribosomal[\w+\s+]*', definition)
    AFLP_id = re.search(r'[\w+\s+]*AFLP[\w+\s+]*', definition)
    miRNA_id = re.search(r'[\w+\s+]*miRNA[\w+\s+]*', definition)
    cytochrome_id = re.search(r'[\w+\s+]*cytochrome[\w+\s+]*', definition)
    lectin_id = re.search(r'[\w+\s+]*lectin[\w+\s+]*', definition)
    caspase_id = re.search(r'[\w+\s+]*caspase[\w+\s+]*', definition)
    heat_id = re.search(r'[\w+\s+]*heat shock[\w+\s+]*', definition)
    actin_id = re.search(r'[\w+\s+]*actin[\w+\s+]*', definition)
    tubulin_id = re.search(r'[\w+\s+]*tubulin[\w+\s+]*', definition)
    myosin_id = re.search(r'[\w+\s+]*myosin[\w+\s+]*', definition)
    hemocyanin_id = re.search(r'[\w+\s+]*hemocyanin[\w+\s+]*', definition)
    histone_id = re.search(r'[\w+\s+]*histone[\w+\s+]*', definition)
    internal_id = re.search(r'[\w+\s+]*internal transcribed spacer[\w+\s+]*', definition)
    SRAP_id = re.search(r'[\w+\s+]*SRAP marker[\w+\s+]*', definition)
    Penelope_id = re.search(r'[\w+\s+]*Penelope[\w+\s+]*', definition)

    if microsatellite_id:
        microsatellite_file.write(record)
        update_record(record,"microsatellite")
    elif mitochondrial_id:
        mitochondrial_file.write(record)
        update_record(record, "mitochondrial")
    elif ribosomal_id:
        ribosomal_file.write(record)
        update_record(record, "ribosomal")
    elif AFLP_id:
        AFLP_file.write(record)
        update_record(record, "AFLP")
    elif miRNA_id:
        miRNA_file.write(record)
        update_record(record, "miRNA")
    elif cytochrome_id:
        cytochrome_file.write(record)
        update_record(record, "cytochrome")
    elif lectin_id:
        lectin_file.write(record)
        update_record(record, "lectin")
    elif caspase_id:
        caspase_file.write(record)
        update_record(record, "caspase")
    elif heat_id:
        heat_file.write(record)
        update_record(record, "heat shock")
    elif actin_id:
        actin_file.write(record)
        update_record(record, "actin")
    elif tubulin_id:
        tubulin_file.write(record)
        update_record(record, "tubulin")
    elif myosin_id:
        myosin_file.write(record)
        update_record(record, "myosin")
    elif hemocyanin_id:
        hemocyanin_file.write(record)
        update_record(record, "hemocyanin")
    elif histone_id:
        histone_file.write(record)
        update_record(record, "histone")
    elif internal_id:
        internal_file.write(record)
        update_record(record,"internal transcribed spacer")
    elif SRAP_id:
        SRAP_file.write(record)
        update_record(record,"SRAP marker")
    elif Penelope_id:
        Penelope_file.write(record)
        update_record(record,"Penelope")
    else:
        other_file.write(record)
        update_record(record, "unknown")
