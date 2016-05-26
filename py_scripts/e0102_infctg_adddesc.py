# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-13 10:56:19
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-13 12:25:28
import sys
HIdesc="/mnt/nfs/media3/Ortho_20151125/HI/ClusterDesc/HI_SpeciesDistr_LVPM.lst.CatORGIN.desc01.wD.uniq"
EFdesc="/mnt/nfs/media3/Ortho_20151125/EF/ClusterDesc/EF_SpeciesDistr_LVPM.lst.CatORGIN.desc01.uniq.wD"
inf_ctg = sys.argv[1]

def read_todic(file):
    clstid = []
    desclst = []
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            clstid.append(l1_split[1])
            desclst.append(l1_split[7].strip('\n'))            
    return clstid,desclst

HIdesc_clstid,HIdesc_desclist = read_todic(HIdesc)
EFdesc_clstid,EFdesc_desclist = read_todic(EFdesc)
out = open(inf_ctg+".desc",'w')
with open(inf_ctg, 'rb') as f2:
        for l2 in f2:
            l2_split = l2.split('\t')
            HIid_ = l2_split[-2]            
            EFid_ = l2_split[-1].strip('\n')            

            hidesc="-"
            efdesc="-"
            for m in HIid_.split(';'):
                if m in HIdesc_clstid:
                    ind = HIdesc_clstid.index(m)
                    if hidesc =="-":
                        hidesc = HIdesc_desclist[ind]
                    else:
                        hidesc += "|"+HIdesc_desclist[ind]
            for k in EFid_.split(';'):
                if k in EFdesc_clstid:                    
                    ind2 = EFdesc_clstid.index(k)
                    if efdesc =="-":
                        efdesc = EFdesc_desclist[ind2]            
                    else:
                        efdesc += "|"+EFdesc_desclist[ind2]            
            out.write(l2.strip('\n')+'\t'+hidesc+'\t'+efdesc+'\n')

