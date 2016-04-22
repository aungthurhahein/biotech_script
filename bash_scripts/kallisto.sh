#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N kallisto
# Run in current working dir
#$ -cwd
#flag to notify when the jod submitted(b) or finished(e) or both(be)
#$ -m e
#email to distribute job status
#$ -M aungthurhahein@gmail.com
# for mutli-thread(parallel) jobs, provide no. of nodes to run(even number make sense)
#$ -pe mpich 1

mkdir e01_pm_chula_CAP397_HC-N-N01
mkdir e01_pm_chula_CAP397_HC-N-S01
mkdir e01_pm_chula_CAP397_HC-V
mkdir e01_pm_chula_CAP397_HC-W
mkdir e01_pm_chula_CAP397_LP-N-N01
mkdir e01_pm_chula_chula_LP-N-S01
mkdir e01_pm_chula_CAP397_LP-V
mkdir e01_pm_chula_CAP397_LP-Y
mkdir e01_pm_chula_CAP397_TW-I
mkdir e01_pm_chula_CAP397_TW-N

trinity="/colossus/home/anuphap/software/trinityrnaseq-2.1.1"

cd e01_pm_chula_CAP397_TW-I &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 136 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 605   --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.PmTwI.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out && cd .. &&

cd e01_pm_chula_CAP397_TW-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 145 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 625  --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.PmTwN.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out && cd .. &&

cd e01_pm_chula_CAP397_HC-N-N01 &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 175 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 586 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.HC-N-N01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out && cd .. &&

cd e01_pm_chula_CAP397_HC-N-S01 &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 175 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 667 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.HC-N-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out && cd .. &&

cd e01_pm_chula_CAP397_HC-V &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 148 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 565 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.HC-V-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd e01_pm_chula_CAP397_HC-W &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 144 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 502 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.HC-W-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd e01_pm_chula_CAP397_LP-N-N01 &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 126 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 487 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.LP-N-N01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd e01_pm_chula_CAP397_LP-V &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 165 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 578 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.LP-V-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd e01_pm_chula_CAP397_LP-Y &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 138 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 496 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.LP-Y-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out 

cd e01_pm_chula_CAP397_HC-N-S01 &&
$trinity/util/align_and_estimate_abundance.pl --fragment_std 164 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/CHULA/e01_pm_CAP3DF/e01_pm.fasta.fna.cap3DF.contigs_2Trinity.fasta --seqType fasta --fragment_length 404 --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm_chula/PM82_wTempLibID_04092014.txt.LP-N-S01.seqID.fasta --est_method kallisto --kallisto_add_opts "--pseudobam" --trinity_mode --prep_reference --output_dir  aln_out

