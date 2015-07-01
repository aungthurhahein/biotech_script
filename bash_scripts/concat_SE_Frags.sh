#!/usr/bin/env bash

for f in  *_1.fq
do
    filename="${f%_*}"
    ext="_1.unpaired.fq"
    ext2="_2.unpaired.fq"
    ext3=".extendedFrags.fastq"
    ext4="_pe_frags.fastq"
    unpair1=$filename$ext
    unpair2=$filename$ext2
    frag=$filename$ext3
    out=$filename$ext4

    echo $filename
    cat $unpair1 > $out
    cat $unpair2 >> $out
    cat $frag >> $out
done




