"""
# parse cdhist_clstr_paser output into groups
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_classifer.py xxxCluster.stat.parse
# output: 5 files are written at line 45
# Dev: Aung
# Date: 10022015
"""
import sys
import re
import codesnippets

clstrfile = sys.argv[1]
clstrfile_read = open(clstrfile, 'r')
cluster_list = []
G2 = []
S2_04 = []
S2_ntu = []
S1_04 = []
S1_ntu = []
else_multi = []
else_sing = []

for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    # multi
    if len(x_split) > 2:
        atm04 = re.search(r'>PV_ATM06\w+', x)
        atmntu = re.search(r'>PV_ATM09\w+', x)
        if atm04 and atmntu:
            G2.append(x)                
        elif atm04:
            S2_04.append(x)
        elif atmntu:
            S2_ntu.append(x)        
        else:
            else_multi.append(x)
    
    # singleton
    else:
        atm04 = re.search(r'>PV_ATM06\w+', x)
        atmntu = re.search(r'>PV_ATM09\w+', x)
        if atm04:
            S1_04.append(x)
        elif atmntu:
            S1_ntu.append(x)
        else:
            else_sing.append(x)

codesnippets.write_file(G2, "{0}_G2".format(clstrfile))
codesnippets.write_file(S2_04, "{0}_S2_04".format(clstrfile))
codesnippets.write_file(S2_ntu, "{0}_S2_NTU".format(clstrfile))
codesnippets.write_file(S1_04, "{0}_S1_04".format(clstrfile))
codesnippets.write_file(S1_ntu, "{0}_S1_NTU".format(clstrfile))
codesnippets.write_file(else_multi, "{0}_else_multi".format(clstrfile))
codesnippets.write_file(else_sing, "{0}_else_sing".format(clstrfile))




