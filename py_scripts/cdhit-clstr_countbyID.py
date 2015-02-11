"""
# parse cdhist_clstr_paser output into count by refID
# Input: #cluser id    #member1....#memberN
# usage: python cdhit-clstr_countbyID.py xxxCluster.stat
# output: #clusterid #Count of RefID #Count of Org_ID
# Dev: Aung
# Date: 10022015
"""
import sys
import re
import codesnippets
clstrfile = sys.argv[1]
clstrfile_read = open(clstrfile, 'r')
cluster_list = []
cluster_list = codesnippets.file_read_line(clstrfile_read)
Clst_stat =[]

for line in cluster_list:
    line_split = line.split("\t")
    if len(line_split) == 3:
        Clst_stat.append(line_split[0]+"\t"+"1"+"\t"+"1"+"\n")
    else:
        ref_count = 0;org_count = 0
        for x in line_split[1:]:
            ref_id = re.search(r'c\w+', x)
            org_id = re.search(r'>gi\|\w+', x)
            if ref_id:
                ref_count = ref_count+1
            if org_id:
                org_count = org_count+1
        Clst_stat.append(line_split[0]+"\t"+str(ref_count)+"\t"+str(org_count)+"\n")

codesnippets.write_file(Clst_stat,"{0}_Both_RefID_OrgID_Count".format(clstrfile))




