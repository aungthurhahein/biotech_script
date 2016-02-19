#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-15 17:52:19
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-15 18:09:51
import sys

baseStr="perl $step2blastp $inputfiles$prefix2 $outputdir $qsubout $db $blasttype"
start = 0
end = sys.argv[1]
strname = sys.argv[2]
i = 0
tmpend = 50

while start < int(end):
    i = i+1    
    sys.stdout.write(baseStr+" "+str(start)+" "+str(tmpend)+" "+strname+str(i)+"\n")
    start = tmpend+1
    tmpend =  tmpend+50
