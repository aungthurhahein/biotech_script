#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
catMap = sys.argv[1]

queryid = []
group = []
species = []
NX = []
with open(catMap,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        queryid.append(line_split[0])
        group.append(line_split[1])
        species.append(line_split[5])
        NX.append(line_split[2])
unique_group = list(set(group))  # uniquify list and return as list
unique_species = list(set(species))

final_res = []
for grp in unique_group:
    group_ind = [i for i,e in enumerate(group) if grp == e]
    for g in group_ind:
        temp_species = species[g]
        for sp in unique_species:
            if sp == temp_species:
                species_ind = [i for i, e in enumerate(species) if temp_species == e and group[i] == grp]
                tmp_query = []
                tmp_str = ""
                for final in species_ind:
                    if queryid[final] not in list(set(tmp_query)):
                        tmp_query.append(queryid[final]+"-"+NX[final])
                tmp_str += grp + "\t" + sp.strip('\n')+"\t"+str(len(tmp_query)) +"\t"
                for pr in tmp_query:
                    tmp_str += pr+';'
                tmp_str += '\n'
                if tmp_str not in final_res:
                    final_res.append(tmp_str)

unique_res = list(set(final_res))

for x in final_res:
    sys.stdout.write(x)