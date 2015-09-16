"""
#
# usage: convert csv to fasta format
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
tsv_file = sys.argv[1]
open_csv = open(tsv_file, 'r')

for line in open_csv:
    line_split = line.split('\t')
    print ">20150902Aung_"+line_split[0].strip()
    print line_split[1].strip('\n').strip()
