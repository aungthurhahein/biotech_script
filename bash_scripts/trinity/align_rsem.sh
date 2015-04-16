#!/bin/bash
#bowtie2
trinity_loc='/share/apps/trinityrnaseq_r20140717'
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-N-N01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_HC-N-N01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-N-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_HC-N-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-V-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_HC-V-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-W-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_HC-W-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-N-N01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_LP-N-N01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-N-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_LP-N-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-V-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_LP-V-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-Y-S01.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_LP-Y-S01;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.PmTwI.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_PmTwI;
$trinity_loc//util/align_and_estimate_abundance.pl --transcripts /fs/home/card/Aung/mapped/e02/e02pm_Trinity/Trinity_e02pm_out.fasta_trinity_fmt.fasta --seqType fasta --single /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.PmTwN.seqID_e02.fasta_1000_bp.fasta --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir e02pm_CAP397_PmTwN;

cd e02pm_CAP397_HC-N-N01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-N-N01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_HC-N-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-N-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_HC-V-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-V-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_HC-W-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.HC-W-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_LP-N-N01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-N-N01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_LP-N-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-N-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_LP-V-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-V-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_LP-Y-S01 &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.LP-Y-S01.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_PmTwI &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.PmTwI.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&
cd e02pm_CAP397_PmTwN &&
get_unmapped_read_fasta.sh /fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm_chula/e02_pm/PM82_wTempLibID_04092014.txt.PmTwN.seqID_e02.fasta_1000_bp.fasta bowtie2.bam && cd ../ &&


cd e02pm_CAP397_HC-N-N01 &&

cd e02pm_CAP397_HC-N-S01 &&

cd e02pm_CAP397_HC-V-S01 &&

cd e02pm_CAP397_HC-W-S01 &&

cd e02pm_CAP397_LP-N-N01 &&

cd e02pm_CAP397_LP-N-S01 &&

cd e02pm_CAP397_LP-V-S01 &&

cd e02pm_CAP397_LP-Y-S01 &&

cd e02pm_CAP397_PmTwI &&

cd e02pm_CAP397_PmTwN &&
