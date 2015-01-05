#! /bin/bash
#-----------------------------------------------------#
# get unmapped reads from bam files
# Dev: Aung
# 18122014
# usage: get_unmapped_bam.sh sample.fasta bowtie2.bam
# output: 
# 1.reads.txt : fastq headers
# 2. mapped.txt: mapped headers
# 3. unmapped.txt: unmapped headers
#-----------------------------------------------------#

FASTA=$1
BAM=$2
#sort bam files by name and index it 
samtools sort $BAM -f sorted.bam && samtools index sorted.bam
# print out mapped headers
samtools view -F 4 sorted.bam | awk '{ print ">"$1"" }' | sort -u > mapped.txt
# grep only the fq headers.
grep '>' $FASTA |  sort -u > reads.txt
# supress and print unmapped
comm -3 reads.txt mapped.txt > unmapped.txt
#print summary 
wc -l reads.txt
wc -l mapped.txt
wc -l unmapped.txt
