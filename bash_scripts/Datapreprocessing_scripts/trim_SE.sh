#!/bin/bash
working_dict=${PWD}
for f in  *.fastq
do
        touch "$f"_1.fq
        java -jar /home/aung/software/Trimmomatic-0.30/Trimmomatic-0.30/trimmomatic-0.30.jar SE -threads 4 -phred33 -trimlog r.log $working_dict/$f $working_dict/"$f"_1.fq ILLUMINACLIP:/home/aung/all.Adapter_20130808_HM.fa:2:40:12 LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:40

done

