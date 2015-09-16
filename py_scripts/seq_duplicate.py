"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys

allrecordfile = sys.argv[1]
uniqfile = sys.argv[2]

species = []
org_id = []
sequence = []

with open(allrecordfile,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        species.append(line_split[1])
        org_id.append(line_split[2])
        sequence.append(line_split[3].strip('\n'))

with open(uniqfile,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        uniqid = line2_split[0]
        ind = [i for i,e in enumerate(sequence) if e == line2_split[1].strip('\n')]
        tmp_sp = ""
        tmp_org = ""
        if len(ind) == 1:
            for i in ind:
                if tmp_sp == "":
                    tmp_sp = species[i]
                    tmp_org = org_id[i]
                else:
                    tmp_sp += ";"+species[i]
                    tmp_org += ":"+org_id[i]
            sys.stdout.write(uniqid+'\t'+tmp_sp+'\t'+tmp_org+'\t'+line2_split[1])
