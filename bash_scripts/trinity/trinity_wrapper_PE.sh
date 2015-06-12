#!/bin/sh
for i in *_1.fastq
do
        filename="${i%_*}"
        input2="$filename"_2.fastq
        ext="_out"
        output=$filename$ext
        echo "#!/bin/bash" > $filename.sh
        echo "#$ -S /bin/bash" >> $filename.sh
        echo "#$ -N $filename" >> $filename.sh
        echo "#$ -cwd" >> $filename.sh
        echo "#$ -m e" >> $filename.sh
        echo "#$ -M aungthurhahein@gmail.com" >> $filename.sh
        echo "#$ -pe mpich 4" >> $filename.sh
        echo ". /fs/home/card/.bashrc" >> $filename.sh
        echo ". /fs/home/card/.bash_profile" >> $filename.sh

        echo "trinity_loc='/share/apps/trinityrnaseq_r20140717'" >> $filename.sh
        echo "working_dict=${PWD}" >> $filename.sh
        echo "input1='$i'" >> $filename.sh
        echo "input2='$input2'" >> $filename.sh
        echo "output='$output'" >> $filename.sh
        echo "# assemble" >> $filename.sh
        echo '$trinity_loc/Trinity --seqType fq --JM 20G --left $working_dict/$input1 --right $working_dict/$input2  --CPU 10 --output $output' >> $filename.sh

        echo "#alignment" >> $filename.sh
        echo 'cd $output' >> $filename.sh
        echo '$trinity_loc/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta  --seqType fq --left ../$input1 --right ../$input2 --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference' >> $filename.sh
done
