#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N cdhit
# Run in current working dir
#$ -cwd
#flag to notify when the jod submitted(b) or finished(e) or both(be)
#$ -m e
#email to distribute job status
#$ -M aungthurhahein@gmail.com
# for mutli-thread(parallel) jobs, provide no. of nodes to run(even number make sense)
#$ -pe mpich 4

. /fs/home/card/.bashrc
. /fs/home/card/.bash_profile
cdhit_home="/fs/home/card/software/cd-hit-v4.6.1-2012-08-27"  #eclipse
#cdhit_home="/colossus/home/anuphap/software/cd-hit-v4.6.1-2012-08-27" #colossus
input_base="/fs/home/card/Aung/PCHUM-RT/stepC/"

for i in *.gb.fasta
do
    out="_out"
    file_out=$i$out
    $cdhit_home/cd-hit-est -i $input_base$i  -o $file_out -c 0.98 -aS 0.97 -d 200 -g 1 -M 10000 -T 15
done