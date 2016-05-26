# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-25 10:40:09
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-25 17:46:41
import sys
old_desc = "/colossus/home/anuphap/ortho_table/20151022-paralogs_Ortho20150902_aS0.97.Org.ID.yesdesc"
new_desc = "/colossus/home/anuphap/ortho_table/EF/EF_combine.txt"
mapfile ="/colossus/home/anuphap/ortho_table/Aung_uniquesequence.fasta_Astranid_map"

aung_id = []
gi = []
with open(mapfile, 'rb') as f8:
    for l8 in f8:
        l8_split = l8.split('\t')
        for m in l8_split[3].split(';'):
            gi_ = m.split('|')[1].strip('\n')
            aung_id.append(l8_split[1])
            gi.append(gi_)

clst_id = []
clst_mem = []
with open(old_desc, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        for m in l3_split[2].split(';'):
            clst_id.append(l3_split[1].strip())
            if 'gi' in m:
                giid = m.split('|')[1].strip('\n')
                ind = gi.index(giid)
                clst_mem.append(aung_id[ind])        
            elif m =="":
                print "pass blank"
            else:    
                clst_mem.append(m.strip("Prot_"))        

o= open("HI_combine_compare_ortho.txt",'w')
with open(new_desc, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        tmp_oldclst = []
        id_list = l1_split[1]
        for x in id_list.split(';'):
            x = x.strip()
            if x in clst_mem:
                ind = clst_mem.index(x)
                tmp_oldclst.append(clst_id[ind])
        uniq_clst = []
        uniq_clst = list(set(tmp_oldclst))
        tmp_clst = ""
        for u in uniq_clst:
            if tmp_clst =="":
                tmp_clst = u
            else:
                tmp_clst += ";"+u
        o.write(l1.strip('\n')+"\t"+tmp_clst+"\n")