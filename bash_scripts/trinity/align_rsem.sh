#!/bin/bash
#bowtie2
trinity_loc='/home/aung/software/trinityrnaseq-2.1.1'
# kallisto
/home/aung/software/trinityrnaseq-2.1.1/util/align_and_estimate_abundance.pl --transcripts c01_Trinity_Out/Trinity.fasta --seqType fq --single /home/aung/shrimp_31_10_2013/control_slx_tr.fastq --est_method kallisto --trinity_mode --prep_reference --output_dir control_slx_tr_RSEM
/home/aung/software/trinityrnaseq-2.1.1/util/align_and_estimate_abundance.pl --transcripts c01_Trinity_Out/Trinity.fasta --seqType fa --single /home/aung/shrimp_31_10_2013/mature_slx_tr.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir mature_slx_tr_RSEM
/home/aung/software/trinityrnaseq-2.1.1/util/align_and_estimate_abundance.pl --transcripts c01_Trinity_Out/Trinity.fasta --seqType fa --single /home/aung/shrimp_31_10_2013/survival_slx_tr.fasta --est_method kallisto --trinity_mode --prep_reference --output_dir survival_slx_tr_RSEM
 

kallisto index -i /home/aung/c01_trinity/c01_Trinity_Out/Trinity.fasta.kallisto_idx -k 31 c01_Trinity_Out/Trinity.fasta

kallisto quant -i /home/aung/c01_trinity/c01_Trinity_Out/Trinity.fasta.kallisto_idx -o control_slx_tr_RSEM -l 390 -s 152.62 --pseudobam --single /home/aung/shrimp_31_10_2013/control_slx_tr.fastq | samtools view -Sb - > control_slx_tr_RSEM/out.bam
/home/aung/software/trinityrnaseq-2.1.1/util/support_scripts/kallisto_trans_to_gene_results.pl control_slx_tr_RSEM/abundance.tsv c01_Trinity_Out/Trinity.fasta.gene_trans_map > control_slx_tr_RSEM/abundance.tsv.genes

kallisto quant -i /home/aung/c01_trinity/c01_Trinity_Out/Trinity.fasta.kallisto_idx -o mature_slx_tr_RSEM -l 390 -s 152.62 --pseudobam --single /home/aung/shrimp_31_10_2013/mature_slx_tr.fastq | samtools view -Sb - > mature_slx_tr_RSEM/out.bam
/home/aung/software/trinityrnaseq-2.1.1/util/support_scripts/kallisto_trans_to_gene_results.pl mature_slx_tr_RSEM/abundance.tsv c01_Trinity_Out/Trinity.fasta.gene_trans_map > mature_slx_tr_RSEM/abundance.tsv.genes

kallisto quant -i /home/aung/c01_trinity/c01_Trinity_Out/Trinity.fasta.kallisto_idx -o survival_slx_tr_RSEM -l 390 -s 152.62 --pseudobam --single /home/aung/shrimp_31_10_2013/survival_slx_tr.fastq | samtools view -Sb - > survival_slx_tr_RSEM/out.bam
/home/aung/software/trinityrnaseq-2.1.1/util/support_scripts/kallisto_trans_to_gene_results.pl survival_slx_tr_RSEM/abundance.tsv c01_Trinity_Out/Trinity.fasta.gene_trans_map > survival_slx_tr_RSEM/abundance.tsv.genes

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/GillN.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_GillN;
$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/GillW.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_GillW;
$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HeN.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_HeN;
$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HeW.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_HeW;
$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HPN.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_HPN;
$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e01_pv/mapped/CAP397/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta --seqType fasta --single /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HPW.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e01pv_CAP397_HPW;

#bamfile status
cd e01pv_CAP397_GillN &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/GillN.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e01pv_CAP397_GillW &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/GillW.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e01pv_CAP397_HeN &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HeN.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e01pv_CAP397_HeW &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HeW.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e01pv_CAP397_HPN &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HpN.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e01pv_CAP397_HPW &&
get_unmapped_read_fasta.sh /fs/home/card/Aung/mapped/e01_pv/lessthan1000/HpW.fasta_1000_bp.fasta bowtie2.bam && cd ../

