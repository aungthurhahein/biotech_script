#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys

v1file = sys.argv[1]
openv1file = open(v1file, 'r')

base = "/fs/home/card/LinWork/atm/taxon_divlist/blastx_div/"
updatefile = base+"taxonID.blastx.ov.lst_group.no20div.lst.div"
open_update = open(updatefile,'r')
oldid = []
newid = []
desc = []
sp = []
div = []
f = open('update_log','w')
for line in open_update:
    line_split = line.split('\t')
    oldid.append(line_split[0])
    newid.append(line_split[1])
    desc.append(line_split[2])
    sp.append(line_split[3])
    div.append(line_split[4].strip('\n'))

old_id = []
new_id = []
v1_line = []
div20 = []
for line2 in openv1file:
    line2_split = line2.split('\t')
    old_id.append(line2_split[0])
    new_id.append(line2_split[1])
    div20.append(line2_split[5].strip('\n'))
    v1_line.append(line2.strip('\n'))

for x, taxid in enumerate(old_id):
    if new_id[x] == "":
        if taxid in oldid:
            f.write(taxid+'\n')
            ind = oldid.index(taxid)
            sys.stdout.write(oldid[ind])
            sys.stdout.write('\t')
            sys.stdout.write(newid[ind])
            sys.stdout.write('\t')
            sys.stdout.write(desc[ind])
            sys.stdout.write('\t')
            sys.stdout.write(sp[ind])
            sys.stdout.write('\t')
            sys.stdout.write(div[ind])
            sys.stdout.write('\t')
            sys.stdout.write(div20[x])
            sys.stdout.write('\n')
        else:
            sys.stdout.write(v1_line[x])
            sys.stdout.write('\n')
    else:
        sys.stdout.write(v1_line[x])
        sys.stdout.write('\n')

