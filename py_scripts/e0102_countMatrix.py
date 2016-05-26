# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-21 15:38:10
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-26 18:26:30
import sys
idlist = "/mnt/nfs/media/Aung/e0102_kallisto/e02_pm/e02pm_Trinity/e02pm.id"
base="/mnt/nfs/media/Aung/e0102_kallisto/e02_pm/e02pm_Trinity/"

hcnn =base +"e02pm_CAP397_HC-N-N01/abundance.tsv"
hcns =base +"e02pm_CAP397_HC-N-S01/abundance.tsv"
hcv  =base +"e02pm_CAP397_HC-V-S01/abundance.tsv"
hcw  =base +"e02pm_CAP397_HC-W-S01/abundance.tsv"
lpnn =base +"e02pm_CAP397_LP-N-N01/abundance.tsv"
lpns =base +"e02pm_CAP397_LP-N-S01/abundance.tsv"
lpv  =base +"e02pm_CAP397_LP-V-S01/abundance.tsv"
lpy  =base +"e02pm_CAP397_LP-Y-S01/abundance.tsv"
twi  =base +"e02pm_CAP397_PmTwI/abundance.tsv"
twn  =base +"e02pm_CAP397_PmTwN/abundance.tsv"

hcnn_id = []
hcnn_count = []
with open(hcnn, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hcnn_id.append(l3_split[0])
        hcnn_count.append(l3_split[3].strip('\n'))

hcns_id = []
hcns_count = []
with open(hcns, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hcns_id.append(l3_split[0])
        hcns_count.append(l3_split[3].strip('\n'))

hcv_id = []
hcv_count = []
with open(hcv, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hcv_id.append(l3_split[0])
        hcv_count.append(l3_split[3].strip('\n'))

hcw_id = []
hcw_count = []
with open(hcw, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hcw_id.append(l3_split[0])
        hcw_count.append(l3_split[3].strip('\n'))

lpnn_id = []
lpnn_count = []
with open(lpnn, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        lpnn_id.append(l3_split[0])
        lpnn_count.append(l3_split[3].strip('\n'))

lpns_id = []
lpns_count = []
with open(lpns, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        lpns_id.append(l3_split[0])
        lpns_count.append(l3_split[3].strip('\n'))

lpv_id = []
lpv_count = []
with open(lpv, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        lpv_id.append(l3_split[0])
        lpv_count.append(l3_split[3].strip('\n'))

lpy_id = []
lpy_count = []
with open(lpy, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        lpy_id.append(l3_split[0])
        lpy_count.append(l3_split[3].strip('\n'))

twi_id = []
twi_count = []
with open(twi, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        twi_id.append(l3_split[0])
        twi_count.append(l3_split[3].strip('\n'))

twn_id = []
twn_count = []
with open(twn, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        twn_id.append(l3_split[0])
        twn_count.append(l3_split[3].strip('\n'))

sys.stdout.write("ID\tHC-NN\tHC-NS\tHC-V\tHC-W\tLP-NN\tLP-NS\tLP-V\tLP-Y\tTw-N\tTw-I\n")
with open(idlist,'rb') as f0:
    for l0 in f0:

        id_ = l0.strip('\n').strip('>')
        tmp = ""
        if id_ in hcnn_id:
            ind = hcnn_id.index(id_)
            if tmp == "":
                tmp = hcnn_count[ind]
            else:
                tmp += "\t"+hcnn_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in hcns_id:
            ind = hcns_id.index(id_)
            if tmp == "":
                tmp = hcns_count[ind]
            else:
                tmp += "\t"+hcns_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hcv_id:
            ind = hcv_id.index(id_)
            if tmp == "":
                tmp = hcv_count[ind]
            else:
                tmp += "\t"+hcv_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hcw_id:
            ind = hcw_id.index(id_)
            if tmp == "":
                tmp = hcw_count[ind]
            else:
                tmp += "\t"+hcw_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in lpnn_id:
            ind = lpnn_id.index(id_)
            if tmp == "":
                tmp = lpnn_count[ind]
            else:
                tmp += "\t"+lpnn_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in lpns_id:
            ind = lpns_id.index(id_)
            if tmp == "":
                tmp = lpns_count[ind]
            else:
                tmp += "\t"+lpns_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in lpv_id:
            ind = lpv_id.index(id_)
            if tmp == "":
                tmp = lpv_count[ind]
            else:
                tmp += "\t"+lpv_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in lpy_id:
            ind = lpy_id.index(id_)
            if tmp == "":
                tmp = lpy_count[ind]
            else:
                tmp += "\t"+lpy_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in twi_id:
            ind = twi_id.index(id_)
            if tmp == "":
                tmp = twi_count[ind]
            else:
                tmp += "\t"+twi_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in twn_id:
            ind = twn_id.index(id_)
            if tmp == "":
                tmp = twn_count[ind]
            else:
                tmp += "\t"+twn_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        sys.stdout.write(id_+"\t"+tmp+"\n")