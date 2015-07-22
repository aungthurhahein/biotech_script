#!/usr/bin/env bash
# to get summary status of Trinotate Step-A

echo "transdecoder output"
grep '>' *.transdecoder.pep | awk '{split($0,a,"|"); print a[1]}' | sort | uniq -c | wc -l
grep '>' *.transdecoder.pep | wc -l

echo "Hmmscan"
expr $(cat TrinotatePFAM.out | awk '{split($4,a,"|"); print a[1]}' | sort -u | wc -l) - 11
expr $(cat TrinotatePFAM.out | wc -l) - 13

echo "SignalP"
expr $(cat signalp.out | awk '{split($0,a,"|"); print a[1]}'| sort -u | wc -l) - 3
expr $(cat signalp.out | wc -l) - 3

echo "TmHmm"
wc -l tmhmm.out

echo "RNammer"
cat *fasta.rnammer.gff | awk '{print $1}' | sort -u | wc -l
wc -l *fasta.rnammer.gff
