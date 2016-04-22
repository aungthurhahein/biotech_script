#! /bin/bash
trinity_loc="/colossus/home/anuphap/software/trinityrnaseq-2.1.1"

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/GillN.fasta --fragment_length 507 --fragment_std 203  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_GillN;

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/GillW.fasta --fragment_length 439 --fragment_std 252  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_GillW;

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/HeN.fasta --fragment_length 540   --fragment_std 210  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_HeN;

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/HeW.fasta--fragment_length 511    --fragment_std 237  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_HeW;

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/HPN.fasta --fragment_length 458   --fragment_std 182  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_HPN;

$trinity_loc/util/align_and_estimate_abundance.pl --transcripts /colossus/home/anuphap/e0102_kallisto/e01_pv/mapped/trinity/Trinity.e01pv_out.fasta_trinity_fmt.fasta --seqType fasta --single /colossus/home/anuphap/e0102_kallisto/e01_pv/sequencebySets/HPW.fasta --fragment_length 479   --fragment_std 217  --est_method kallisto --trinity_mode --prep_reference --output_dir e01pv_CAP397_HPW;

