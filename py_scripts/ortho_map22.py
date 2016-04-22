# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-21 10:36:24
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-21 15:34:51
import re
import sys
idlist = sys.argv[1]
prefix=["PM_e0101",
        "PM_e0102",
        "PV_e0106",
        "V3_SIEST01",
        "PVPM_E0102",
        "Pool_contigsV22",
        "DN_ENS01",        
        "PH_ENS01",
        "TC_ENS01"
        ]
base = "/mnt/nfs/media/Aung/Ortholog_Table/desc/"
e0101 = base+"e0101_short.desc"
e0102 = base+"e0102_short.desc"
e0106 = base+"e0106_short.desc"
siest = base+"SIEST.desc"
e01_02 = base+"E0102.desc"
contigs = base+"contigsV22.desc"
dn_ens01 = base+"DN_ENS01_flt.desc"
ph_ens01 = base+"PH_ENS01_flt.desc"
tc_ens01 = base+"TC_ENS01_flt.desc"

# e0101
e0101_id = []
e0101_desc = []
with open(e0101, 'rb') as f6:
    for l6 in f6:
        l6_split = l6.split('\t')
        e0101_id.append(l6_split[0])
        e0101_desc.append(l6_split[1].strip('\n'))

# e0102
e0102_id = []
e0102_desc = []
with open(e0102, 'rb') as f8:
    for l8 in f8:
        l8_split = l8.split('\t')
        e0102_id.append(l8_split[0])
        e0102_desc.append(l8_split[1].strip('\n'))

# e0106
e0106_id = []
e0106_desc = []
with open(e0106, 'rb') as f9:
    for l9 in f9:
        l9_split = l9.split('\t')
        e0106_id.append(l9_split[0])
        e0106_desc.append(l9_split[1].strip('\n'))

# V3_SIEST01_100001
siest_id = []
siest_desc = []
with open(siest, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        siest_id.append(l3_split[0])
        siest_desc.append(l3_split[1].strip('\n'))

# PVPM_E0102_10001
e01_02_id = []
e01_02_desc = []
with open(e01_02, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        e01_02_id.append(l2_split[0])
        e01_02_desc.append(l2_split[1].strip('\n'))

# Pool_contigsV22_
contigs_id = []
contigs_desc = []
with open(contigs,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        contigs_id.append(l1_split[0])
        contigs_desc.append(l1_split[1].strip('\n'))

# dn_ens01
dn_ens01_id = []
dn_ens01_desc = []
with open(dn_ens01,'rb') as f10:
    for l10 in f10:
        l10_split = l10.split('\t')
        dn_ens01_id.append(l10_split[0])
        dn_ens01_desc.append(l10_split[1].strip('\n'))

#ph_ens01
ph_ens01_id = []
ph_ens01_desc = []
with open(ph_ens01,'rb') as f11:
    for l11 in f11:
        l11_split = l11.split('\t')
        ph_ens01_id.append(l11_split[0])
        ph_ens01_desc.append(l11_split[1].strip('\n'))

#ph_ens01
tc_ens01_id = []
tc_ens01_desc = []
with open(tc_ens01,'rb') as f12:
    for l12 in f12:
        l12_split = l12.split('\t')
        tc_ens01_id.append(l12_split[0])
        tc_ens01_desc.append(l12_split[1].strip('\n'))

outfile = open(idlist+".desc",'w')
with open(idlist,'rb') as f0:
    for l0 in f0:
        l0_split = l0.split('\t')
        clstid_ = l0_split[0]
        num = l0_split[1]
        num2 = l0_split[2]
        mem = l0_split[3].split(';')
        tmp_desc = ""
        for m in mem:
            m = m.strip().strip('\n')
            if prefix[0] in m:
                if m in e0101_id:
                    ind = e0101_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = e0101_desc[ind]
                    else:
                        tmp_desc += ";"+e0101_desc[ind]
            if prefix[1] in m:
                if m in e0102_id:
                    ind = e0102_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = e0102_desc[ind]
                    else:
                        tmp_desc += ";"+e0102_desc[ind]
            if prefix[2] in m:
                if m in e0106_id:
                    ind = e0106_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = e0106_desc[ind]
                    else:
                        tmp_desc += ";"+e0106_desc[ind]
            if prefix[3] in m:
                if m in siest_id:
                    ind = siest_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = siest_desc[ind]
                    else:
                        tmp_desc += ";"+siest_desc[ind]
            if prefix[4] in m:
                if m in e01_02_id:
                    ind = e01_02_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = e01_02_desc[ind]
                    else:
                        tmp_desc += ";"+e01_02_desc[ind]
            if prefix[5] in m:
                if m in contigs_id:
                    ind = contigs_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = contigs_desc[ind]
                    else:
                        tmp_desc += ";"+contigs_desc[ind]
            if prefix[6] in m:
                if m in dn_ens01_id:
                    ind = dn_ens01_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = dn_ens01_desc[ind]
                    else:
                        tmp_desc += ";"+dn_ens01_desc[ind]
            if prefix[7] in m:
                if m in ph_ens01_id:
                    ind = ph_ens01_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = ph_ens01_desc[ind]
                    else:
                        tmp_desc += ";"+ph_ens01_desc[ind]
            if prefix[8] in m:
                if m in tc_ens01_id:
                    ind = tc_ens01_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = tc_ens01_desc[ind]
                    else:
                        tmp_desc += ";"+tc_ens01_desc[ind]
        outfile.write(clstid_+'\t'+num+'\t'+num2+'\t'+l0_split[3].strip('\n')+'\t'+tmp_desc+'\n')
