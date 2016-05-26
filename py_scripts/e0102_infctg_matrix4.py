# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-12 10:39:21
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-12 10:56:19
import sys
def read_todic(file):
    tmp = []
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            tmp.append(l1_split[0])
    return tmp

glw = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pv/inf_ctg/e02pv_cap97_count.matrix_astran_flt_glw"
hev = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pv/inf_ctg/e02pv_cap97_count.matrix_astran_flt_hev"
hpw = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pv/inf_ctg/e02pv_cap97_count.matrix_astran_flt_hpw"

glw_lst = read_todic(glw)
hev_lst = read_todic(hev)
hpw_lst = read_todic(hpw)

uniq_id = list(set(glw_lst+hev_lst+hpw_lst))

for id_ in uniq_id:
    outline = id_
    if id_ in glw_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    if id_ in hev_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    if id_ in hpw_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    print outline
