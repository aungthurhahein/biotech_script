#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import codesnippets

cdhit98set01 = sys.argv[1]
cdhit98Share = sys.argv[2]
cdhit982 = sys.argv[3]
cdhit95 = sys.argv[4]
cdhit90 = sys.argv[5]
cdhit85 = sys.argv[6]
cdhit80 = sys.argv[7]
allid = sys.argv[8]

opencdhit_98 = open(cdhit98set01, 'r')
opencdhit_98Share = open(cdhit98Share, 'r')
opencdhit_982 = open(cdhit982, 'r')
opencdhit_95 = open(cdhit95, 'r')
opencdhit_90 = open(cdhit90, 'r')
opencdhit_85 = open(cdhit85, 'r')
opencdhit_80 = open(cdhit80, 'r')
openallid = open(allid, 'r')

list98 = codesnippets.file_read_line(opencdhit_98)
list98Share = codesnippets.file_read_line(opencdhit_98Share)
list982 = codesnippets.file_read_line(opencdhit_982)
list95 = codesnippets.file_read_line(opencdhit_95)
list90 = codesnippets.file_read_line(opencdhit_90)
list85 = codesnippets.file_read_line(opencdhit_85)
list80 = codesnippets.file_read_line(opencdhit_80)
listallid = codesnippets.file_read_line(openallid)

print 'ID\tLen\tATM01-98\tATM02-98\tATM02-95\tATM02-90\tATM02-85\tATM02-80'

for line in listallid:
    line_split = line.split('\t')
    seqid = ">"+line_split[0].strip()
    lgth = line_split[1].strip()
    sys.stdout.write(seqid)
    sys.stdout.write('\t')
    sys.stdout.write(lgth)
    sys.stdout.write('\t')

    if seqid in list98:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    elif seqid in list98Share:
        sys.stdout.write('n')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')

    if seqid in list982:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')
    if seqid in list95:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')
    if seqid in list90:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')
    if seqid in list85:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')
    if seqid in list80:
        sys.stdout.write('y')
        sys.stdout.write('\t')
    else:
        sys.stdout.write('\t')
    sys.stdout.write('\n')