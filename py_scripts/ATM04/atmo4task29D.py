#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
gtfile = sys.argv[1]
fpkmfile = sys.argv[2]
atmidmapfile = sys.argv[3]

cap3_id = []
atm04_id = []
with open(atmidmapfile,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')        
        atm04_id.append(l3_split[1])
        cap3_id.append(l3_split[2].strip('\n').strip('>'))

atmid = []
fpkm_record = []
with open(fpkmfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        atmid.append(l1_split[1])   
        fpkm_record.append(l1)

with open(gtfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')        
        atm_id = l2_split[5]
        sys.stdout.write(l2)
        for x in atm_id.split(';'):
            if x.strip().strip('\n').strip('-XN') in atmid:
                ind = atmid.index(x.strip().strip('\n').strip('-XN'))
                sys.stdout.write(fpkm_record[ind])
            elif x.strip().strip('\n').strip('-XN') in cap3_id:
                indexes = [i for i,e in enumerate(cap3_id) if e == x.strip().strip('\n').strip('-XN')]
                for i in indexes:
                    ind = atmid.index(atm04_id[i])
                    sys.stdout.write(fpkm_record[ind].strip('\n')+'\t'+x.strip().strip('\n').strip('-XN')+'\n')
        sys.stdout.write('//\n')

# python atm04task29D.py blastn-x.tophit.querycatx.genus_count_expand2.D_gt0.flt ../ATM04-Task29B/fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0 atm04-cap3_contig_orgid.map > blastn-x.tophit.querycatx.genus_count_expand2.D_gt0.flt.fpkm
# python atm04task29D.py blastn-x.tophit.querycatx.genus_count_expand2.E_gt0.flt ../ATM04-Task29B/fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0 atm04-cap3_contig_orgid.map > blastn-x.tophit.querycatx.genus_count_expand2.E_gt0.flt.fpkm
# python atm04task29D.py blastn-x.tophit.querycatx.genus_count_expand2.I6_gt0.flt ../ATM04-Task29B/fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0 atm04-cap3_contig_orgid.map > blastn-x.tophit.querycatx.genus_count_expand2.I6_gt0.flt.fpkm
# python atm04task29D.py blastn-x.tophit.querycatx.genus_count_expand2.I8_gt0.flt ../ATM04-Task29B/fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0 atm04-cap3_contig_orgid.map > blastn-x.tophit.querycatx.genus_count_expand2.I8_gt0.lft.fpkm