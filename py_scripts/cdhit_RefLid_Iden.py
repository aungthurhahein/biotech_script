#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date:
python ../cluster_identify.py ../ids_cdhit/HC_uniquemappedRef.txt.uniq ../ids_cdhit/HC_unmappedRefID.txt.uniq ../ids_cdhit/HC_unmappedLibID.txt.uniq

"""
import sys
import codesnippets

mapped_ref = sys.argv[1]   # mapped_ref
unmapped_ref = sys.argv[2]  # unmapped_ref
unmapped_lib = sys.argv[3]  # unmapped_lib
clstrfile = sys.argv[4]     # parsed cluster file

clstrfile_read = open(clstrfile, 'r')
mapped_ref_read = open(mapped_ref, 'r')
unmapped_ref_read = open(unmapped_ref, 'r')
unmapped_lib_read = open(unmapped_lib, 'r')

cluster_list = []
mapped_reflist = []
unmapped_reflist = []
unmapped_liblist = []

RUL_side = []
RU_Multi = []
RL_Multi = []
UL_Multi = []
R_Multi = []
U_Multi = []
L_Multi = []
R_Singleton = []
U_Singleton = []
L_Singleton = []

for line in clstrfile_read:
    cluster_list.append(line.strip())
for ref in mapped_ref_read:
    ref_split = ref.split()
    mapped_reflist.append(ref_split[1].strip())
for unref in unmapped_ref_read:
    unref_split = unref.split()
    unmapped_reflist.append(unref_split[1].strip())
for unlib in unmapped_lib_read:
    unlib_split = unlib.split()
    unmapped_liblist.append(unlib_split[1].strip())

for x in cluster_list:
    x_split = x.split('\t')
    idR_count = 0
    idU_count = 0
    idL_count = 0
    # multi
    if len(x_split) > 2:
        id_flag = range(len(x_split))
        for x_count, mem in enumerate(x_split):
            if mem.strip() in mapped_reflist:  # in R
                id_flag[x_count] = "*"
            elif mem.strip() in unmapped_reflist:  # in U
                id_flag[x_count] = "#"
            elif mem.strip() in unmapped_liblist:  # in L
                id_flag[x_count] = "&"
            else:
                print mem
        for y in id_flag:
            if y == "*":
                idR_count += 1
            elif y == "#":
                idU_count += 1
            elif y == "&":
                idL_count += 1
        if idR_count >= 1 and idU_count >= 1 and idL_count >= 1:  # G3
            RUL_side.append(x)
        elif idR_count >= 1 and idU_count >= 1 and idL_count == 0:  # G2AL
            RU_Multi.append(x)
        elif idR_count >= 1 and idU_count == 0 and idL_count >= 1:  # G2AC
            RL_Multi.append(x)
        elif idR_count == 0 and idU_count >= 1 and idL_count >= 1:  # G2LC
            UL_Multi.append(x)
        elif idR_count >= 1 and idU_count == 0 and idL_count == 0:  # S2A
            R_Multi.append(x)
        elif idR_count == 0 and idU_count >= 1 and idL_count == 0:  # S2L
            U_Multi.append(x)
        elif idR_count == 0 and idU_count == 0 and idL_count >= 1:  # S2C
            L_Multi.append(x)
        else:
            print x
    # singleton
    else:
        if x_split[1].strip() in mapped_reflist:  # R
            R_Singleton.append(x)
        elif x_split[1].strip() in unmapped_reflist:  # U
            U_Singleton.append(x)
        elif x_split[1].strip() in unmapped_liblist:  # L
            L_Singleton.append(x)

codesnippets.write_file(R_Singleton, "{0}_S1R".format(clstrfile))
codesnippets.write_file(U_Singleton, "{0}_S1U".format(clstrfile))
codesnippets.write_file(L_Singleton, "{0}_S1L".format(clstrfile))
codesnippets.write_file(R_Multi, "{0}_S2R".format(clstrfile))
codesnippets.write_file(U_Multi, "{0}_S2U".format(clstrfile))
codesnippets.write_file(L_Multi, "{0}_S2L".format(clstrfile))
codesnippets.write_file(RU_Multi, "{0}_G2RU".format(clstrfile))
codesnippets.write_file(RL_Multi, "{0}_G2RL".format(clstrfile))
codesnippets.write_file(UL_Multi, "{0}_G2UL".format(clstrfile))
codesnippets.write_file(RUL_side, "{0}_G3".format(clstrfile))
