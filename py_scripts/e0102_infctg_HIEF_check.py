# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-12 13:54:12
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-12 17:18:23
import sys
HIdesc="/mnt/nfs/media/Aung/Ortholog_Table/HI/HI_org.all"
EFdesc="/mnt/nfs/media/Aung/Ortholog_Table/EF/EF_org.all"
inf_ctg = sys.argv[1]

def read_todic(file):
    clstid = []
    idlist = []
    with open(file, 'rb') as f1:
        for l1 in f1:
            l1_split = l1.split('\t')
            clstid.append(l1_split[0])
            idlist.append(l1_split[2])            
    return clstid,idlist

HIdesc_clstid,HIdesc_idlist = read_todic(HIdesc)
EFdesc_clstid,EFdesc_idlist = read_todic(EFdesc)

# out = open(inf_ctg+"_efhiclst",'w')
with open(inf_ctg, 'rb') as f2:
        for l2 in f2:
            l2_split = l2.split('\t')
            id_ = l2_split[0]            
            
            HIind = []
            EFind = []
            for i,e in enumerate(HIdesc_idlist):
                for m in e.split(';'):
                    if id_ == m.strip('>\n').strip():
                        HIind.append(i)
            for i,e in enumerate(EFdesc_idlist):
                for m in e.split(';'):
                    if id_ == m.strip('>\n').strip():
                        EFind.append(i)
            HI_clst =[]
            EF_clst =[]
            for i in HIind:
                HI_clst.append(HIdesc_clstid[i])
            for i in EFind:
                EF_clst.append(EFdesc_clstid[i])

            uniqHI = list(set(HI_clst))                    
            uniqEF = list(set(EF_clst))
            sys.stdout.write(l2.strip('\n')+"\t"+';'.join(uniqHI)+"\t"+';'.join(uniqEF)+"\n")
