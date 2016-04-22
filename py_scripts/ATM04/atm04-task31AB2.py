# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-09 15:22:41
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-09 18:30:38
import sys
atm04mapfile = sys.argv[1]
with open(atm04mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        rsem2 = float(l1_split[2])
        rsem3 = float(l1_split[3])
        kal5 =  float(l1_split[5])
        kal6 =  float(l1_split[6])
        Grpa = ""            
        if rsem2 == 0.0 and rsem3 == 0.0 and kal5 == 0.0 and kal6 == 0.0: 
            Grpa = "O"
        elif rsem2 > 0 and rsem3 == 0.0 and kal5 > 0 and kal6 == 0.0: 
            Grpa = "Ab"
        elif rsem2 > 0 and rsem3 == 0.0 and kal5 == 0.0 and kal6 == 0.0: 
            Grpa = "AR"
        elif rsem2 == 0.0 and rsem3 == 0.0 and kal5 == 0.0 and kal6 == 0.0: 
            Grpa = "AK" 
        elif rsem2 == 0.0 and rsem3 > 0 and kal5 == 0.0 and kal6 > 0: 
            Grpa = "Nb" 
        elif rsem2 == 0.0 and rsem3 > 0 and kal5 == 0.0 and kal6  == 0.0: 
            Grpa = "NR" 
        elif rsem2 == 0.0 and rsem3 > 0 and kal5 == 0.0 and kal6 == 0.0: 
            Grpa = "NK" 
        elif rsem2> 0 and rsem3 > 0 and kal5 > 0 and kal6 > 0: 
            Grpa = "Rb" 
        elif rsem2 > 0 and rsem3 > 0 and kal5 == 0.0 and kal6 == 0.0: 
            Grpa = "RR" 
        elif rsem2 == 0.0 and rsem3 == 0.0 and kal5 > 0 and kal6 > 0: 
            Grpa = "RK" 
        else:
            Grpa = "X"
        # col12 = str(max(rsem2,kal5))
        # col13 = str(max(rsem3,kal6))
        sys.stdout.write(l1.strip('\n')+"\t"+Grpa+"\n")
        

# python update11.py atm04_common_kallisto_rsem.D.fmt > atm04_common_kallisto_rsem.D.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.E.fmt > atm04_common_kallisto_rsem.E.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.F.fmt > atm04_common_kallisto_rsem.F.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.G.fmt > atm04_common_kallisto_rsem.G.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.I1.fmt > atm04_common_kallisto_rsem.I1.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.I2.fmt > atm04_common_kallisto_rsem.I2.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.I4.fmt > atm04_common_kallisto_rsem.I4.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.I6.fmt > atm04_common_kallisto_rsem.I6.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.I7.fmt > atm04_common_kallisto_rsem.I7.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.K.fmt > atm04_common_kallisto_rsem.K.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.L.fmt > atm04_common_kallisto_rsem.L.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.matrix.fmt > atm04_common_kallisto_rsem.matrix.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.M.fmt > atm04_common_kallisto_rsem.M.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.N.fmt > atm04_common_kallisto_rsem.N.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.O.fmt > atm04_common_kallisto_rsem.O.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.P.fmt > atm04_common_kallisto_rsem.P.fmt.grpa
# python update11.py atm04_common_kallisto_rsem.U.fmt > atm04_common_kallisto_rsem.U.fmt.grpa


