#!/bin/bash
trinity_home="/share/apps/trinityrnaseq_r20140717"
sqlite_db="Trinotate.sqlite"

#################################################################
## Load Expression info and DE analysis results for Trinotate-web
#################################################################


# import the expression data (counts, fpkms, and samples)

echo "###################################"
echo Loading Component Expression Matrix
echo "###################################"

$trinity_home/util/transcript_expression/import_samples_n_expression_matrix.pl --sqlite ${sqlite_db} --component_mode --samples_file samples_n_reads_described.txt --count_matrix Trinity_components.counts.matrix --fpkm_matrix Trinity_components.counts.matrix.TMM_normalized.FPKM --bulk_load


echo "###################################"
echo Loading Transcript Expression Matrix
echo "###################################"

$trinity_home/util/transcript_expression/import_samples_n_expression_matrix.pl --sqlite ${sqlite_db} --transcript_mode --samples_file samples_n_reads_described.txt --count_matrix Trinity_trans.counts.matrix --fpkm_matrix Trinity_trans.counts.matrix.TMM_normalized.FPKM --bulk_load


# import the DE analysis results:

echo "###########################"
echo Loading DE results for transcripts
echo "###########################"

$trinity_home/util/transcript_expression/import_DE_results.pl --sqlite ${sqlite_db} --DE_dir edgeR_trans --transcript_mode --bulk_load


echo "###########################"
echo Loading DE results for components
echo "###########################"


$trinity_home/util/transcript_expression/import_DE_results.pl --sqlite ${sqlite_db} --DE_dir edgeR_components --component_mode --bulk_load

echo "######################################################"
echo Loading transcription profile clusters for transcripts
echo "######################################################"


# import the transcription profile cluster stuff
$trinity_home/util/transcript_expression/import_transcript_clusters.pl --group_name DE_all_vs_all --analysis_name edgeR_trans/diffExpr.P0.001_C2.matrix.R.all.RData.clusters_fixed_P_20 --sqlite ${sqlite_db} edgeR_trans/diffExpr.P0.001_C2.matrix.R.all.RData.clusters_fixed_P_20/*matrix



