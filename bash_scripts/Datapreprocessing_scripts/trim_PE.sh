#! /bin/bash
working_dict="/mnt/nfs/media/new_SRA_datasets_05032015/fastq_files/illumina/PE"
# create empty files for trimmomatic output
for f in  *.fastq
do
        filename="${f%.*}"
        touch "$filename".fq
        touch "$filename".unpaired.fq
done

for f in  *_1.fastq
do
        filename="${f%.*}"
        filename2="${f%_*}"
        f1="$filename".fq
        f1_u="$filename".unpaired.fq
        input2="$filename2"_2.fastq
        f2="$filename2"_2.fq
        f2_u="$filename2"_2.unpaired.fq
        java -jar /home/aung/software/Trimmomatic-0.30/Trimmomatic-0.30/trimmomatic-0.30.jar PE -phred33 -trimlog r.log $working_dict/$f $working_dict/$input2 $working_dict/$f1 $working_dict/$f1_u $working_dict/$f2 $working_dict/$f2_u ILLUMINACLIP:/home/aung/all.Adapter_20130808_HM.fa:2:40:12 LEADING:10 TRAILING:10 SLIDINGWINDOW:4:15 MINLEN:40
done

