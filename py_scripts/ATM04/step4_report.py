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
        atm_id = l2_split[6]
        sys.stdout.write(l2)
        for x in atm_id.split(';'):
            if x.strip().strip('\n').strip('-XN') in atmid:
                ind = atmid.index(x.strip().strip('\n').strip('-XN'))
                sys.stdout.write(fpkm_record[ind])
        sys.stdout.write('//\n')

# python step4_report.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand.D_gt0 fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand.D_gt0.fpkm
# python step4_report.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand.E_gt0 fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand.E_gt0.fpkm
# python step4_report.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand.I6_gt0 fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand.I6_gt0.fpkm
# python step4_report.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand.I8_gt0 fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand.I8_gt0.fpkm

python step4.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand2.D_gt0 ../fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand2.D_gt0.fpkm
python step4.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand2.E_gt0 ../fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand2.E_gt0.fpkm
python step4.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand2.I6_gt0 ../fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand2.I6_gt0.fpkm
python step4.py summaryfiles/blastn-x.tophit.querycatx.genus_count_expand2.I8_gt0 ../fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0 > blastn-x.tophit.querycatx.genus_count_expand2.I8_gt0.fpkm