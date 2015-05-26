#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
updatefile = sys.argv[1]
updatefile2 = sys.argv[2]
matrixfile = sys.argv[3]

openupdatefile = open(updatefile, 'r')  # used file to update C01_MIRA
openupdatefile2 = open(updatefile2, 'r')  # trinity
openmatrixfile = open(matrixfile, 'r')  # matrix to update

update_id = []
update_cms = []
for line in openupdatefile:
    line_split = line.split()
    if len(line_split) > 1:
        update_id.append(line_split[0].strip())
        update_cms.append(line_split[1:])

update_trinid = []
update_tincms = []
for line3 in openupdatefile2:
    line3_split = line3.split()
    if len(line3_split) > 1:
        update_trinid.append(line3_split[0].strip())
        update_tincms.append(line3_split[1:])


matrix_id = []
matrix_records = []
for line2 in openmatrixfile:
    line2_split = line2.split('\t')
    id_split = line2_split[3].split('|')
    if len(id_split) > 1:
        matrixid = id_split[1].strip('>').strip()
    else:
        matrixid = id_split[0].strip()
    matrix_id.append(matrixid)
    matrix_records.append(line2.strip())

for x, maxid in enumerate(matrix_id):
    record_split = matrix_records[x].split('\t')
    # look at mira
    if maxid in update_id and record_split[2].strip() == 'C01_MIRA':
        ind = update_id.index(maxid)
        for col in record_split:
            sys.stdout.write(col)
            sys.stdout.write('\t')
        for col2 in update_cms[ind]:
            sys.stdout.write(col2)
            sys.stdout.write('\t')
        sys.stdout.write('\n')
    elif maxid.strip('>') in update_trinid and record_split[2].strip() == 'C01_Trinity':
        ind = update_trinid.index(maxid.strip('>'))
        for col in record_split:
            sys.stdout.write(col)
            sys.stdout.write('\t')
        for col2 in update_tincms[ind]:
            sys.stdout.write(col2)
            sys.stdout.write('\t')
        sys.stdout.write('\n')
    else:
        record_split = matrix_records[x].split('\t')
        for col in record_split:
            sys.stdout.write(col)
            sys.stdout.write('\t')
        sys.stdout.write('\n')