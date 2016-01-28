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

G4A1 = []
G4A2 = []
G4A3 = []
G4A4 = []
G4A5 = []
G4A6 = []
G4A7 = []
G4A8 = []
G4N = []

G3A1 = []
G3A2 = []
G3A3 = []
G3A4 = []
G3A5 = []
G3A6 = []
G3A7 = []
G3A8 = []
G3A9 = []
G3A10 = []
G3A11 = []
G3A12 = []
G3N1 = []
G3N2 = []
G3N3 = []

G2A1 = []
G2A2 = []
G2A3 = []
G2A4 = []
G2N1 = []
G2N2 = []

G23 = []

for line in clstrfile_read:
    cluster_list.append(line.strip())

for x in cluster_list:
    x_split = x.split('\t')
    clstid = x_split[0]
    atm04 = int(x_split[1])
    atm03 = int(x_split[2])
    nonatm02 = int(x_split[3])
    atm02 = int(x_split[4])
    nonatm01 = int(x_split[5])
    atm01 = int(x_split[6].strip('\n'))

    if atm04 == 0:
        atm04 = 0
    else:
        atm04 = 1

    if atm03 == 0:
        atm03 = 0
    else:
        atm03 = 1

    if nonatm02 == 0:
        nonatm02 = 0
    else:
        nonatm02 = 1

    if atm02 == 0:
        atm02 = 0
    else:
        atm02 = 1

    if nonatm01 == 0:
        nonatm01 = 0
    else:
        nonatm01 = 1

    if atm01 == 0:
        atm01 = 0
    else:
        atm01 = 1


    # G4
    if atm04 and atm03 and nonatm01 and nonatm02 and atm01 and atm02:
        G4A1.append(x)
    elif atm04 and atm03 and atm01 and nonatm01 and atm02:
        G4A2.append(x)
    elif atm04 and atm03 and atm01 and nonatm01 and nonatm02:
        G4A3.append(x)
    elif atm04 and atm03 and atm01 and atm02 and nonatm02:
        G4A4.append(x)
    elif atm04 and atm03 and atm01 and atm02:
        G4A5.append(x)
    elif atm04 and atm03 and atm01 and nonatm02:
        G4A6.append(x)
    elif atm04 and atm03 and nonatm01 and atm02 and nonatm02:
        G4A7.append(x)
    elif atm04 and atm03 and nonatm01 and atm02:
        G4A8.append(x)

    elif atm04 and atm03 and nonatm01 and nonatm02:
        G4N.append(x)

    #G3
    elif atm04 and atm03 and atm01 and nonatm01:
        G3A1.append(x)
    elif atm04 and atm03 and atm01:
        G3A2.append(x)

    elif atm04 and atm03 and atm02 and nonatm02:
        G3A3.append(x)
    elif atm04 and atm03 and atm02:
        G3A4.append(x)

    elif atm04 and nonatm01 and nonatm02 and atm01 and atm02:
        G3A5.append(x)
    elif atm04 and atm01 and nonatm01 and atm02:
        G3A6.append(x)
    elif atm04 and atm01 and nonatm01 and nonatm02:
        G3A7.append(x)

    elif atm04 and atm01 and atm02 and nonatm02:
        G3A8.append(x)
    elif atm04 and atm01 and atm02:
        G3A9.append(x)
    elif atm04 and atm01 and nonatm02:
        G3A10.append(x)

    elif atm04 and nonatm01 and atm02 and nonatm02:
        G3A11.append(x)

    elif atm04 and atm02 and nonatm01:
        G3A12.append(x)

    elif atm04 and nonatm01 and nonatm02:
        G3N1.append(x)
    elif atm04 and atm03 and nonatm01:
        G3N2.append(x)
    elif atm04 and atm03 and nonatm02:
        G3N3.append(x)

    #G2
    elif atm04 and atm01 and nonatm01:
        G2A1.append(x)

    elif atm04 and atm01:
        G2A2.append(x)

    elif atm04 and atm02 and nonatm02:
        G2A3.append(x)
    elif atm04 and atm02:
        G2A4.append(x)

    elif atm04 and nonatm01:
        G2N1.append(x)

    elif atm04 and nonatm02:
        G2N2.append(x)
    # G3
    elif atm04 and atm03:
        G23.append(x)
    else:
        print x

codesnippets.write_file(G4A1, "{0}_G4A1".format(clstrfile))
codesnippets.write_file(G4A2, "{0}_G4A2".format(clstrfile))
codesnippets.write_file(G4A3, "{0}_G4A3".format(clstrfile))
codesnippets.write_file(G4A4, "{0}_G4A4".format(clstrfile))
codesnippets.write_file(G4A5, "{0}_G4A5".format(clstrfile))
codesnippets.write_file(G4A6, "{0}_G4A6".format(clstrfile))
codesnippets.write_file(G4A7, "{0}_G4A7".format(clstrfile))
codesnippets.write_file(G4A8, "{0}_G4A8".format(clstrfile))
codesnippets.write_file(G4N, "{0}_G4N".format(clstrfile))

