# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-20 17:53:37
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-28 14:06:08
import sys
desc = sys.argv[1]
with open(desc,'rb') as f1:
    for l1 in f1:        
        l1_split = l1.split('\t')
        clstid = l1_split[0]
        id_ = l1_split[1]
        oldclst = l1_split[3].strip('\n')
        desc = l1_split[2].split(';')
        tmp_mem = []        
        for m in desc[0:3]:
            tmp_mem.append(m)
        sorted(tmp_mem,reverse=True)

        tmp_string =""
        for x in tmp_mem:
            if tmp_string =="":
                tmp_string = x.strip('|;')
            else:
                tmp_string +="|"+x.strip('|;')
        
        desc_final = tmp_string.split('|')        
        tmp_desc = ""        
        sorted(desc_final,reverse=True)
        print desc_final
        for x in desc_final[0:3]:                        
            if tmp_desc == "":
                tmp_desc = x
            else:
                tmp_desc += "|"+x        

        output = clstid+'\t'+id_+'\t'+tmp_desc+'\t'+oldclst        
        sys.stdout.write(output.strip('\n')+"\n")





