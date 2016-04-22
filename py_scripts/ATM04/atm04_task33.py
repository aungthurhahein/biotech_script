# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-09 17:56:30
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-09 18:30:37
import sys
atm04mapfile = sys.argv[1]

ab = open(atm04mapfile+".Ab",'w')
ar = open(atm04mapfile+".Ar",'w')
ak = open(atm04mapfile+".Ak",'w')

rb = open(atm04mapfile+".Rb",'w')
rr = open(atm04mapfile+".Rr",'w')
rk = open(atm04mapfile+".Rk",'w')

with open(atm04mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        gpra = l1_split[10].strip('\n').strip()
        if gpra == "Ab":
            ab.write(l1)
        elif gpra == "AR":
            ar.write(l1)
        elif gpra =="AK":
            ak.write(l1)
        elif gpra =="Rb":
            rb.write(l1)
        elif gpra == "RK":
            rb.write(l1)

# python task33.py atm04_common_kallisto_rsem.D.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.E.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.F.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.G.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.I1.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.I2.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.I4.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.I6.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.I7.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.K.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.L.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.matrix.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.M.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.N.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.O.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.P.fmt.grpa
# python task33.py atm04_common_kallisto_rsem.U.fmt.grpa
