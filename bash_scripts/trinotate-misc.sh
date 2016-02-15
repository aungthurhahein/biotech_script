#!/usr/bin/env bash


python /fs/home/card/bin/trinity_withotherassembly.py -s SRR988098_out.Trinity.fasta -a ILT10 -i PV_ILT10
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR653437.Trinity.fasta -a ILT11 -i PV_ILT11
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR839222.Trinity.fasta -a ILT12 -i PV_ILT12
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037362.Trinity.fasta -a ILT13 -i PV_ILT13
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037365.Trinity.fasta -a ILT14 -i PV_ILT14
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR842625.Trinity.fasta -a ILT15 -i PV_ILT15
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR839236.Trinity.fasta -a ILT16 -i PV_ILT16
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037363.Trinity.fasta -a ILT17 -i PV_ILT17
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR842627.Trinity.fasta -a ILT18 -i PV_ILT18
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037366.Trinity.fasta -a ILT19 -i PV_ILT19
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR842572.Trinity.fasta -a ILT20 -i PV_ILT20
python /fs/home/card/bin/trinity_withotherassembly.py -s SRR1037364.Trinity.fasta -a ILT21 -i PV_ILT21
python /fs/home/card/bin/trinity_withotherassembly.py -s Trinity_SRR1039534_out.Trinity.fasta -a ILT22 -i PV_ILT22

for i in *.Trinity.fasta
do
    out="_id_map.txt"
    out2="_trinity_fmt.fasta"
    i1=$i$out
    i2=$i$out2
    python /fs/home/card/bin/AsTranid_Convert.py $i2 $i1
done


mkdir PV_ILT10_trinotate
mkdir PV_ILT11_trinotate
mkdir PV_ILT12_trinotate
mkdir PV_ILT13_trinotate
mkdir PV_ILT14_trinotate
mkdir PV_ILT15_trinotate
mkdir PV_ILT16_trinotate
mkdir PV_ILT17_trinotate
mkdir PV_ILT18_trinotate
mkdir PV_ILT19_trinotate
mkdir PV_ILT20_trinotate
mkdir PV_ILT21_trinotate
mkdir PV_ILT22_trinotate
mkdir PV_ILT23_trinotate
mkdir PV_ILT24_trinotate
mkdir PV_ILT25_trinotate
mkdir PV_ILT26_trinotate
mkdir PV_ILT27_trinotate
mkdir PV_ILT28_trinotate
mkdir PV_ILT29_trinotate
mkdir PV_ILT30_trinotate
mkdir PV_ILT31_trinotate
mkdir PV_ILT32_trinotate
mkdir PV_ILT33_trinotate
mkdir PV_ILT34_trinotate
mkdir PV_ILT35_trinotate