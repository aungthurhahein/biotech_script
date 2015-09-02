"""
# parse cdhist_clstr_paser output into groups
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_countbyID.py xxxCluster.stat xxxInput.fasta  ClstrIDs_in_this_format "1,2,..n"
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
clstrid_read = open(clstrid, 'r') # by file
clstr_list = []
clstr_id = []
org_seqid = []
org_sequence = []

clstr_list = codesnippets.file_read_line(clstrfile_read)
clstr_id = codesnippets.file_read_line(clstrid_read)  # by file

# clstr_id = clstrid.split(',')
for seq_record in SeqIO.parse(fastafile, "fasta"):
    org_seqid.append(seq_record.id.strip())
    org_sequence.append(seq_record.seq.strip())

for clstrid in clstr_id:
    # clstrid = ">Cluster {0}".format(clstrid) # not necessary for ID file input
    for x in clstr_list:
        x_split = x.split('\t')
        if clstrid.strip() == x_split[0].strip():
            for clst_mem in x_split[1:]:
                if clst_mem.strip('>').strip() in org_seqid:
                        ind = org_seqid.index(clst_mem.strip('>').strip())
                        print ">" + org_seqid[ind]
                        print org_sequence[ind]


