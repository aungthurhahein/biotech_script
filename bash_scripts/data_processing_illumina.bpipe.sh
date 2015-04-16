#!/bin/bash
# Illumina PE

sra_path="/opt/sratoolkit/sratoolkit.2.3.2-5-ubuntu64/bin/"
trimmomatic_path="/home/aung/software/Trimmomatic-0.30/Trimmomatic-0.30"
# convert to fastq
fastq_convert={
    exec "$sra_path/fastq-dump --split-3 $input"
}
# fastqc report
fastqc_report={
    exec "fastqc --split-3 $input"
}
# create files
create_files={
    exec "touch t1.fq && touch t2.fq && touch t1.unpaired.fq && touch t2.unpaired.fq"
}
# Trimmmomatic
trim_read={
    exec "java -jar $trimmomatic_path/trimmomatic-0.30.jar PE -phred33 -trimlog r.log {$input}_1.fastq {$input}_2.fastq  t1.fq t1.unpaired.fq t2.fq t2.unpaired.fq ILLUMINACLIP:/home/aung/all.Adapter_20130808_HM.fa:2:40:12 LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:40"
}

# Flash
length_adjust={
    exec "flash t1.fq t2.fq"
}

Bpipe.run {
    fastq_convert + fastqc_report + crate_files + trim_read + length_adjust
}