# get unique mapped ref
cd e01pv_CAP397_GillN &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../ &&
cd e01pv_CAP397_GillW &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../ &&
cd e01pv_CAP397_HeN &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../ &&
cd e01pv_CAP397_HeW &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../ &&
cd e01pv_CAP397_HPN &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../ &&
cd e01pv_CAP397_HPW &&
cat mapped_wRef.txt | awk '{ print ""$2"" }'|sort| uniq -c > unique_mapped.txt && cd ../

#get unique mapped ref ID from prev result
cd e01pv_CAP397_GillN &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&
cd e01pv_CAP397_GillW &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&
cd e01pv_CAP397_HeN &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&
cd e01pv_CAP397_HeW &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&
cd e01pv_CAP397_HPN &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&
cd e01pv_CAP397_HPW &&
cat unique_mapped.txt | awk '{print ">"$2}' | sort > unique_mapped.txt.id && cd ../ &&

#get unique unmapped LibID
cd e01pv_CAP397_GillN &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../ &&
cd e01pv_CAP397_GillW &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../ &&
cd e01pv_CAP397_HeN &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../ &&
cd e01pv_CAP397_HeW &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../ &&
cd e01pv_CAP397_HPN &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../ &&
cd e01pv_CAP397_HPW &&
cat unmapped_wRef.txt | awk '{ print ""$1"" }'|sort| uniq -c > unique_unmapped.txt && cd ../

#get unmapped REFID
cd e01pv_CAP397_GillN &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../ &&
cd e01pv_CAP397_GillW &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../ &&
cd e01pv_CAP397_HeN &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../ &&
cd e01pv_CAP397_HeW &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../ &&
cd e01pv_CAP397_HPN &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../ &&
cd e01pv_CAP397_HPW &&
comm -3 ../pv_aunguniq_all.fasta.screen.cm.ge50.fasta.fna.cap3097.contigs_trinity_fmt.fasta.id unique_mapped.txt.id > unmapped_refid.txt && cd ../

#get count
cd e01pv_CAP397_GillN &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../ &&
cd e01pv_CAP397_GillW &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../ &&
cd e01pv_CAP397_HeN &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../ &&
cd e01pv_CAP397_HeW &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../ &&
cd e01pv_CAP397_HPN &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../ &&
cd e01pv_CAP397_HPW &&
pwd
wc -l mapped_wRef.txt
wc -l  unique_mapped.txt.id;
wc -l unmapped_refid.txt;
wc -l unique_unmapped.txt;
cd ../

# combine by set
cd e01pv_CAP397_GillN &&
cat  unique_mapped.txt.id > ../Gill.mappedRef.id;
cat unmapped_refid.txt > ../Gill_unmappedRef.id;
cat unmapped.txt > ../Gill_unmmapedLib.id;
cd ../ &&
cd e01pv_CAP397_GillW &&
cat  unique_mapped.txt.id >> ../Gill.mappedRef.id;
cat unmapped_refid.txt >> ../Gill_unmappedRef.id;
cat unmapped.txt >> ../Gill_unmmapedLib.id;
cd ../ &&
cd e01pv_CAP397_HeN &&
cat  unique_mapped.txt.id >> ../He.mappedRef.id;
cat unmapped_refid.txt >> ../He_unmappedRef.id;
cat unmapped.txt >> ../He_unmmapedLib.id;
cd ../ &&
cd e01pv_CAP397_HeW &&
cat  unique_mapped.txt.id >> ../He.mappedRef.id;
cat unmapped_refid.txt >> ../He_unmappedRef.id;
cat unmapped.txt >> ../He_unmmapedLib.id;
cd ../ &&
cd e01pv_CAP397_HPN &&
cat  unique_mapped.txt.id >> ../HP.mappedRef.id;
cat unmapped_refid.txt >> ../HP_unmappedRef.id;
cat unmapped.txt >> ../HP_unmmapedLib.id;
cd ../ &&
cd e01pv_CAP397_HPW &&
cat  unique_mapped.txt.id >> ../HP.mappedRef.id;
cat unmapped_refid.txt >> ../HP_unmappedRef.id;
cat unmapped.txt >> ../HP_unmmapedLib.id;
cd ../