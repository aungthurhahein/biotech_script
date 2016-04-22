# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-09 13:35:45
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-14 12:18:14

import sys
mapfile = sys.argv[1]
specieslist = sys.argv[2]
infile = sys.argv[3]

cap_id = []
atm_id = []
with open(mapfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        cap_id.append(l1_split[2].strip('\n').strip('>'))
        atm_id.append(l1_split[1])

xn_list = []
catx_list = []
cap3_list = []
with open(specieslist,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        id_ = l2_split[0].strip()
        if "CDF" in id_:
            indexes = [i for i,e in enumerate(cap_id) if e == id_.strip()]
            for i in indexes:                
                cap3_list.append(atm_id[i])
                catx_list.append(l2_split[1])
                xn_list.append(l2_split[2])
        else:
            cap3_list.append(id_)
            catx_list.append(l2_split[1])
            xn_list.append(l2_split[2])

with open(infile,'rb') as f3:
    for l3 in f3:
        if '>' in l3:            
            id_ = l3.strip('>').strip('\n')
            tmp = id_
            if id_ in cap3_list:
                indx = cap3_list.index(id_)
                catx = catx_list[indx]
                nx = xn_list[indx]
            else:
                catx = "-"
                nx="-"
        elif l3.split('\t')[0] == "RSEM":
            l3_split = l3.split('\t')
            # print l3_split            
            if id_ in atm_id:
                ind = atm_id.index(id_)
                tmp +="\t"+cap_id[ind]
            else:
                tmp +="\t"+id_
            if float(l3_split[8]) == 0:
                div = "ATMOnly"
            else:
                div = str(float(l3_split[7])/float(l3_split[8]))
            tmp += "\t"+l3_split[7]+"\t"+l3_split[8]+"\t"+div
        elif l3.split('\t')[0] == "KALS":
            l3_split = l3.split('\t')
            if float(l3_split[8]) == 0:
                div = "ATMOnly"
            else:
                div = str(float(l3_split[7])/float(l3_split[8]))
            tmp += "\t"+l3_split[7]+"\t"+l3_split[8]+"\t"+div+"\t"+catx+"\t"+nx
            sys.stdout.write(tmp+'\n')

# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.D > atm04_common_kallisto_rsem.D.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.E > atm04_common_kallisto_rsem.E.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.F > atm04_common_kallisto_rsem.F.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.G > atm04_common_kallisto_rsem.G.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.I1 > atm04_common_kallisto_rsem.I1.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.I2 > atm04_common_kallisto_rsem.I2.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.I4 > atm04_common_kallisto_rsem.I4.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.I6 > atm04_common_kallisto_rsem.I6.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.I7 > atm04_common_kallisto_rsem.I7.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.K > atm04_common_kallisto_rsem.K.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.L > atm04_common_kallisto_rsem.L.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.M > atm04_common_kallisto_rsem.M.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.matrix > atm04_common_kallisto_rsem.matrix.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.N > atm04_common_kallisto_rsem.N.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.O > atm04_common_kallisto_rsem.O.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.P > atm04_common_kallisto_rsem.P.fmt
# python atm04-32AB.py atm04-cap3_contig_orgid.map blastn-x.tophit.querycatx_16DIV.species atm04_common_kallisto_rsem.U > atm04_common_kallisto_rsem.U.fmt
