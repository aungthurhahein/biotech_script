#!/usr/bin/env python
__author__ = 'aung'
import sys
file1 = sys.argv[1]
file1_read = open(file1,'r')
outputfile = open(file1+"_uniqueseqID.txt",'w')
file1_list=[]
final_list=[]
seq_list=[]
for x in file1_read:
    file1_list.append(x)

for line in file1_list:
    line_split = line.split('\t')
    seq_id = line_split[0].strip()
    if seq_id in seq_list:
        for x, k in enumerate(final_list):
            k_split = k.split('\t')
            if k_split[0].strip() == seq_id.strip():
                print seq_id
                update = k_split[0]+"\t"+k_split[1]+"\t"+k_split[2]+"|"+line_split[2]+"\t"+k_split[3]+"|"+line_split[3]+ \
                         "\t"+k_split[4]
                final_list[x] = update
    else:
        seq_list.append(seq_id)
        final_list.append(line)

print len(final_list)
outputfile.write(res)
# for res in final_list:
#     pass