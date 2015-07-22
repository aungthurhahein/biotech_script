#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N job-name
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


#sys env
#trinotate_home="/fs/home/card/hasan/Trinotate_r20140708"
trinotate_home="/fs/home/card/software/Trinotate-2.0.2" #trinoteate v.2.0.2
working_dir=${PWD}

#input
trinity_file="trinity.fasta"
ext=".transdecoder.pep"
ext2=".gene_trans_map"
ext3=".rnammer.gff"
transdecoder_output=$trinity_file$ext
gene_trans_map=$trinity_file$ext2
rnammer_output=$trinity_file$ext3

# B1: download sqlite file with schema
echo "#########################"
echo "B1:Downloading new trinotate sqlite file"
echo "#########################"
# wget "ftp://ftp.broadinstitute.org/pub/Trinity/Trinotate_v2.0_RESOURCES/Trinotate.sprot_uniref90.20150131.boilerplate.sqlite.gz" -O Trinotate.sqlite.gz
cp /fs/home/card/Aung/trinotate_req/Trinotate.sqlite.gz $working_dir
gunzip Trinotate.sqlite.gz
rm -rf Trinotate.sqlite.gz

# B2:  Loading Transcript-protein
echo "#########################"
echo "B2:Loading Transcript-protein"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite init --gene_trans_map $gene_trans_map --transcript_fasta $trinity_file --transdecoder_pep $transdecoder_output


# C1: loading search result
# load protein hits(SP blast)
echo "#########################"
echo "C1:load protein hits(SP blast)"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_swissprot_blastx blastx.outfmt6

# load protein hits(uniref blast)
echo "#########################"
echo "C1:load protein hits(uniref blast)"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_trembl_blastx uniref90.blastx.outfmt6

# load transcript hits(SP blast)
echo "#########################"
echo "C1:load transcript hits(SP blast)"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_swissprot_blastp blastp.outfmt6

# load transcript hits(uniref blast)
echo "#########################"
echo "C1:load transcript hits(uniref blast)"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_trembl_blastp uniref90.blastp.outfmt6


# C.2 loading pfam(A4 Process) domain entries

# load pfam domain
echo "#########################"
echo "C2:load pfam domain"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_pfam TrinotatePFAM.out


# C.3 loading signal peptide prediction(A5 Process)

# load signlap output
echo "#########################"
echo "C3:load signlap output"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_signalp signalp.out


# C.4 loading transmembrane (A6 Process) domain

# load tmhmm domain
echo "#########################"
echo "C4:load tmhmm domain"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_tmhmm tmhmm.out

# C.5 loading rnammer output (A7 Process)

# load rnammer output
echo "#########################"
echo "C5:load rnammer output"
echo "#########################"
$trinotate_home/Trinotate Trinotate.sqlite LOAD_rnammer $rnammer_output


echo "#########################"
echo "Trinotate Process B-C runned completely!"
echo "#########################"