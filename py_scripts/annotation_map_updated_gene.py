#! /usr/bin/env python
"""
#--------------------------------------------------------------------------#
# mapp annotataion text file with sample specific text file
# Date: 9012015
# Usage: annotataion_map.py annotation.txt DE_Specific.tsv
# __author__ = 'Aung'
#--------------------------------------------------------------------------#
"""
import sys

usage = "Usage %s infile" % sys.argv[0]  # specific massage for no input

try:
    annotationfile = sys.argv[1]
    DEfile = sys.argv[2]
except:
    print usage, sys.exit(1)


def file_read(fileinput):
    temp_list = []
    for k in fileinput:
        temp_list.append(k)
    return temp_list

# open file read
annotationfile2 = open(annotationfile, 'r')
annotationfile_list = file_read(annotationfile2)
DEfile2 = open(DEfile, 'r')
DEFile_list = file_read(DEfile2)
DE_NotInAnnot = open("{0}_notinAnnot.txt".format(DEfile), 'w')
DE_Not = []

print "ID\tC\tM\tS\tCM\tCS\tMC\tMS\tSC\tSM\tC\tM\tS\tMS\tgene-id\tTranscript-id\t" \
      "sprot-Top-BLASTX-hit\tTrEMBL-Top-BLASTX-hit\tRNAMMER\tprot-id\tprot-coords\tsprot-Top-BLASTP-hit\t" \
      "TrEMBL-Top-BLASTP-hit\tPfam\tSignalP\tTmHMM\teggnog\tgene-ontology-blast\tgene-ontology-pfam\ttranscript\tpeptide"
for de_records in DEFile_list:
    de_split = de_records.split('\t')
    de_id = de_split[0].strip()  # either gene_id or transcript_id
    for annot_record in annotationfile_list:
        annot_split = annot_record.split('\t')
        annot_id = annot_split[0].strip()  # 1 for transcriptid and 0 for genes
        if de_id == annot_id:
            DE_Not.append(de_id)
            print de_records.strip('\n'),
            print '\t',
            for item in annot_split:
                if len(item) > 750:
                    print "{0}\t".format(item[0:750].strip()),
                else:
                    print "{0}\t".format(item.strip()),
            print "\n"

# write to file not in annotation
for de_records in DEFile_list:
    de_split = de_records.split('\t')
    de_id = de_split[0].strip()  # either gene_id or transcript_id
    if de_id not in DE_Not:
        DE_NotInAnnot.write(de_records)
