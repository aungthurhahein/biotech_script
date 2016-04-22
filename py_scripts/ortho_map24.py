# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-21 12:27:18
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-21 12:32:01
import re
import sys
idlist = sys.argv[1]
prefix=["gpatNuclV3"]
base = "/mnt/nfs/media/Aung/Ortholog_Table/desc/"
nucl = base+"Nucl.desc"

nucl_id = []
nucl_desc = []
with open(nucl, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        nucl_id.append(l3_split[0])
        nucl_desc.append(l3_split[3].strip('\n'))

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
                if m in nucl_id:
                    ind = nucl_id.index(m)
                    if tmp_desc == "":
                        tmp_desc = nucl_desc[ind]
                    else:
                        tmp_desc += ";"+nucl_desc[ind]
            outfile.write(clstid_+'\t'+num+'\t'+num2+'\t'+l0_split[3].strip('\n')+'\t'+tmp_desc+'\n')