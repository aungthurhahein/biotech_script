#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N trinity2
# Run in current working dir
#$ -cwd
#flag to notify when the jod submitted(b) or finished(e) or both(be)
#$ -m e
#email to distribute job status
#$ -M aungthurhahein@gmail.com
# for mutli-thread(parallel) jobs, provide no. of nodes to run(even number make sense)
#$ -pe mpich 1

. /fs/home/card/.bashrc
. /fs/home/card/.bash_profile

trinity_loc='/colossus/home/anuphap/software/trinityrnaseq-2.1.1'
inputfile1='NGRL-RNA1_strand_specifc_RNA_ACTGAT_RmCtrl_R1.fastq'
inputfile2='NGRL-RNA1_strand_specifc_RNA_ACTGAT_RmCtrl_R2.fastq'
ext="_out"
ext2="rsem"
output=$inputfile$ext
rsemout=$inputfile$rsem
# assemble
#single
# $trinity_loc/Trinity --seqType fq --JM 20G --single $inputfile --CPU 10 --output $output

#pair
$trinity_loc/Trinity --seqType fq --left $inputfile1 --right $inputfile2 --max_memory 20G --SS_lib_type FR --CPU 10 --output NGRL_RNA_Trinity

#alignment
# $trinity_loc/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta  --seqType fq --left $inputfile1 --left $inputfile2 --est_method kallisto --SS_lib_type FR --trinity_mode --prep_reference --output_dir control_slx_tr_RSEM/

#Generating Expression Value Matrix
#$trinity_loc/abundance_estimates_to_matrix.pl --est_method RSEM --out_prefix