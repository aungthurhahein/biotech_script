#!/usr/bin/env bash

DIR1="/fs/home/card/Assembly/AsPepID/E01/"
# e0101
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pm_mira_idmap.txt /fs/home/card/Aung/by_trinotate/e0101_trinotate/e01_pm_mira_trinity.fasta.transdecoder.pep
# e0102
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pm_cap397_idmap.txt /fs/home/card/Aung/by_trinotate/e0102_trinotate/T/e01_pm_cap397_trinity.fasta.transdecoder.pep
# e0103
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pm_cap3DF_idmap.txt /fs/home/card/Aung/by_trinotate/e0103_trinotate/e01_pm_cap3Df_trinity.fasta.transdecoder.pep
# e0104
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pm_Trinity_idmap.txt /fs/home/card/Aung/by_trinotate/e0104_trinotate/e01_pm_trinity.fasta.transdecoder.pep
# e0105
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pv_mira_idmap.txt /fs/home/card/Aung/by_trinotate/e0105_trinotate/e01_pv_mira_trinity.fasta.transdecoder.pep
# e0106
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pv_cap97_idmap.txt /fs/home/card/Aung/by_trinotate/e0106_trinotate/e01_pv_cap97_trinity.fasta.transdecoder.pep
# e0107
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pv_capDF_idmap.txt /fs/home/card/Aung/by_trinotate/e0107_trinotate/e01_pv_capDF_trinity.fasta.transdecoder.pep
# e0108
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pv_Trinity_idmap.txt /fs/home/card/Aung/by_trinotate/e0108_trinotate/e01_pv_Trinity_trinity.fasta.transdecoder.pep
# e0109
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E01/e01_pm_cap397_unm01_idmap.txt /fs/home/card/Aung/by_trinotate/e0109_trinotate/e01_pm_cap397_unm01.fasta.transdecoder.pep

mv /fs/home/card/Aung/by_trinotate/e0101_trinotate/e01_pm_mira_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0102_trinotate/T/e01_pm_cap397_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0103_trinotate/e01_pm_cap3Df_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0104_trinotate/e01_pm_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0105_trinotate/e01_pv_mira_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0106_trinotate/e01_pv_cap97_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0107_trinotate/e01_pv_capDF_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0108_trinotate/e01_pv_Trinity_trinity.fasta.transdecoder.pep_* $DIR1
mv /fs/home/card/Aung/by_trinotate/e0109_trinotate/e01_pm_cap397_unm01.fasta.transdecoder.pep_* $DIR1


DIR2="/fs/home/card/Assembly/AsPepID/E02/"

#e02
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pm_mira_idmap.txt /fs/home/card/Aung/by_trinotate/e0201_trinotate/e02_pm_mira_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pm_cap97_idmap.txt /fs/home/card/Aung/by_trinotate/e0202_trinotate/e02_pm_cap97_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pm_capDF_idmap.txt /fs/home/card/Aung/by_trinotate/e0203_trinotate/e02_pm_capDF_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pm_Trinity_idmap.txt /fs/home/card/Aung/by_trinotate/e0204_trinotate/e02_pm_Trinity_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pv_mira_id_map.txt /fs/home/card/Aung/by_trinotate/e0205_trinotate/e02_pv_mira_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pv_cap97_id_map.txt /fs/home/card/Aung/by_trinotate/e0206_trinotate/e02_pv_cap97_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pv_capDF_id_map.txt /fs/home/card/Aung/by_trinotate/e0207_trinotate/e02_pv_capDF_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E02/e02_pv_Trinity_idmap.txt /fs/home/card/Aung/by_trinotate/e0208_trinotate/e02_pv_Trinity_trinity.fasta.transdecoder.pep

mv e02_pm_mira_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0201_trinotate/
mv e02_pm_cap97_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0202_trinotate/
mv e02_pm_capDF_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0203_trinotate/
mv e02_pm_Trinity_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0204_trinotate/
mv e02_pv_mira_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0205_trinotate/
mv e02_pv_cap97_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0206_trinotate/
mv e02_pv_capDF_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0207_trinotate/
mv e02_pv_Trinity_trinity.fasta.transdecoder.pep /fs/home/card/Aung/by_trinotate/e0208_trinotate/

mv /fs/home/card/Aung/by_trinotate/e0201_trinotate/e02_pm_mira_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0202_trinotate/e02_pm_cap97_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0203_trinotate/e02_pm_capDF_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0204_trinotate/e02_pm_Trinity_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0205_trinotate/e02_pv_mira_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0206_trinotate/e02_pv_cap97_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0207_trinotate/e02_pv_capDF_trinity.fasta.transdecoder.pep_* $DIR2
mv /fs/home/card/Aung/by_trinotate/e0208_trinotate/e02_pv_Trinity_trinity.fasta.transdecoder.pep_* $DIR2


DIR4="/fs/home/card/Assembly/AsPepID/E0102_ContigsV22_Nucl3_SIEST_EHP"

