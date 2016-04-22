# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-19 10:04:27
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-19 11:44:22
import sys
orthofile = sys.argv[1]

prefix=["20150902Aung"]
wrf= open(orthofile+"_flt",'w')
with open(orthofile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        id_list = l1_split[2].split(';')        
        tmp_list = ""
        for m in id_list:
            tmp = 0
            for x in prefix:
                if x in m:
                    tmp = 1
                    break;
            if tmp == 1:
                if tmp_list == "":
                    tmp_list = m.strip('\n')
                else:
                    tmp_list += ";"+ m.strip('\n')
        print l1
        if tmp_list == "":
            lentmp = "0"
        else:
            lentmp = str(len(tmp_list.split(';')))
        wrf.write(l1_split[0]+"\t"+l1_split[1]+"\t"+lentmp+"\t"+tmp_list+'\n') 



