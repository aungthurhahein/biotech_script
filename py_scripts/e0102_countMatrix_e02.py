# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-22 13:08:29
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-25 17:46:31
import sys
idlist = "/mnt/nfs/media/Aung/e0102_kallisto/e02_pv/mapped/trinity/e02pv.id"
base="/mnt/nfs/media/Aung/e0102_kallisto/e02_pv/mapped/trinity/"
gilln = base+"e01pv_CAP397_GillN/abundance.tsv"
gillw = base+"e01pv_CAP397_GillW/abundance.tsv"
hen = base+"e01pv_CAP397_HeN/abundance.tsv"
hew = base+"e01pv_CAP397_HeW/abundance.tsv"
hpn = base+"e01pv_CAP397_HPN/abundance.tsv"
hpw = base+"e01pv_CAP397_HPW/abundance.tsv"

gilln_id = []
gilln_count = []
with open(gilln, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        gilln_id.append(l3_split[0])
        gilln_count.append(l3_split[3].strip('\n'))

gillw_id = []
gillw_count = []
with open(gillw, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        gillw_id.append(l3_split[0])
        gillw_count.append(l3_split[3].strip('\n'))

hen_id = []
hen_count = []
with open(hen, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hen_id.append(l3_split[0])
        hen_count.append(l3_split[3].strip('\n'))

hew_id = []
hew_count = []
with open(hew, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hew_id.append(l3_split[0])
        hew_count.append(l3_split[3].strip('\n'))

hpn_id = []
hpn_count = []
with open(hpn, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hpn_id.append(l3_split[0])
        hpn_count.append(l3_split[3].strip('\n'))

hpw_id = []
hpw_count = []
with open(hpw, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        hpw_id.append(l3_split[0])
        hpw_count.append(l3_split[3].strip('\n'))

sys.stdout.write("ID\tGill-N\tGill-W\tHE-N\tHE-W\tHP-N\tHP-W\n")
with open(idlist,'rb') as f0:
    for l0 in f0:

        id_ = l0.strip('\n').strip('>')
        tmp = ""
        if id_ in gilln_id:
            ind = gilln_id.index(id_)
            if tmp == "":
                tmp = gilln_count[ind]
            else:
                tmp += "\t"+gilln_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        
        if id_ in gillw_id:
            ind = gillw_id.index(id_)
            if tmp == "":
                tmp = gillw_count[ind]
            else:
                tmp += "\t"+gillw_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hen_id:
            ind = hen_id.index(id_)
            if tmp == "":
                tmp = hen_count[ind]
            else:
                tmp += "\t"+hen_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hew_id:
            ind = hew_id.index(id_)
            if tmp == "":
                tmp = hew_count[ind]
            else:
                tmp += "\t"+hew_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hpn_id:
            ind = hpn_id.index(id_)
            if tmp == "":
                tmp = hpn_count[ind]
            else:
                tmp += "\t"+hpn_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"

        if id_ in hpw_id:
            ind = hpw_id.index(id_)
            if tmp == "":
                tmp = hpw_count[ind]
            else:
                tmp += "\t"+hpw_count[ind]
        else:
            if tmp == "":
                tmp = "-"
            else:
                tmp += "\t-"
        sys.stdout.write(id_+"\t"+tmp+"\n")