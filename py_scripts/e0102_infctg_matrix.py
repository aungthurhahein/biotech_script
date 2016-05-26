import sys

hcv_chula = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/CHULA/inf_ctg/e01pm_cap97_count.matrix_astran_flt_hcv"
hcw_chula = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/CHULA/inf_ctg/e01pm_cap97_count.matrix_astran_flt_hcw"
lpv_chula = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/CHULA/inf_ctg/e01pm_cap97_count.matrix_astran_flt_lpv"
lpy_chula = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/CHULA/inf_ctg/e01pm_cap97_count.matrix_astran_flt_lpy"
whw_chula = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/CHULA/inf_ctg/e01pm_cap97_count.matrix_astran_flt_whw"

hcv_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_hcv"
hcw_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_hcw"
hcy_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_hcy"
lpv_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_lpv"
lpy_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_lpy"
mlw_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_mlw"
whv_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_whv"
whw_ncbi = "/mnt/nfs/media/Aung/e0102_kallisto/count_matrix/e01pm/NCBI/inf_ctg/e01pm_cap97_count.matrix_astran_flt_whw"

def read_todic(file):
    tmp = []
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            tmp.append(l1_split[0])
    return tmp

hcv_chula_lst = read_todic(hcv_chula) 
hcw_chula_lst = read_todic(hcw_chula) 
lpv_chula_lst = read_todic(lpv_chula) 
lpy_chula_lst = read_todic(lpy_chula) 
whw_chula_lst = read_todic(whw_chula) 

hcv_ncbi_lst = read_todic(hcv_ncbi)
hcw_ncbi_lst = read_todic(hcw_ncbi)
hcy_ncbi_lst = read_todic(hcy_ncbi)
lpv_ncbi_lst = read_todic(lpv_ncbi)
lpy_ncbi_lst = read_todic(lpy_ncbi)
mlw_ncbi_lst = read_todic(mlw_ncbi)
whv_ncbi_lst = read_todic(whv_ncbi)
whw_ncbi_lst = read_todic(whw_ncbi)

uniq_id = list(set(hcv_chula_lst+hcw_chula_lst+lpv_chula_lst+lpy_chula_lst+whw_chula_lst+hcv_ncbi_lst+hcw_ncbi_lst+hcy_ncbi_lst+lpv_ncbi_lst+lpy_ncbi_lst+mlw_ncbi_lst+whv_ncbi_lst+whw_ncbi_lst))


for id_ in uniq_id:
    outline = id_
    if id_ in hcv_chula_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in hcw_chula_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpv_chula_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpy_chula_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in whw_chula_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in hcv_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in hcw_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in hcy_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpv_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in lpy_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in mlw_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in whv_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'

    if id_ in whw_ncbi_lst:
        outline += "\t"+'1'
    else:
        outline += "\t"+'0'
    print outline