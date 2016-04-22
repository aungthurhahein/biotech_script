#! /bin/bash

mkdir NCBI01-Gill-N
mkdir NCBI01-Gill-W
mkdir NCBI01-HC-N
mkdir NCBI01-HC-W
mkdir NCBI01-HC-Y
mkdir NCBI01-HC-V
mkdir NCBI01-LY-N
mkdir NCBI01-LY-Y
mkdir NCBI01-LY-V
mkdir NCBI01-LY-V
mkdir NCBI01-WH-W
mkdir NCBI01-WH-N
mkdir NCBI01-WH-N
mkdir NCBI01-WH-V
mkdir NCBI01-ML-W
mkdir NCBI01-ML-N

trinity="/colossus/home/anuphap/software/trinityrnaseq-2.1.1"

cd NCBI01-Gill-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 428 --fragment_std 207 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-Gill-N.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-Gill-W &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 470 --fragment_std 161 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-Gill-W.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-HC-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 645 --fragment_std 245 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-HC-N.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-HC-W &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 470 --fragment_std 161 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-HC-W.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-HC-Y &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 462 --fragment_std 195 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-HC-Y.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-HC-V &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 542 --fragment_std 163 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-HC-V.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-LY-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 522 --fragment_std 155 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-LY-N.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-LY-Y &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 476 --fragment_std 163 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-LY-Y.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-LY-V &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 570 --fragment_std 140 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-LY-V.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&


cd NCBI01-WH-W &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 418 --fragment_std 235 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-WH-W.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-WH-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 488 --fragment_std 227 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-WH-N.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-WH-V &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 346 --fragment_std 182 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-WH-V.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-ML-W &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 322 --fragment_std 211 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-ML-W.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd .. &&

cd NCBI01-ML-N &&
$trinity/util/align_and_estimate_abundance.pl --fragment_length 583 --fragment_std 158 --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pm/NCBI/e01_pm_CAP397/e01_pm.fasta.fna.cap3097.contigs_2Trinity.fasta --seqType fasta --single /colossus/home/anuphap/EST/EST_lib_IDs/pm/slect_bytissues_pm/NCBI01-ML-N.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir aln_out && cd ..
