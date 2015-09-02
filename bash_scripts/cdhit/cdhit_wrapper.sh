#!/usr/bin/env bash
#
#input_base="/fs/home/card/Aung/ATM03-Task20-B"
#filebase="ATM02-TaskB"
ext=".fasta"
out="_out"
i=0
ext2=".sh"
#while [ $i -le 15 ]
for i in *.fasta
do
#    i=$(( $i + 1 ))
    filename=$i$ext2
    file_out=$i$out
    echo "#!/bin/sh" > $filename
    echo "#$ -S /bin/bash" >> $filename
    echo "#$ -N cdhit_$i" >> $filename
    echo "#$ -cwd" >> $filename
    echo "#$ -m e" >> $filename
    echo "#$ -M aungthurhahein@gmail.com" >> $filename
    echo "#$ -pe mpich 4" >> $filename
    echo ". /fs/home/card/.bashrc" >> $filename
    echo ". /fs/home/card/.bash_profile" >> $filename
    cdhit_home="/fs/home/card/software/cd-hit-v4.6.1-2012-08-27"
#    echo "infile=$input_base$filebase$i$ext" >> $filename
#    echo "file_out=$i$out" >> $filename
    echo "$cdhit_home/cd-hit-est -i $i  -o $file_out -c 0.98 -aS 0.97 -d 200 -g 1 -M 10000 -T 15" >> $filename
done