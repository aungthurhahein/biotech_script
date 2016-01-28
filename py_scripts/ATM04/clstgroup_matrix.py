#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
clstgroupfile = sys.argv[1]
allclstmem = sys.argv[2]
atmlenlst = sys.argv[3]

clst = []
group = []
with open(clstgroupfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        clst.append(l1_split[0].strip('>').strip())
        group.append(l1_split[1].strip('\n'))

atmid = []
atmlen = []
with open(atmlenlst, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        atmid.append(l3_split[0].strip().strip('>').strip('\n'))
        atmlen.append(l3_split[1].strip('\n'))

with open(allclstmem,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        clstid = l2_split[0].strip('>').strip()
        # clstmem.append(l2_split[1:])
        if clstid in clst:
            ind = clst.index(clstid)
            for m in l2_split[1:]:
                m = m.strip().strip('>').strip('\n')
                if m in atmid:
                    ind2 = atmid.index(m)
                    idlen = atmlen[ind2]
                    sys.stdout.write(m+'\t'+idlen+'\t'+group[ind]+'\t'+clstid+'\n')

# python get_atm04clstgroup.matrix.py atm04_clst.group ../ATM0425A.fasta_out.clstr.parse2 ../../ATM04-Task25A.fasta_lngth
#
# python clst_groups/get_atm04clstgroup.matrix.py atm04_clst.group ATM0425A.fasta_out.clstr.parse2 ../ATM04-Task25A.fasta_lngth


python /fs/home/card/bin/trinity_withotherassembly.py -s SRR839222.Trinity_PE -a ILT23 -i PV_ILT23
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037362.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037365.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR842625.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR839236.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037363.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s  SRR842627.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037366.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR842572.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037364.Trinity_PE
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1039534.Trinity_PE