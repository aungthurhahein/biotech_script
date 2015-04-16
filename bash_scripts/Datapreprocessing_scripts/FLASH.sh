#!/bin/bash
working_dict="/mnt/nfs/media/new_SRA_datasets_05032015/fastq_files/illumina/PE/trimmed_reads"
flash_dir="/home/aung/software/FLASH-1.2.7"

for f in  *_1.fq
do
        filename="${f%.*}"
        filename2="${f%_*}"
        input2="$filename2"_2.fq

        echo "$flash_dir/flash -o $filename2 $working_dict/$f $working_dict/$input2"
        $flash_dir/flash -o $filename2 $working_dict/$f $working_dict/$input2
done
