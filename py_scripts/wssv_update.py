__author__ = 'aung'
import sys

wssv_file = sys.argv[1]
de_annotfile = sys.argv[2]

def file_read(fileinput):
    temp_list = []
    for k in fileinput:
        temp_list.append(k)
    return temp_list

#file open
wssv_open = open(wssv_file,'r')
deannot_open = open(de_annotfile,'r')
wssv_list = []
for k in wssv_open:
    k_split = k.split('\t')
    geneid = k_split[0].split('_')
    geneid = geneid[0]+"_"+geneid[1]
    wssv_list.append(geneid.strip())

deannot_list = file_read(deannot_open)

for annot in deannot_list:
    annot_split = annot.split('\t')
    annot_id = annot_split[0].strip()# 0 15
    if annot_id in wssv_list:
        tmp = annot.strip('\n') + "\t" + "wssv"
    else:
        tmp = annot.strip('\n') + "\t" + "-"
    print tmp
