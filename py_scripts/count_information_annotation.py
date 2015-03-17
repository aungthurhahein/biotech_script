#! /usr/bin/env python
"""
# --------------------------------------------------------------------------#
# count information
# Date: 9012015
# Usage: annotataion_map.py
# __author__ = 'Aung ေအာင်သူရဟိန်း'
#--------------------------------------------------------------------------#
"""
import sys
import linecache

file1 = "/home/aung/server_downloads/c01_MIRA_DE/T1_DE.txt"
file2 = "/home/aung/server_downloads/c01_MIRA_DE/c01MIRA_AnnotationTransfer.tsv"
file3 = "/home/aung/server_downloads/c01_MIRA_CDHIT/mira_org_trinity.txt"
file_read = open(file1, 'r')
file2_read = open(file2, 'r')
file3_read = open(file3, 'r')
# result_clst=[];result_id=[];result_count=[];
DE_file = [];
Annotation_file = [];
mira_org = [];
mira_trinity = [];

for i in file_read:
    DE_file.append(i)
for j in file2_read:
    Annotation_file.append(j)
for k in file3_read:
    k_split = k.split('\t')
    trinity_tempid = k_split[1].split()
    mira_org.append(k_split[0].strip())
    mira_trinity.append(trinity_tempid[0].strip('>'))

for de_line in DE_file:
    de_split = de_line.split('\t')
    de_trans = de_split[0].strip()
    if de_trans in mira_trinity:
        tempindex = mira_trinity.index(de_trans)
        mira_org_id = mira_org[tempindex].strip()
    else:
        mira_org_id = "null"
    # print mira_org_id
    for annot_line in Annotation_file:
        annot_split = annot_line.split('\t')
        annot_trans = annot_split[0].strip('>')
        # print mira_org_id.strip('>'),annot_trans.strip()
        if mira_org_id.strip('>') == annot_trans.strip():
            print de_line.strip('\n'), '\t', annot_line


        #
        # for miraline in MIRA_file:
        #     mira_split = miraline.split('\t')
        #     for line in Trinity_file:
        #         trinity_split = line.split()
        #         trinity_cluster= trinity_split[0]+" "+trinity_split[1]
        #         if mira_split[0].strip() == trinity_cluster.strip():
        #             print "{0}\t{1}".format(miraline.strip(), line.strip())

        #Trinity maps with annotation
        # for i in file_read:
        #     Trinity_file.append(i)
        # for j in file2_read:
        #     Trinotate_file.append(j)
        #
        # for line in Trinity_file:
        #     trinity_split = line.split()
        #     for trinotate in Trinotate_file:
        #         trinotate_split = trinotate.split('\t')
        #         if trinity_split[2].strip() == trinotate_split[1].strip():
        #             print trinity_split[0],trinity_split[1],
        #             for x in trinotate_split:
        #                 if len(x) > 750:
        #                     print "{0}\t".format(x[0:750].strip()),
        #                 else:
        #                     print "{0}\t".format(x.strip()),
        #             print '\n'

        #
        # # 2cdhit-> 1stcdhit
        # for i in file_read:
        #   MIRAmapped32.append(i)
        # for j in file2_read:
        #     MIRAFirst.append(j)
        #
        # for id in MIRAFirst:
        #     mira_id= id.strip()
        #     for line in MIRAmapped32:
        #         line_split = line.split('\t')
        #         if line_split[3].strip() == mira_id:
        #             print line.strip('\n'),"\t",
        #             print mira_id

        # 3cdhit-->2cdhit
        # print "3CDHIT_ClstrID 3CDHIT_ID 2CDHIT_ClstrID 2CDHIT_ID"
        # for mira_line in Mirasplit_list:
        #     mira_split = mira_line.split()
        #     mira_id =mira_split[2].strip()
        #     for clst in cluster_list:
        #         clst_split = clst.split()
        #         for member in clst_split:
        #             if member.strip('>') == mira_id:
        #                 for res in range(2,len(clst_split)):
        #                     print mira_split[0],mira_split[1],"\t", #3rd MIRA ID
        #                     print mira_id,"\t",
        #                     print clst_split[0],clst_split[1],"\t",
        #                     print clst_split[res]


        #
        # for clst_line in cluster_list:
        #     if ">Cluster" in clst_line:
        #         print '\n'
        #         print clst_line.strip(),"\t",
        #     else:
        #         clst_split = clst_line.split()
        #         print clst_split[2].strip("."),"\t",


        #
        # for line in file_list:
        #     line_split=line.split()
        #     cluster= line_split[1]
        #     id = line_split[2]
        #     count = line_split[3]
        #     check_clst="'{0}'".format(cluster)
        #
        #     if str(cluster) in result_clst:
        #         temp_index=result_clst.index(cluster)
        #         temp_id =result_id[temp_index]
        #         temp_count = result_count[temp_index]
        #         if count < temp_count:
        #             result_id[temp_index]= id
        #             result_count[temp_index] = count
        #     else:
        #         result_clst.append(cluster)
        #         result_id.append(id)
        #         result_count.append(count)
        #
        # for i in range(0,len(result_clst)):
        #     print ">Cluster ",result_clst[i],"\t",
        #     print result_id[i],"\t",
        #     print result_count[i]



        # for line in file2_list:
        #   line_split= line.split()
        #   trans_id =line_split[2].strip()
        #   trans_cluster = line_split[0]+" "+line_split[1]
        #   for x in file_list:
        #       x_split= x.split()
        #       if x_split[0] == trans_id:
        #         print trans_cluster,
        #         print trans_id,
        #         print x_split[1]

        #
        # count = 0
        # for i in line_split:
        #     if i==".":
        #         count=count+1
        # print line_split[1],'\t',count

