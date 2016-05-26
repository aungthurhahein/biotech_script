# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-22 10:45:56
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-25 16:39:08
import sys
idlist = "/mnt/nfs/media/Aung/e0102_kallisto/e01_pm/CHULA/e01_pm_Trinity/e01_pm_trinity.id"
base="/mnt/nfs/media/Aung/e0102_kallisto/e01_pm/NCBI/e01_pm_Trinity/"

GillN=base+"NCBI01-Gill-N/aln_out/abundance.tsv"
GillW=base+"NCBI01-Gill-W/aln_out/abundance.tsv"
HCN=base+"NCBI01-HC-N/aln_out/abundance.tsv"
HCV=base+"NCBI01-HC-V/aln_out/abundance.tsv"
HCW=base+"NCBI01-HC-W/aln_out/abundance.tsv"
HCY=base+"NCBI01-HC-Y/aln_out/abundance.tsv"
LYN=base+"NCBI01-LY-N/aln_out/abundance.tsv"
LYV=base+"NCBI01-LY-V/aln_out/abundance.tsv"
LYY=base+"NCBI01-LY-Y/aln_out/abundance.tsv"
MLN=base+"NCBI01-ML-N/aln_out/abundance.tsv"
MLW=base+"NCBI01-ML-W/aln_out/abundance.tsv"
WHN=base+"NCBI01-WH-N/aln_out/abundance.tsv"
WHV=base+"NCBI01-WH-V/aln_out/abundance.tsv"
WHW=base+"NCBI01-WH-W/aln_out/abundance.tsv"

HCN_id = []
HCN_count = []
with open(HCN, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        HCN_id.append(l3_split[0])
        HCN_count.append(l3_split[3].strip('\n'))

HCV_id = []
HCV_count = []
with open(HCV, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        HCV_id.append(l3_split[0])
        HCV_count.append(l3_split[3].strip('\n'))

HCW_id = []
HCW_count = []
with open(HCW, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        HCW_id.append(l3_split[0])
        HCW_count.append(l3_split[3].strip('\n'))

HCY_id = []
HCY_count = []
with open(HCY, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        HCY_id.append(l3_split[0])
        HCY_count.append(l3_split[3].strip('\n'))

LYN_id = []
LYN_count = []
with open(LYN, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        LYN_id.append(l3_split[0])
        LYN_count.append(l3_split[3].strip('\n'))

LYV_id = []
LYV_count = []
with open(LYV, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        LYV_id.append(l3_split[0])
        LYV_count.append(l3_split[3].strip('\n'))

LYY_id = []
LYY_count = []
with open(LYY, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        LYY_id.append(l3_split[0])
        LYY_count.append(l3_split[3].strip('\n'))

MLN_id = []
MLN_count = []
with open(MLN, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        MLN_id.append(l3_split[0])
        MLN_count.append(l3_split[3].strip('\n'))

MLW_id = []
MLW_count = []
with open(MLW, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        MLW_id.append(l3_split[0])
        MLW_count.append(l3_split[3].strip('\n'))

WHN_id = []
WHN_count = []
with open(WHN, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        WHN_id.append(l3_split[0])
        WHN_count.append(l3_split[3].strip('\n'))

WHV_id = []
WHV_count = []
with open(WHV, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        WHV_id.append(l3_split[0])
        WHV_count.append(l3_split[3].strip('\n'))

WHW_id = []
WHW_count = []
with open(WHW, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        WHW_id.append(l3_split[0])
        WHW_count.append(l3_split[3].strip('\n'))

sys.stdout.write("ID\tHCN\tHCV\tHCW\tHCY\tLYN\tLYV\tLYY\tMLN\tMLW\tWHN\tWHV\tWHW\n")

with open(idlist,'rb') as f0:
    for l0 in f0:

        id_ = l0.strip('\n').strip('>')
        tmp = ""
        if id_ in HCN_id:
            ind = HCN_id.index(id_)
            if tmp == "":
                tmp = HCN_count[ind]
            else:
                tmp += "\t"+HCN_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in HCV_id:
            ind = HCV_id.index(id_)
            if tmp == "":
                tmp = HCV_count[ind]
            else:
                tmp += "\t"+HCV_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in HCW_id:
            ind = HCW_id.index(id_)
            if tmp == "":
                tmp = HCW_count[ind]
            else:
                tmp += "\t"+HCW_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in HCY_id:
            ind = HCY_id.index(id_)
            if tmp == "":
                tmp = HCY_count[ind]
            else:
                tmp += "\t"+HCY_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"


        if id_ in LYN_id:
            ind = LYN_id.index(id_)
            if tmp == "":
                tmp = LYN_count[ind]
            else:
                tmp += "\t"+LYN_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in LYV_id:
            ind = LYV_id.index(id_)
            if tmp == "":
                tmp = LYV_count[ind]
            else:
                tmp += "\t"+LYV_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in LYY_id:
            ind = LYY_id.index(id_)
            if tmp == "":
                tmp = LYY_count[ind]
            else:
                tmp += "\t"+LYY_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in MLN_id:
            ind = MLN_id.index(id_)
            if tmp == "":
                tmp = MLN_count[ind]
            else:
                tmp += "\t"+MLN_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in MLW_id:
            ind = MLW_id.index(id_)
            if tmp == "":
                tmp = MLW_count[ind]
            else:
                tmp += "\t"+MLW_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in WHN_id:
            ind = WHN_id.index(id_)
            if tmp == "":
                tmp = WHN_count[ind]
            else:
                tmp += "\t"+WHN_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in WHV_id:
            ind = WHV_id.index(id_)
            if tmp == "":
                tmp = WHV_count[ind]
            else:
                tmp += "\t"+WHV_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        if id_ in WHW_id:
            ind = WHW_id.index(id_)
            if tmp == "":
                tmp = WHW_count[ind]
            else:
                tmp += "\t"+WHW_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        sys.stdout.write(id_+"\t"+tmp+"\n")