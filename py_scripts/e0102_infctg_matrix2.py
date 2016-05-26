# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-11 17:34:10
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-12 10:55:24
import sys
def read_todic(file):
    tmp = []
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            tmp.append(l1_split[0])
    return tmp

hcv = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pm/inf_ctg/e02pm_cap97_count.matrix_astran_flt_hcv"
lpv = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pm/inf_ctg/e02pm_cap97_count.matrix_astran_flt_hcw"
whw = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pm/inf_ctg/e02pm_cap97_count.matrix_astran_flt_lpv"
hcw = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pm/inf_ctg/e02pm_cap97_count.matrix_astran_flt_lpy"
lpy = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e02pm/inf_ctg/e02pm_cap97_count.matrix_astran_flt_whw"

hcv_lst = read_todic(hcv)
lpv_lst = read_todic(lpv)
whw_lst = read_todic(whw)
hcw_lst = read_todic(hcw)
lpy_lst = read_todic(lpy)

uniq_id = list(set(hcv_lst+lpv_lst+whw_lst+hcw_lst+lpy_lst))

for id_ in uniq_id:
    outline = id_
    if id_ in hcv_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpv_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    
    if id_ in whw_lst :
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in hcw_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpy_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    print outline
        