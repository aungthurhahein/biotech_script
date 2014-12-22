#!/bin/bash
#loop the files and get trinity.fasta status
for f in  *.fasta
do
        /share/apps/trinityrnaseq_r20140717/util/TrinityStats.pl $f > $f.stat
done

