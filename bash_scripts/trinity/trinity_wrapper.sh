#!/bin/sh

for i in *.fastq
do
        echo "#!/bin/bash" > $i.sh
        echo "#$ -S /bin/bash" >> $i.sh
        echo "#$ -N $i" >> $i.sh
        echo "#$ -cwd" >> $i.sh
        echo "#$ -m e" >> $i.sh
        echo "#$ -M aungthurhahein@gmail.com" >> $i.sh
        echo "#$ -pe mpich 4" >> $i.sh
        echo ". /fs/home/card/.bashrc" >> $i.sh
        echo ". /fs/home/card/.bash_profile" >> $i.sh

        echo "trinity_loc='/share/apps/trinityrnaseq_r20140717'" >> $i.sh
        echo 'working_dict=${PWD}' >> $i.sh

        echo "inputfile='$i'" >> $i.sh
        echo 'rsemout=$inputfile$rsem' >> $i.sh
        echo "ext='_out'" >> $i.sh
        echo "ext2='_rsem'">> $i.sh
        echo 'output=$inputfile$ext' >> $i.sh

        echo "# assemble" >> $i.sh
        echo '$trinity_loc/Trinity --seqType fq --JM 20G --single $working_dict/$inputfile --CPU 10 --output $output' >> $i.sh


        echo "#alignment" >> $i.sh
        echo 'cd $output' >> $i.sh
        echo '$trinity_loc/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta  --seqType fq --single ../$inputfile --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference' >> $i.sh
done
