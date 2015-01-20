#! /usr/bin/env python
#--------------------------------------------------------------------------#
# mapping annotation file with miratrinity_cdhit
# __author__ = 'atrx'
# usage: annot_miratrinity_map.py annotation.txt MiraTrinity_Member_all.txt
# Date: 14012015
#--------------------------------------------------------------------------#
import sys
import linecache
import re

usage= "Usage %s infile" % sys.argv[0] #specific massage for no input

try:
    annotationfile = sys.argv[1]
    tmfile = sys.argv[2]
except:
    print usage, sys.exit(1)

tmfile = open(tmfile,'r')
print "MIRA_ID\tCluster#\tTrinity_ID\tC\tM\tS\tCM\tCS\tMC\tMS\tSC\tSM\tC\tM\tS\tMS\tgene-id\tTranscript-id\tsprot-Top-BLASTX-hit\tTrEMBL-Top-BLASTX-hit\tRNAMMER\tprot-id\tprot-coords\tsprot-Top-BLASTP-hit\tTrEMBL-Top-BLASTP-hit\tPfam\tSignalP\tTmHMM\teggnog\tgene-ontology-blast\tgene-ontology-pfam\ttranscript\tpeptide"
for line in tmfile:
    cond1 = re.split(r'\t+',line)
    #  loop all mira,trinity ids from trinity_mirafile
    for tuple in cond1:
        annotationf = open(annotationfile,'r')
        # loop annotation file
        for annot in annotationf:
            annot_split = re.split(r'\t+', annot)
            annot_id = str(annot_split[1]) #trinitity_isoforms_id
            # compare all ids with annotaion_trinity_id
            tuple = tuple.replace('.','')
            if annot_id.strip() == tuple.strip():
                # loop MIRA_IDs and print it out with same trinity_id and Cluster_ID
                for tuple2 in cond1:
                    cond2 =re.search(r'c01_PM\w+',tuple2)
                    if cond2:
                        print cond2.group(), # Mira
                        print "\t",
                        print cond1[0], #Cluster
                        print "\t",
                        print annot # annotation
        else:
            annotationf.close()



