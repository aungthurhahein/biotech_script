#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]
genuscount = sys.argv[2]

inter_id = []
atm_id = []
with open(mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        inter_id.append(l1_split[2].strip('\n').strip('>'))
        atm_id.append(l1_split[1])

with open(genuscount,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        tmp = ""
        for x in l2_split[5].split(';'):            
            x2 = x.strip('\n').strip('-XN')            
            if "CDF" in x2:
                xorn = x.split('-')[2]
                indexes = [i for i,e in enumerate(inter_id) if e == x2.strip()] 
                for i in indexes:
                    if tmp == "":
                        tmp = atm_id[i]+"-"+xorn
                    else:
                        tmp += ';'+atm_id[i]+"-"+xorn
            else:                                
                if len(x.split('-')) > 1:                
                    xorn = x.split('-')[1]
                else:
                    xorn = ""
                if tmp == "":
                    tmp = x2+"-"+xorn
                else:
                    tmp += ';'+x2+"-"+xorn

        sys.stdout.write(l2_split[0]+'\t'+l2_split[1]+'\t'+l2_split[2]+'\t'+l2_split[3]+'\t'+l2_split[4]+'\t'+str(len(tmp.split(';'))-1)+'\t'+tmp+'\n')

# cat /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.I6.sort | awk -F '\t' '{if ($9 >0) print $0}' > /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0
# cat /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.I8.sort | awk -F '\t' '{if ($9 >0) print $0}' > /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0
# cat /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.D.sort | awk -F '\t' '{if ($9 >0) print $0}' > /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0
# cat /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.E.sort | awk -F '\t' '{if ($9 >0) print $0}' > /fs/home/card/Aung/ATM04/ATM04-Task29/infiles/fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0