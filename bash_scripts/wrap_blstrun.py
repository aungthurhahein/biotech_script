# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-10 14:44:53
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-10 15:41:51
import sys

base_str ="perl $step2blastp $inputfiles$prefix2 $outputdir $qsubout $db $blasttype "
prefix = "OrthoRegEF-HI"
nofile= 100
start = 1
end = 7274
tmpend  = 0
o=open("blstrun.log",'w')
while (end >= 0):
    if (end-nofile) > 0:
        tmpend +=nofile
        o.write(base_str+str(start)+" "+str(tmpend)+" "+prefix+str(start)+"\n")
        end = end - nofile
        start += nofile        
    else:
        tmpend = tmpend+end        
        end = end - nofile
        o.write(base_str+str(start)+" "+str(tmpend)+" "+prefix+str(start)+"\n")
