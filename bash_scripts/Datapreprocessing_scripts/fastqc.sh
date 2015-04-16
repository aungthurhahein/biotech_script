#! /bin/bash
for f in  *.fastq
do
        fastqc $f
done

