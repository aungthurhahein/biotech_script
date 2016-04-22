# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-09 18:07:46
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-09 18:30:34
import sys
atm04mapfile = sys.argv[1]
with open(atm04mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')        
        rsem5 = float(l1_split[4]) #col5
        kal8 = float(l1_split[7]) #col8

        col12 = str(max(rsem5,kal8))
        col13 = str(min(rsem5,kal8))
        sys.stdout.write(l1.strip('\n')+"\t"+col12+"\t"+col13+"\n")

# python task33A2.py atm04_common_kallisto_rsem.D.fmt.grpa.Rb > atm04_common_kallisto_rsem.D.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.E.fmt.grpa.Rb > atm04_common_kallisto_rsem.E.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.F.fmt.grpa.Rb > atm04_common_kallisto_rsem.F.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.G.fmt.grpa.Rb > atm04_common_kallisto_rsem.G.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.I1.fmt.grpa.Rb > atm04_common_kallisto_rsem.I1.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.I2.fmt.grpa.Rb > atm04_common_kallisto_rsem.I2.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.I4.fmt.grpa.Rb > atm04_common_kallisto_rsem.I4.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.I6.fmt.grpa.Rb > atm04_common_kallisto_rsem.I6.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.I7.fmt.grpa.Rb > atm04_common_kallisto_rsem.I7.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.K.fmt.grpa.Rb > atm04_common_kallisto_rsem.K.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.L.fmt.grpa.Rb > atm04_common_kallisto_rsem.L.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.matrix.fmt.grpa.Rb > atm04_common_kallisto_rsem.matrix.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.M.fmt.grpa.Rb > atm04_common_kallisto_rsem.M.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.N.fmt.grpa.Rb > atm04_common_kallisto_rsem.N.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.O.fmt.grpa.Rb > atm04_common_kallisto_rsem.O.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.P.fmt.grpa.Rb > atm04_common_kallisto_rsem.P.fmt.grpa.Rb.col
# python task33A2.py atm04_common_kallisto_rsem.U.fmt.grpa.Rb > atm04_common_kallisto_rsem.U.fmt.grpa.Rb.col