codesnippets.write_file(G3A1, "{0}_G3A1".format(clstrfile))
codesnippets.write_file(G3A2, "{0}_G3A2".format(clstrfile))
codesnippets.write_file(G3A3, "{0}_G3A3".format(clstrfile))
codesnippets.write_file(G3A4, "{0}_G3A4".format(clstrfile))
codesnippets.write_file(G3A5, "{0}_G3A5".format(clstrfile))
codesnippets.write_file(G3A6, "{0}_G3A6".format(clstrfile))
codesnippets.write_file(G3A7, "{0}_G3A7".format(clstrfile))
codesnippets.write_file(G3A8, "{0}_G3A8".format(clstrfile))
codesnippets.write_file(G3A9, "{0}_G3A9".format(clstrfile))
codesnippets.write_file(G3A10, "{0}_G3A10".format(clstrfile))
codesnippets.write_file(G3A11, "{0}_G3A11".format(clstrfile))
codesnippets.write_file(G3A12, "{0}_G3A12".format(clstrfile))

codesnippets.write_file(G3N1, "{0}_G3N1".format(clstrfile))
codesnippets.write_file(G3N2, "{0}_G3N2".format(clstrfile))
codesnippets.write_file(G3N3, "{0}_G3N3".format(clstrfile))

codesnippets.write_file(G2A1, "{0}_G2A1".format(clstrfile))
codesnippets.write_file(G2A2, "{0}_G2A2".format(clstrfile))
codesnippets.write_file(G2A3, "{0}_G2A3".format(clstrfile))
codesnippets.write_file(G2A4, "{0}_G2A4".format(clstrfile))
codesnippets.write_file(G2N1, "{0}_G2N1".format(clstrfile))
codesnippets.write_file(G2N2, "{0}_G2N2".format(clstrfile))
codesnippets.write_file(G23, "{0}_G23".format(clstrfile))

#
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A2 | awk -F '\t' '{print $1"\tG3A2"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A2 | awk -F '\t' '{print $1"\tG4A2"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G23 | awk -F '\t' '{print $1"\tG23"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A3| awk -F '\t' '{print $1"\tG3A3"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A3| awk -F '\t' '{print $1"\tG4A3"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2A1| awk -F '\t' '{print $1"\tG2A1"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A4| awk -F '\t' '{print $1"\tG3A4"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A4| awk -F '\t' '{print $1"\tG4A4"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2A2| awk -F '\t' '{print $1"\tG2A2"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A5| awk -F '\t' '{print $1"\tG3A5"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A5| awk -F '\t' '{print $1"\tG4A5"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2A3| awk -F '\t' '{print $1"\tG2A3"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A6| awk -F '\t' '{print $1"\tG3A6"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A6| awk -F '\t' '{print $1"\tG4A6"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2A4| awk -F '\t' '{print $1"\tG2A4"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A7| awk -F '\t' '{print $1"\tG3A7"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A7| awk -F '\t' '{print $1"\tG4A7"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2N1| awk -F '\t' '{print $1"\tG2N1"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A8| awk -F '\t' '{print $1"\tG3A8"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A8| awk -F '\t' '{print $1"\tG4A8"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G2N2| awk -F '\t' '{print $1"\tG2N2"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A9| awk -F '\t' '{print $1"\tG3A9"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4N| awk -F '\t' '{print $1"\tG4N"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A1| awk -F '\t' '{print $1"\tG3A1"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3N1| awk -F '\t' '{print $1"\tG3N1"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A10| awk -F '\t' '{print $1"\tG3A10"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3N2| awk -F '\t' '{print $1"\tG3N2"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A11| awk -F '\t' '{print $1"\tG3A11"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3N3| awk -F '\t' '{print $1"\tG3N3"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G3A12| awk -F '\t' '{print $1"\tG3A12"}' >> atm04_clst.group
# cat atm04_clustercountExpend_withATM03-Task20B.matrix_G4A1| awk -F '\t' '{print $1"\tG4A1"}' >> atm04_clst.group

# cat ATM0425A.fasta_out.clstr.parse2_multi| awk -F '\t' '{print $1"\tS2"}' >> atm04_clst.group
# cat ATM0425A.fasta_out.clstr.parse2_singleton| awk -F '\t' '{print $1"\tS1"}' >> atm04_clst.group

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
