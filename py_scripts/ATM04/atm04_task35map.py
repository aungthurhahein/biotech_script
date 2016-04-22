# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-14 10:50:30
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-14 15:03:15
import sys
mapfile = sys.argv[1]
rsemdefile = sys.argv[2]
kaldefile = sys.argv[3]
specieslist = sys.argv[4]
infile = sys.argv[5]

cap_id = []
atm_id = []
with open(mapfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        cap_id.append(l2_split[2].strip('\n').strip('>'))
        atm_id.append(l2_split[1])

rsem_astranid = []
rsem_atm = []
rsem_nonatm = []
with open(rsemdefile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        rsem_astranid.append(l1_split[1])
        rsem_atm.append(l1_split[6])
        rsem_nonatm.append(l1_split[7])

kal_astranid = []
kal_atm = []
kal_nonatm = []
with open(kaldefile,'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        kal_astranid.append(l3_split[1])
        kal_atm.append(l3_split[6])
        kal_nonatm.append(l3_split[7])        

xn_list = []
catx_list = []
cap3_list = []
with open(specieslist,'rb') as f5:
    for l5 in f5:
        l5_split = l5.split('\t')
        id_ = l5_split[0].strip()
        if "CDF" in id_:
            indexes = [i for i,e in enumerate(cap_id) if e == id_.strip()]
            for i in indexes:                
                cap3_list.append(atm_id[i])
                catx_list.append(l5_split[1])
                xn_list.append(l5_split[2])
        else:
            cap3_list.append(id_)
            catx_list.append(l5_split[1])
            xn_list.append(l5_split[2])

def get_record(id_):
    tmp = id_
    if id_ in atm_id:
        ind = atm_id.index(id_)
        tmp +="\t"+cap_id[ind]
    else:
        tmp +="\t"+id_
    if id_ in rsem_astranid:
        ind = rsem_astranid.index(id_)        
        tmp += "\t"+rsem_atm[ind]+"\t"+rsem_nonatm[ind]
        if float(rsem_nonatm[ind]) == 0:
            div2 = "ATMOnly"
        else:
            div2 = str(float(rsem_atm[ind])/float(rsem_nonatm[ind]))
        tmp += "\t"+div2
    else:
        tmp += "\t-\t-\t-"

    if id_ in kal_astranid:
        ind = kal_astranid.index(id_)        
        tmp += "\t"+kal_atm[ind]+"\t"+kal_nonatm[ind]
        if float(kal_nonatm[ind]) == 0:
            div = "ATMOnly"
        else:
            div = str(float(kal_atm[ind])/float(kal_nonatm[ind]))
        tmp += "\t"+div        
    else:
        tmp += "\t-\t-\t-"
    if id_ in cap3_list:
        indx = cap3_list.index(id_)
        catx = catx_list[indx]
        nx = xn_list[indx]
    else:
        catx = "-"
        nx="-"
    tmp +="\t"+catx+"\t"+nx
    return tmp
with open(infile,'rb') as f4:
    for l4 in f4:
        id_ = l4.strip('\n')
        if "CDF" in id_:
            indexes = [i for i,e in enumerate(cap_id) if e == id_.strip()]
            for i in indexes:                
                sys.stdout.write(get_record(atm_id[i])+"\n")
        else:
            sys.stdout.write(get_record(id_)+"\n")


# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/D.comm.notpass > D.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/E.comm.notpass > E.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/F.comm.notpass > F.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/G.comm.notpass > G.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/I1.comm.notpass > I1.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/I2.comm.notpass > I2.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/I4.comm.notpass > I4.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/I6.comm.notpass > I6.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/I7.comm.notpass > I7.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/K.comm.notpass > K.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/L.comm.notpass > L.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/M.comm.notpass > M.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/N.comm.notpass > N.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/noblast.comm.notpass > noblast.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/O.comm.notpass > O.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/P.comm.notpass > P.comm.notpass.fmt
# python atm04_task35.py infiles/atm04-cap3_contig_orgid.map infiles/fpkm_count_tmm_tmmnorm.matrix infiles/task28_kallisto.matrix.final infiles/blastn-x.tophit.querycatx_16DIV.species notpass_EK/U.comm.notpass > U.comm.notpass.fmt


# python update11.py D.comm.notpass.fmt > D.comm.notpass.fmt.grpa
# python update11.py E.comm.notpass.fmt > E.comm.notpass.fmt.grpa
# python update11.py F.comm.notpass.fmt > F.comm.notpass.fmt.grpa
# python update11.py G.comm.notpass.fmt > G.comm.notpass.fmt.grpa
# python update11.py I1.comm.notpass.fmt > I1.comm.notpass.fmt.grpa
# python update11.py I2.comm.notpass.fmt > I2.comm.notpass.fmt.grpa
# python update11.py I4.comm.notpass.fmt > I4.comm.notpass.fmt.grpa
# python update11.py I6.comm.notpass.fmt > I6.comm.notpass.fmt.grpa
# python update11.py I7.comm.notpass.fmt > I7.comm.notpass.fmt.grpa
# python update11.py K.comm.notpass.fmt > K.comm.notpass.fmt.grpa
# python update11.py L.comm.notpass.fmt > L.comm.notpass.fmt.grpa
# python update11.py M.comm.notpass.fmt > M.comm.notpass.fmt.grpa
# python update11.py N.comm.notpass.fmt > N.comm.notpass.fmt.grpa
# python update11.py noblast.comm.notpass.fmt > noblast.comm.notpass.fmt.grpa
# python update11.py O.comm.notpass.fmt > O.comm.notpass.fmt.grpa
# python update11.py P.comm.notpass.fmt > P.comm.notpass.fmt.grpa
# python update11.py U.comm.notpass.fmt > U.comm.notpass.fmt.grpa