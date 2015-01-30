#!/bin/bash

# unmaped reads count
cat unmapped_wRef.txt | wc -l
# unique unmaped reads
cat unmapped_wRef.txt | uniq -c |wc -l

#mapped readcount
cat mapped_wRef.txt | awk '{ print ""$2"" }' | wc -l
# unique mapped count
cat mapped_wRef.txt | awk '{ print ""$2"" }' | uniq -c | wc -l


# TW
cd e01pm_CAP397_chula_Tw-N/e01_pm_chula_CAP397_TW-N/ &&
cat unmapped_wRef.txt > /fs/home/card/mapped/CHULA/e01_pm_cap397/TW_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_Tw-I/e01_pm_chula_CAP397_TW-I/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/TW_unmapped.txt
&& cd ../../ &&

#HC
cd e01pm_CAP397_chula_HC-N-N01/e01_pm_chula_CAP397_HC-N-N01/ &&
cat unmapped_wRef.txt > /fs/home/card/mapped/CHULA/e01_pm_cap397/HC_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_HC-N-S01/e01_pm_chula_CAP397_HC-N-S01/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/HC_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_HC-V/e01_pm_chula_CAP397_HC-V/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/HC_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_HC-W/e01_pm_chula_CAP397_HC-W/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/HC_unmapped.txt
&& cd ../../ &&

#LP
cd e01pm_CAP397_chula_LP-N-N01/e01_pm_chula_CAP397_LP-N-N01/ &&
cat unmapped_wRef.txt > /fs/home/card/mapped/CHULA/e01_pm_cap397/LP_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_LP-V/e01_pm_chula_CAP397_LP-V/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/LP_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_LP-Y/e01_pm_chula_CAP397_LP-Y/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/LP_unmapped.txt
&& cd ../../ &&
cd e01pm_CAP397_chula_LP-N-S01/e01_pm_chula_chula_LP-N-S01/ &&
cat unmapped_wRef.txt >> /fs/home/card/mapped/CHULA/e01_pm_cap397/LP_unmapped.txt
&& cd ../../



cat PM82_wTempLibID_04092014.txt.PmTwI.seqID.fasta_1000_bp.fasta > TW_combine.sh &&
cat PM82_wTempLibID_04092014.txt.PmTwN.seqID.fasta_1000_bp.fasta >> TW_combine.sh &&
cat PM82_wTempLibID_04092014.txt.HC-N-N01.seqID.fasta_1000_bp.fasta > HC_combine.sh &&
cat PM82_wTempLibID_04092014.txt.HC-N-S01.seqID.fasta_1000_bp.fasta >> HC_combine.sh &&
cat PM82_wTempLibID_04092014.txt.HC-V-S01.seqID.fasta_1000_bp.fasta >> HC_combine.sh &&
cat PM82_wTempLibID_04092014.txt.HC-W-S01.seqID.fasta_1000_bp.fasta >> HC_combine.sh &&
cat PM82_wTempLibID_04092014.txt.LP-N-N01.seqID.fasta_1000_bp.fasta > LP_combine.sh &&
cat PM82_wTempLibID_04092014.txt.LP-N-S01.seqID.fasta_1000_bp.fasta >> LP_combine.sh &&
cat PM82_wTempLibID_04092014.txt.LP-V-S01.seqID.fasta_1000_bp.fasta >> LP_combine.sh &&
cat PM82_wTempLibID_04092014.txt.LP-Y-S01.seqID.fasta_1000_bp.fasta >> LP_combine.sh
