#!/bin/bash
#wrapper for cd_hit_Clstr_stat.py

for f in  *.clstr
do
    cd_hit_Clstr_stat.py -i $f > $f.stat
done

#
#ext=".id"
#in1="_ATM02_Multi"
#in2="_ATM02_Singleton"
#
#for f in *.clstr_parse2
#do
#    out=$f$ext
#    infile1=$f$in1
#    infile2=$f$in2
#    python clust_mem.py $infile1 > $out
#    python clust_mem.py $infile2 >> $out
#done
