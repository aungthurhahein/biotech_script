#!/bin/bash
sra_home="/opt/sratoolkit/sratoolkit.2.3.2-5-ubuntu64/bin"
working_dir=${PWD}

for i in *.sra
do
    $sra_home/fastq-dump --split-3 $working_dir/$i
done