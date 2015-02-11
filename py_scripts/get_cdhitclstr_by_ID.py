"""
# parse cdhist_clstr_paser output into groups
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_countbyID.py xxxCluster.stat xxxInput.fasta ClstrID(1,2,..n)
# output: #clusterid #Count of RefID #Count of Org_ID
# Dev: Aung
# Date: 10022015
"""
import sys
from Bio import SeqIO
import codesnippets

clstrfile = sys.argv[1]
fastafile = sys.argv[2]
clstrid = sys.argv[3]
clstrfile_read = open(clstrfile, 'r')
clstr_list = []
clstr_id = []

clstr_list = codesnippets.file_read_line(clstrfile_read)
clstr_id = clstrid.split(',')

for clstrid in clstr_id:
    clstrid = ">Cluster {0}".format(clstrid)
    for x in clstr_list:
        x_split = x.split('\t')
        if clstrid.strip() == x_split[0].strip():
            for clst_mem in x_split[1:]:
                for seq_record in SeqIO.parse(fastafile, "fasta"):
                    if seq_record.id.strip() == clst_mem.strip('>').strip():
                        print ">"+seq_record.id
                        print seq_record.seq


