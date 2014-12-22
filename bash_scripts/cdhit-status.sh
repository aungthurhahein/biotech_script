#!/bin/bash
#wrapper for cd_hit_Clstr_stat.py

for f in  *.clstr
do
    cd_hit_Clstr_stat.py -i $f > $f.stat
done
