#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date:
 python ../../c01p_count_trinity.py ../../../A.id ../../../L.id ../../../C.id ../../../Cu.id ~card/Aung/mapped/c01/c01_orgreads/id_list/control.id ~card/Aung/mapped/c01/c01_orgreads/id_list/mature.id ~card/Aung/mapped/c01/c01_orgreads/id_list/survival.id c01p-02t_out.clstr.parse2_G2LC ../../../c01_TrinityDE.tsv c01p_02T > G2LC.stat

"""
import sys
A_id = sys.argv[1]  # A
L_id = sys.argv[2]  # L
C_id = sys.argv[3]  # C
Cu_id = sys.argv[4]  # C Unmap
Control_id = sys.argv[5]  # control_id
Mature_id = sys.argv[6]   # mature_id
Survival_id = sys.argv[7]  # survival_id
cluster_file = sys.argv[8]  # cluster parsed file
DE_file = sys.argv[9]  # DE File
set_name = sys.argv[10]  # setname

open_Aid = open(A_id, 'r')
open_Lid = open(L_id, 'r')
open_Cid = open(C_id, 'r')
open_Cuid = open(Cu_id, 'r')
open_controlid = open(Control_id, 'r')
open_matureid = open(Mature_id, 'r')
open_survivalid = open(Survival_id, 'r')
open_cluster = open(cluster_file, 'r')
open_de = open(DE_file, 'r')

A_id_list = []
L_id_list = []
C_id_list = []
Cu_id_list = []
control_list = []
mature_list = []
survival_list = []
clst_list = []
de_id = []
de_record = []

for id1 in open_Aid:
    A_id_list.append(id1.strip())
for id2 in open_Lid:
    L_id_list.append(id2.strip())
for id3 in open_Cid:
    C_id_list.append(id3.strip())
for id4 in open_Cuid:
    Cu_id_list.append(id4.strip())
for cluster in open_cluster:
    clst_list.append(cluster.strip())
for control in open_controlid:
    control_list.append(control.strip())
for mature in open_matureid:
    mature_list.append(mature.strip())
for survival in open_survivalid:
    survival_list.append(survival.strip())
for de in open_de:
    de_split = de.split('\t')
    de_id.append(de_split[0].strip())
    de_record.append(de_split[1:])

def delindx(delindex, del_object):
    for y in reversed(delindex):
        del del_object[y]

print 'Set\tClusterID\tInfoType\t#'
for x in clst_list:
    x_split = x.split('\t')
    AL_count = 0
    del_indx = []
    AL_List = []
    C_List = []
    CUnmap_list = []
    clustername = x_split[0]
    del x_split[0]
    # AL
    for x, mem in enumerate(x_split):
        if mem.strip() in A_id_list or mem.strip() in L_id_list:
            AL_List.append(mem.strip())
            del_indx.append(x)

    delindx(del_indx, x_split)
    del_indx = []

    # C
    for z, memb in enumerate(x_split):
        if memb.strip() in C_id_list:
            C_List.append(memb.strip())
            del_indx.append(z)

    delindx(del_indx, x_split)
    del_indx = []

    # C Unmap
    for k, member in enumerate(x_split):
        if member.strip() in Cu_id_list:
            CUnmap_list.append(member.strip())
            del_indx.append(k)
    delindx(del_indx, x_split)

    tmp_string = ""
    tmp_string2 = ""
    tmp_string3 = ""

    # AL
    tmp_string = set_name + '\t' + clustername + '\t' + 'A/L' + '\t' + str(len(AL_List)) + '\t'
    for al in AL_List:
        tmp_string += al + '\t'
    print tmp_string

    # C
    for C01 in C_List:
        tmp_string2 = ""
        tmp_string2 = set_name + '\t' + clustername + '\t' + 'C01_Trinity' + '\t'
        tmp_string2 += C01 + '\t'
        if C01.strip().strip('>') in de_id:
            for derecord in de_record[de_id.index(C01.strip().strip('>'))]:
                tmp_string2 += derecord + '\t'
        print tmp_string2

    # C Unmap
    tmp_string3 = set_name + '\t' + clustername + '\t' + 'C01_Trinity_Unmap' + '\t' + str(len(CUnmap_list)) + '\t'
    Control_count = 0
    Mature_count = 0
    Survival_count = 0
    for CU in CUnmap_list:
        if CU.strip() in control_list:
            Control_count += 1
        elif CU.strip() in mature_list:
            Mature_count += 1
        elif CU.strip() in survival_list:
            Survival_count += 1
    tmp_string3 += str(Control_count) + '\t' + str(Mature_count) + '\t' + str(Survival_count)

    if len(CUnmap_list) > 0:
        print tmp_string3

