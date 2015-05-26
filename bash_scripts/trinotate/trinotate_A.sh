#!/bin/bash

#sys envvariables
trinity_home="/share/apps/trinityrnaseq_r20140717"
trinotate_home="/fs/home/card/hasan/Trinotate_r20140708"
transdecoder_home="/share/apps/trinityrnaseq_r20140717/trinity-plugins/transdecoder" #version 2.0
#transdecoder_home="/fs/home/card/software/TransDecoder-2.0.1" #version 2.1
hmmer_home="/fs/home/card/bin"
signalp_home="/fs/home/card/hasan/signalp-4.1"
tmhmm_home="/fs/home/card/hasan/tmhmm/tmhmm-2.0c/bin"
rnammer_home="/fs/home/card/hasan/rnammer12"

#input
trinity_file="trinity.fasta"
ext=".transdecoder.pep"
ext2=".gene_trans_map"
transdecoder_output=$trinity_file$ext
gene_trans_map=$trinity_file$ext2

#A1: Transdecoder
echo "#########################"
echo"A1:Running Transdecoder"
echo "#########################"
$transdecoder_home/TransDecoder -t $trinity_file

#A2: Gene_Trans Map
echo "#########################"
echo"A2:mapping genes and transcripts"
echo "#########################"
$trinotate_home/util/support_scripts/get_Trinity_gene_to_trans_map.pl $trinity_file > $gene_trans_map


#A3: BLAST
echo "#########################"
echo"A3:Running blastp and blastx"
echo "#########################"
blastx -query $trinity_file -db uniprot_sprot.trinotate.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastx.outfmt6
blastp -query $transdecoder_output -db uniprot_sprot.trinotate.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > blastp.outfmt6

blastx -query $trinity_file -db uniprot_uniref90.trinotate.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > uniref90.blastx.outfmt6
blastp -query $transdecoder_output -db uniprot_uniref90.trinotate.pep -num_threads 8 -max_target_seqs 1 -outfmt 6 > uniref90.blastp.outfmt

#A4: HMMer
echo "A4:#########################"
echo"Running HMMer"
echo "#########################"
$hmmer_home/hmmscan --cpu 8 --domtblout TrinotatePFAM.out Pfam-A.hmm $transdecoder_output > pfam.log

#A5: SignalP
echo "A5:#########################"
echo"Running SignalP"
echo "#########################"
$signalp_home/signalp -f short -n signalp.out $transdecoder_output

#A6: TmHMM
echo "#########################"
echo"A6:Running TmHMM"
echo "#########################"
$tmhmm_home/tmhmm --short < $transdecoder_output > tmhmm.out

#A7: RNammer
echo "#########################"
echo"A7:Running RNammer"
echo "#########################"
$trinotate_home/util/rnammer_support/RnammerTranscriptome.pl --transcriptome $trinity_file --path_to_rnammer=$rnammer_home


echo "#########################"
echo "Trinotate Process A1-A7 runned completely!"
echo "#########################"