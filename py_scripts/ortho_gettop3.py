# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-20 17:53:37
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-21 11:27:34
import sys

desc = sys.argv[1]

with open(desc,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        id_ = l1_split[0]
        desc = l1_split[1].split(';')
        tmp_mem = []        
        for m in desc[0:3]:
            tmp_mem.append(m)
        sorted(tmp_mem,reverse=True)

        tmp_string =""
        for x in tmp_mem:
            if tmp_string =="":
                tmp_string = x
            else:
                tmp_string +="|"+x
        
        desc_final = tmp_string.split('|')        
        output = ""
        sorted(desc_final,reverse=True)
        for x in desc_final[0:3]:
            if output =="":
                output = id_+'\t'+x
            else:
                output += "|"+x
        sys.stdout.write(output.strip('\n')+"\n")





