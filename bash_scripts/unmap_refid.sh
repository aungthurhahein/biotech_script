#!/bin/bash
grep '>' $1 | sort | awk '{print $1}' > "$1".sortid

cat $2 | awk '{print ">"$2}' > "$2".sortid
comm -3 "$1".sortid "$2".sortid > "$2".unmapped_refID

path="/fs/home/card/Aung/mapped/NCBI/e01_pm_CAP3DF"
file_path="/fs/home/anuphap/EST/lib_IDs/slect_bytissues_pm/e01_pm"
gn="NCBI01-Gill-N.fasta_1000_bp.fasta"
gw="NCBI01-Gill-W_1000_bp.fasta"
hcn="NCBI01-HC-N.fasta_1000_bp.fasta"
hcv="NCBI01-HC-V.fasta_1000_bp.fasta"
hcw="NCBI01-HC-W.fasta_1000_bp.fasta"
hcy="NCBI01-HC-Y.fasta_1000_bp.fasta"
lyn="NCBI01-LY-N.fasta_1000_bp.fasta"
lyv="NCBI01-LY-V.fasta_1000_bp.fasta"
lyy="NCBI01-LY-Y.fasta_1000_bp.fasta"
mln="NCBI01-ML-N.fasta_1000_bp.fasta"
whn="NCBI01-WH-N.fasta_1000_bp.fasta"
whv="NCBI01-WH-V.fasta_1000_bp.fasta"
whw="nucest_id.info.Lib_ID.gi2libid.LIBEST_021064.fasta_1000_bp.fasta"
mlw="nucest_id.info.Lib_ID.gi2libid.LIBEST_023446.fasta_1000_bp.fasta"

cd NCBI01-Gill-N/NCBI01-Gill-N/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$gn  && cd ../../ &&
cd NCBI01-Gill-W/NCBI01-Gill-W/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$gw  && cd ../../ &&
cd NCBI01-HC-N/NCBI01-HC-N/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$hcn  && cd ../../ &&
cd NCBI01-HC-W/NCBI01-HC-W/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$hcw  && cd ../../ &&
cd NCBI01-HC-Y/NCBI01-HC-Y/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$hcy  && cd ../../ &&
cd NCBI01-HC-V/NCBI01-HC-V/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$hcv  && cd ../../ &&
cd NCBI01-LY-N/NCBI01-LY-N/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$lyn  && cd ../../ &&
cd NCBI01-LY-Y/NCBI01-LY-Y/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$lyy  && cd ../../ &&
cd NCBI01-LY-V/NCBI01-LY-V/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$lyv  && cd ../../ &&
cd NCBI01-WH-W/NCBI01-WH-W/ &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$whw  && cd ../../ &&
cd NCBI01-WH-N/NCBI01-WH-N &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$whn  && cd ../../ &&
cd NCBI01-WH-V/NCBI01-WH-V &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$whv  && cd ../../ &&
cd NCBI01-ML-W/NCBI01-ML-W &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$mlw  && cd ../../ &&
cd NCBI01-ML-N/NCBI01-ML-N &&
python $path/get_seq_by_ID_org.py unique_unmapped.txt $file_path/$mln  && cd ../../ &&
