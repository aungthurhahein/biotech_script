# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-21 11:49:18
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-21 15:34:48
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-21 10:36:24
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-21 11:30:22
import re
import sys
idlist = sys.argv[1]
prefix=["20150902Aung"]
base = "/mnt/nfs/media/Aung/Ortholog_Table/desc/"
prov22 = base+"prov22.desc"
mapfile = base+"Aung_uniquesequence.fasta_Astranid_map"

aung_id = []
gi = []
with open(mapfile, 'rb') as f8:
    for l8 in f8:
        l8_split = l8.split('\t')
        for m in l8_split[3].split(';'):
            gi_ = m.split('|')[1].strip('\n')
            aung_id.append(l8_split[1])
            gi.append(gi_)

prov22_id = []
prov22_desc = []
with open(prov22, 'rb') as f9:
    for l9 in f9:
        l9_split = l9.split('\t')
        giid = l9_split[0]
        if giid in gi:
            ind = gi.index(giid)
            prov22_id.append(aung_id[ind])
            prov22_desc.append(l9_split[1].strip('\n'))

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
                if m in prov22_id:
                    ind = prov22_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = prov22_desc[ind]
                    else:
                        tmp_desc += ";"+prov22_desc[ind]
        outfile.write(clstid_+'\t'+num+'\t'+num2+'\t'+l0_split[3].strip('\n')+'\t'+tmp_desc+'\n')


            MCL.mul.mul.mul.txt_flt
            MCL.sing.mul.mul.txt_flt