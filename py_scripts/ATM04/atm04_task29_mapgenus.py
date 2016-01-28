#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
atmidmapfile = sys.argv[1]
genus_list = sys.argv[2]
outputfile = sys.argv[3]

cap3_id = []
atm04_id = []
with open(atmidmapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')        
        atm04_id.append(l1_split[1])
        cap3_id.append(l1_split[2].strip('\n').strip('>'))

out_id = []
with open(outputfile,'rb') as f2:
    for l2 in f2:        
        out_id.append(l2.strip('\n').strip('>'))

with open(genus_list, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')        
        atm_id = l3_split[5]
        tmp = []
        for x in atm_id.split(';'):
            id_ = x.strip().strip('\n').strip('-XN')
            if id_ in out_id:
                tmp.append(x.strip().strip('\n'))
            elif 'CDF' in id_:
                indexes = [i for i,e in enumerate(cap3_id) if e == id_]
                for i in indexes:
                    if atm04_id[i] in out_id:
                        tmp.append(atm04_id[i].strip().strip('\n')+"-"+x.split('-')[2].strip().strip('\n'))
        if len(tmp) > 0:
            countx = 0
            countn = 0             
            uniq_tmp = list(set(tmp))
            for fin in uniq_tmp:
                if "-X" in fin:
                    countx += 1
                elif "-N" in fin:
                    countn += 1                        
            sys.stdout.write(l3_split[0]+ "\t" +l3_split[1]+"\t"+str(countn)+ "\t" +str(countx)+ "\t" + str(len(uniq_tmp))+"\t"+ ";".join(uniq_tmp)+'\n')

python atm04_mapgenus.py ../ATM04-Task29/infiles/atm04-cap3_contig_orgid.map infiles/A1/blastn-x.tophit.D output/id/atm04_fpkm_commom_D.id> output/catx/atm04_fpkm_commom_D_catx
python atm04_mapgenus.py ../ATM04-Task29/infiles/atm04-cap3_contig_orgid.map infiles/A1/blastn-x.tophit.E output/id/atm04_fpkm_commom_E.id> output/catx/atm04_fpkm_commom_E_catx
python atm04_mapgenus.py ../ATM04-Task29/infiles/atm04-cap3_contig_orgid.map infiles/A1/blastn-x.tophit.I6 output/id/atm04_fpkm_commom_I6.id> output/catx/atm04_fpkm_commom_I6_catx
python atm04_mapgenus.py ../ATM04-Task29/infiles/atm04-cap3_contig_orgid.map infiles/A1/blastn-x.tophit.I8 output/id/atm04_fpkm_commom_I8.id> output/catx/atm04_fpkm_commom_I8_catx