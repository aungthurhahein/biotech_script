#!/usr/bin/env bash


base="/fs/home/card/LinWork/byTri/e0102/stept/smallfastafile/"
map="/fs/home/card/Assembly/e01/pm/CAP97/e01_pm.fasta.fna.cap3097.contigs_id_map.txt"
pep="/fs/home/card/Aung/by_trinotate/e0102_trinotate/T/e01_pm_cap397_trinity.fasta.transdecoder.pep"


cd $base
for i in *.fasta
do
    python /fs/home/card/bin/TrinityID.Convert.py $i $map $pep
done
