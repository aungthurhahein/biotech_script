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
# G3-A
# G3-N
# G2-31A
# G2-31N
# G2-32A
# G2-32N
# G2-21
# S2
# S1
G3A0 = []
G3A1 = []
G3A2 = []
G3A3 = []
G3A4 = []
G3A5 = []
G3A6 = []
G3A7 = []
G3A8 = []

G3N = []
G231A = []
G231N = []
G232A = []
G232N = []
G221 = []
S2 = []
S1 = []
else_multi = []
else_sing = []
for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    # multi
    if len(x_split) > 2:
        atm01 = re.search(r'>PV_ATM01\w+', x)
        nonatm01 = re.search(r'>PV_ATM02\w+', x)
        atm02 = re.search(r'>PV_ATM03\w+', x)
        nonatm02 = re.search(r'>PV_ATM04\w+', x)
        atm03 = re.search(r'>PV_ATM05\w+', x)
        if atm03 and nonatm01 and nonatm02 and atm01 and atm02:
            G3A0.append(x)
        elif atm03 and atm01 and nonatm01 and atm02:
            G3A1.append(x)
        elif atm03 and atm01 and nonatm01 and nonatm02:
            G3A2.append(x)
        elif atm03 and atm01 and atm02 and nonatm02:
            G3A3.append(x)
        elif atm03 and atm01 and atm02:
            G3A4.append(x)
        elif atm03 and atm01 and nonatm02:
            G3A5.append(x)
        elif atm03 and nonatm01 and atm02 and nonatm02:
            G3A6.append(x)
        elif atm03 and nonatm01 and atm02:
            G3A7.append(x)

        elif atm03 and nonatm01 and nonatm02:
            G3N.append(x)

        elif atm03 and (atm01 or nonatm01) and (atm02 or nonatm02):
            G3A8.append(x)


        elif atm03 and atm01 and nonatm01:
            G231A.append(x)
        elif atm03 and atm01:
            G231A.append(x)
        elif atm03 and nonatm01:
            G231N.append(x)

        elif atm03 and atm02 and nonatm02:
            G232A.append(x)
        elif atm03 and atm02:
            G232A.append(x)
        elif atm03 and nonatm02:
            G232N.append(x)

        elif atm01 and atm02 and nonatm01 and nonatm02:
            G221.append(x)
        elif atm03:
            S2.append(x)
        else:
            else_multi.append(x)

    # singleton
    else:
        atm03 = re.search(r'>PV_ATM05\w+', x)
        if atm03:
            S1.append(x)
        else:
            else_sing.append(x)

codesnippets.write_file(G3A0, "{0}_G3A0".format(clstrfile))
codesnippets.write_file(G3A1, "{0}_G3A1".format(clstrfile))
codesnippets.write_file(G3A2, "{0}_G3A2".format(clstrfile))
codesnippets.write_file(G3A3, "{0}_G3A3".format(clstrfile))
codesnippets.write_file(G3A4, "{0}_G3A4".format(clstrfile))
codesnippets.write_file(G3A5, "{0}_G3A5".format(clstrfile))
codesnippets.write_file(G3A6, "{0}_G3A6".format(clstrfile))
codesnippets.write_file(G3A7, "{0}_G3A7".format(clstrfile))
codesnippets.write_file(G3A8, "{0}_G3A8".format(clstrfile))

codesnippets.write_file(G3N, "{0}_G3N".format(clstrfile))
codesnippets.write_file(G221, "{0}_G221".format(clstrfile))
codesnippets.write_file(G231A, "{0}_G231A".format(clstrfile))
codesnippets.write_file(G231N, "{0}_G231N".format(clstrfile))
codesnippets.write_file(G232A, "{0}_G232A".format(clstrfile))
codesnippets.write_file(G232N, "{0}_G232N".format(clstrfile))
codesnippets.write_file(S2, "{0}_S2".format(clstrfile))
codesnippets.write_file(S1, "{0}_S1".format(clstrfile))
codesnippets.write_file(else_multi, "{0}_else_multi".format(clstrfile))
codesnippets.write_file(else_sing, "{0}_else_sing".format(clstrfile))
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_else_multi | awk -F '\t' '{print $1"\tElse-Multi"}' > clst.group
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_else_sing | awk -F '\t' '{print $1"\tElse-Sing"}' >> clst.group
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_G221 | awk -F '\t' '{print $1"\tG221"}' >> clst.group
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_G231A | awk -F '\t' '{print $1"\tG231A"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G231N | awk -F '\t' '{print $1"\tG231N"}' >> clst.group
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_G232N | awk -F '\t' '{print $1"\tG232N"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G232A | awk -F '\t' '{print $1"\tG232A"}' >> clst.group
#
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A0 | awk -F '\t' '{print $1"\tG3A0"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A1 | awk -F '\t' '{print $1"\tG3A1"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A2 | awk -F '\t' '{print $1"\tG3A2"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A3 | awk -F '\t' '{print $1"\tG3A3"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A4 | awk -F '\t' '{print $1"\tG3A4"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A5 | awk -F '\t' '{print $1"\tG3A5"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A6 | awk -F '\t' '{print $1"\tG3A6"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3A7 | awk -F '\t' '{print $1"\tG3A7"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_G3N | awk -F '\t' '{print $1"\tG3N"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_S1 | awk -F '\t' '{print $1"\tS1"}' >> clst.group
# cat ATM03-Task20-A.fasta_out.clstr.parse_S2 | awk -F '\t' '{print $1"\tS2"}' >> clst.group