#!/bin/bash
trinity_loc='/share/apps/trinityrnaseq_r20140717'
inputfile='trinity.fastq'
ext="_out"
ext2="rsem"
output=$inputfile$ext
rsemout=$inputfile$rsem
# assemble
$triinity_loc/Trinity --seqType fq --JM 20G --single $inputfile --CPU 10 --output $output

#alignment
#$trinity_loc/util/align_and_estimate_abundance.pl --transcripts $output/Trinity.fasta  --seqType fastq --single $inputfile --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir $rsemout

#Generating Expression Value Matrix
#$trinity_loc/abundance_estimates_to_matrix.pl --est_method RSEM --out_prefix
