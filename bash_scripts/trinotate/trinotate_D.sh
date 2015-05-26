#!/bin/bash
trinotate_home="/fs/home/card/hasan/Trinotate_r20140708"

# Generate Report
echo "#########################"
echo "Generating Annotation Report"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite report > trinotate_annotation_report.xls

echo "#########################"
echo "Trinotate Report generation done"
echo "#########################"

# Column Info
#0       #gene_id
#1       transcript_id
#2       Top_BLASTX_hit
#3       RNAMMER
#4       prot_id
#5       prot_coords
#6       Top_BLASTP_hit
#7       Pfam
#8       SignalP
#9       TmHMM
#10      eggnog
#11      gene_ontology