#nucl3
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/20141022_nucleotide3/pool_nucleotideseq.txt.sort.fasta_out_id_map.txt /fs/home/card/Aung/20141022_nucleotide3/StepT/pool_nucleotideseq.txt.sort.fasta_out_trinity_fmt.fasta.transdecoder.pep

#contigsv22
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/ContigsV22/contigsV22_pool_Lin201501_id_map.txt /fs/home/card/Aung/contigv22/stepT/contigsV22_nonF.id.fasta.transdecoder.pep

#E0102
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/E0102pmpv_sequences/E0102_pmpv.fasta_out_id_map.txt /fs/home/card/Aung/E01-02PMPV/by_trinotate/E0102_pmpv.fasta_out_trinity_fmt.fasta.transdecoder.pep

#SIEST
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/SIEST01/SgpatESTcmV3-20150821_id_map.txt /fs/home/card/Aung/SIESTCM_CDHIT/StepT/SIESTCM20150821_updated.fasta_out_trinity_fmt.fasta.transdecoder.pep

#EHP
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Aung/20150722_michaelA5/contigs.orf_nucleotid.fasta_id_map.txt /fs/home/card/Aung/20150722_michaelA5/contigs.orf_nucleotid.fasta_trinity_fmt.fasta.transdecoder.pep

mv /fs/home/card/Aung/20141022_nucleotide3/StepT/pool_nucleotideseq.txt.sort.fasta_out_trinity_fmt.fasta.transdecoder.pep_* $DIR4
mv /fs/home/card/Aung/contigv22/stepT/contigsV22_nonF.id.fasta.transdecoder.pep_* $DIR4
mv /fs/home/card/Aung/E01-02PMPV/by_trinotate/E0102_pmpv.fasta_out_trinity_fmt.fasta.transdecoder.pep_* $DIR4
mv /fs/home/card/Aung/SIESTCM_CDHIT/StepT/SIESTCM20150821_updated.fasta_out_trinity_fmt.fasta.transdecoder.pep_* $DIR4
mv /fs/home/card/Aung/20150722_michaelA5/contigs.orf_nucleotid.fasta_trinity_fmt.fasta.transdecoder.pep_*  $DIR4


DIR5="/fs/home/card/Assembly/AsPepID/Illumina"
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388207_PE_trinity.id_map.txt /fs/home/card/Aung/by_trinotate/ILT01_trinotate/illumina_trinity_SRR388207_PE_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388221_PE_id_map.txt /fs/home/card/Aung/by_trinotate/ILT02_trinotate/illumina_trinity_SRR388221_PE_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388222_PE_id_map.txt /fs/home/card/Aung/by_trinotate/ILT03_trinotate/illumina_trinity_SRR388222_PE_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388207_SR_id_map.txt /fs/home/card/Aung/by_trinotate/ILT04_trinotate/illumina_trinity_SRR388207_SR_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388221_SR_id_map.txt /fs/home/card/Aung/by_trinotate/ILT05_trinotate/illumina_trinity_SRR388221_SR_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388222_SR_id_map.txt /fs/home/card/Aung/by_trinotate/ILT06_trinotate/illumina_trinity_SRR388222_SR_trinity.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388207_2CDHIT-Out_id_map.txt /fs/home/card/Aung/by_trinotate/ILT07_trinotate/illumina_trinity_SRR388207_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388221_2CDHIT-Out_id_map.txt /fs/home/card/Aung/by_trinotate/ILT08_trinotate/illumina_trinity_SRR388221_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/illumina_trinity_SRR388222_2CDHIT-Out_id_map.txt /fs/home/card/Aung/by_trinotate/ILT09_trinotate/illumina_trinity_SRR388222_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/pm_APc01_trinity_e01_3CDHIT_id_map.txt /fs/home/card/Aung/by_trinotate/pmP01_trinotate/pm_APc01_trinity_e01_3CDHIT_trinity.fasta.transdecoder.
python /fs/home/card/bin/pepid_gen.py /fs/home/card/Assembly/AsTranIDs/illumina/PM/pm_P_trinity_e01_3CDHIT_id_map.txt /fs/home/card/Aung/by_trinotate/pmP01_trinotate/pm_P_trinity_e01_3CDHIT_trinity.fasta.transdecoder.pep

mv /fs/home/card/Aung/by_trinotate/pmP01_trinotate/pm_P_trinity_e01_3CDHIT_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/pmP01_trinotate/pm_APc01_trinity_e01_3CDHIT_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT01_trinotate/illumina_trinity_SRR388207_PE_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT02_trinotate/illumina_trinity_SRR388221_PE_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT03_trinotate/illumina_trinity_SRR388222_PE_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT04_trinotate/illumina_trinity_SRR388207_SR_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT05_trinotate/illumina_trinity_SRR388221_SR_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT06_trinotate/illumina_trinity_SRR388222_SR_trinity.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT07_trinotate/illumina_trinity_SRR388207_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT08_trinotate/illumina_trinity_SRR388221_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep_* $DIR5
mv /fs/home/card/Aung/by_trinotate/ILT09_trinotate/illumina_trinity_SRR388222_2CDHIT-Out_trinity_fmt.fasta.transdecoder.pep_* $DIR5

