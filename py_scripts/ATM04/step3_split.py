#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
genuscount = sys.argv[1]
gt0file = sys.argv[2]

atm_id = []
with open(gt0file,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')        
        atm_id.append(l1_split[1])

o1 = open(genuscount+'_gt0','w')
o2 = open(genuscount+'_lte0','w')
with open(genuscount,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        tmp_gt0 = ""
        tmp_lte0 = ""   
        for x in l2_split[6].split(';'):
            if x.strip('-XN').strip() in atm_id:
                if tmp_gt0 == "":
                    tmp_gt0 = x.strip()
                else:
                    tmp_gt0 += ";"+ x.strip()
            else:
                if tmp_lte0 == "":
                    tmp_lte0 = x.strip()
                else:
                    tmp_lte0 += ";"+ x.strip()
        if tmp_gt0 != "":
            o1.write(l2_split[0]+'\t'+l2_split[1]+'\t'+l2_split[2]+'\t'+l2_split[3]+'\t'+l2_split[4]+'\t'+l2_split[5]+'\t'+tmp_gt0+'\n')
        if tmp_lte0 != "":
            o2.write(l2_split[0]+'\t'+l2_split[1]+'\t'+l2_split[2]+'\t'+l2_split[3]+'\t'+l2_split[4]+'\t'+l2_split[5]+'\t'+tmp_lte0+'\n')

# python step3_split.py blastn-x.tophit.querycatx.genus_count_expand.D fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0
# python step3_split.py blastn-x.tophit.querycatx.genus_count_expand.E fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0
# python step3_split.py blastn-x.tophit.querycatx.genus_count_expand.I6 fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0
# python step3_split.py blastn-x.tophit.querycatx.genus_count_expand.I8 fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0

python step3.py blastn-x.tophit.querycatx.genus_count_expand2.D ../fpkm_count_tmm_tmmnorm.matrix.D.sort.gt0
python step3.py blastn-x.tophit.querycatx.genus_count_expand2.E ../fpkm_count_tmm_tmmnorm.matrix.E.sort.gt0
python step3.py blastn-x.tophit.querycatx.genus_count_expand2.I6 ../fpkm_count_tmm_tmmnorm.matrix.I6.sort.gt0
python step3.py blastn-x.tophit.querycatx.genus_count_expand2.I8 ../fpkm_count_tmm_tmmnorm.matrix.I8.sort.gt0
