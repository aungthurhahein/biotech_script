__author__ = 'Aung'
import sys
import re

# enumerate file into list
def file_read(file_handle):
    temp_list=[]
    for line in file_handle:
        temp_list.append(line)
    return temp_list

clstrfile = "/home/aung/server_downloads/allpool/by_division/inv_division/inv_div_#5.clstr.parse2"
clstr_open = open(clstrfile,'r')
clstr_list = file_read(clstr_open)

targetfile = "/home/aung/server_downloads/allpool/by_division/inv_division/inv_div.txt_uniqueseqID.txt"
fileopen = open(targetfile, 'r')
file_list = file_read(fileopen)

microsatellite_file = []
mitochondrial_file = []
ribosomal_file = []
AFLP_file = []
miRNA_file = []
cytochrome_file = []
lectin_file = []
caspase_file = []
heat_file = []
actin_file = []
tubulin_file = []
myosin_file = []
hemocyanin_file = []
histone_file = []
internal_file = []
SRAP_file = []
Penelope_file = []
other_file=[]

for record in file_list:
    record_split = record.split('\t')
    definition = record_split[3].strip()
    seqid = record_split[0].strip()
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
        microsatellite_file.append(seqid)
    elif mitochondrial_id:
        mitochondrial_file.append(seqid)
    elif ribosomal_id:
        ribosomal_file.append(seqid)
    elif AFLP_id:
        AFLP_file.append(seqid)
    elif miRNA_id:
        miRNA_file.append(seqid)
    elif cytochrome_id:
        cytochrome_file.append(seqid)
    elif lectin_id:
        lectin_file.append(seqid)
    elif caspase_id:
        caspase_file.append(seqid)
    elif heat_id:
        heat_file.append(seqid)
    elif actin_id:
        actin_file.append(seqid)
    elif tubulin_id:
        tubulin_file.append(seqid)
    elif myosin_id:
        myosin_file.append(seqid)
    elif hemocyanin_id:
        hemocyanin_file.append(seqid)
    elif histone_id:
        histone_file.append(seqid)
    elif internal_id:
        internal_file.append(seqid)
    elif SRAP_id:
        SRAP_file.append(seqid)
    elif Penelope_id:
        Penelope_file.append(seqid)
    else:
        other_file.append(seqid)

for x in clstr_list:
    clst_split = x.strip().split('\t')
    result = clst_split[0]
    for member in clst_split[1:]:
        member_split = member.strip().split('-')
        seq_memberid = member_split[1].strip()
        if seq_memberid in microsatellite_file:
            result += "\t"+"microsatellite"
        elif seq_memberid in mitochondrial_file:
            result += "\t" + "mitochondrial"
        elif seq_memberid in ribosomal_file:
            result += "\t" + "ribosomal"
        elif seq_memberid in AFLP_file:
            result += "\t" + "AFLP"
        elif seq_memberid in miRNA_file:
            result += "\t" + "miRNA"
        elif seq_memberid in cytochrome_file:
            result += "\t" + "cytochrome"
        elif seq_memberid in lectin_file:
            result += "\t" + "lectin"
        elif seq_memberid in caspase_file:
            result += "\t" + "caspase"
        elif seq_memberid in heat_file:
            result += "\t" + "heat_stock"
        elif seq_memberid in actin_file:
            result += "\t" + "actin"
        elif seq_memberid in tubulin_file:
            result += "\t" + "tubulin"
        elif seq_memberid in myosin_file:
            result += "\t" + "myosin"
        elif seq_memberid in hemocyanin_file:
            result += "\t" + "hemocyanin"
        elif seq_memberid in histone_file:
            result += "\t" + "histone"
        elif seq_memberid in internal_file:
            result += "\t" + "internal_transcribed_spacer"
        elif seq_memberid in SRAP_file:
            result += "\t" + "SRAP"
        elif seq_memberid in Penelope_file:
            result += "\t" + "Penelope"
        else:
            result += "\t" + "unknown"
    print result