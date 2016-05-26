# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-11 13:38:23
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-11 14:11:19
import sys
idlist = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/input/refid.lst"
hcnn = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/HCNN.map_astran.refmapcount"
hcns = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/HCNS.map_astran.refmapcount"
hcv = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/HCV.map_astran.refmapcount"
hcw = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/HCW.map_astran.refmapcount"
lpnn = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/LPNN.map_astran.refmapcount"
lpns = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/LPNS.map_astran.refmapcount"
lpv = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/LPV.map_astran.refmapcount"
lpy = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/LPY.map_astran.refmapcount"
twi = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/TWI.map_astran.refmapcount"
twn = "/mnt/nfs/media/Aung/mapped/count_matrix/CHULA_CAP397_Org/refmapcount/TWN.map_astran.refmapcount"

def read_todic(file):
    tmp = {}
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            tmp[l1_split[0]] = l1_split[2].strip('\n')
    return tmp

twi_dic = read_todic(twi) 
twn_dic = read_todic(twn) 
hcnn_dic = read_todic(hcnn) 
hcns_dic = read_todic(hcns) 
hcv_dic = read_todic(hcv) 
hcw_dic = read_todic(hcw) 
lpnn_dic = read_todic(lpnn) 
lpns_dic = read_todic(lpns) 
lpv_dic = read_todic(lpv) 
lpy_dic = read_todic(lpy) 


with open(idlist, 'rb') as f1:
    for l1 in f1:
        id_ = l1.strip('\n')
        tmp_res = id_
        if id_ in twi_dic:
            tmp_res += "\t"+twi_dic[id_]
        else:
            tmp_res += "\t"+"0"
        
        if id_ in twn_dic:
            tmp_res += "\t"+twn_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in hcnn_dic:
            tmp_res += "\t"+hcnn_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in hcns_dic:
            tmp_res += "\t"+hcns_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in hcv_dic:
            tmp_res += "\t"+hcv_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in hcw_dic:
            tmp_res += "\t"+hcw_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in lpnn_dic:
            tmp_res += "\t"+lpnn_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in lpns_dic:
            tmp_res += "\t"+lpns_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in lpns_dic:
            tmp_res += "\t"+lpns_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in lpv_dic:
            tmp_res += "\t"+lpv_dic[id_]
        else:
            tmp_res += "\t"+"0"

        if id_ in lpy_dic:
            tmp_res += "\t"+lpy_dic[id_]
        else:
            tmp_res += "\t"+"0"
        sys.stdout.write(tmp_res+"\n")