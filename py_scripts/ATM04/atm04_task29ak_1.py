#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
idlist = sys.argv[1]
maplist = sys.argv[2]
fpkmmatrix = sys.argv[3]

inter_id = []
atm_id = []
with open(maplist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        inter_id.append(l1_split[2].strip('\n').strip('>'))
        atm_id.append(l1_split[1])

final_idlist = []
with open(idlist,'rb') as f2:
    for l2 in f2:
        id = l2.split('\t')[0].strip()
        if "CDF" in id:
            indexes = [i for i,e in enumerate(inter_id) if e == id.strip()]
            for i in indexes:
                final_idlist.append(atm_id[i])
        else:
            final_idlist.append(id)

uniqid_list = list(set(final_idlist))

with open(fpkmmatrix,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        if l3_split[1] in uniqid_list:
            sys.stdout.write(l3)

python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.D.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.D.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.E.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.E.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.I6.sort infiles/atm04-cap3_contig_orgid.map  infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.I6.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.K.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.K.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.L.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.L.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.M.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.M.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.N.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.N.sort.fpkm
python atm04_29_1.py infiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.O.sort  infiles/atm04-cap3_contig_orgid.map infiles/task28_kallisto.matrix.final > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.O.sort.fpkm


python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.D.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.D.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.E.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.E.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.I6.sort.fpkm > summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.I6.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.K.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.K.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.L.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.L.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.M.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.M.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.N.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.N.sort.fpkm.contig
python atm04_29_2.py infiles/atm04-cap3_contig_orgid.map  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.O.sort.fpkm >  summaryfiles/fpkm_count_tmm_tmmnorm.matrix_16DIV.O.sort.fpkm.contig