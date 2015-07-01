#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
infile = sys.argv[1]

queryid = []
species = []
genus = []
group = []
with open(infile,'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        queryid.append(line_split[3].strip('\n'))
        species.append(line_split[1])
        genus.append(line_split[1].split()[0])
        group.append(line_split[0])


unique_group = list(set(group))  # uniquify list and return as list
unique_genus = list(set(genus))
final_res = []
for grp in unique_group:
    group_ind = [i for i, e in enumerate(group) if grp == e]
    for g in group_ind:
        temp_genus = genus[g]
        for ge in unique_genus:
            if ge == temp_genus:
                genus_ind = [i for i, e in enumerate(genus) if temp_genus == e and group[i] == grp]
                tmp_query = []
                tmp_str = ""
                for final in genus_ind:
                    if queryid[final] not in tmp_query:
                        tmp_query.append(queryid[final].rstrip(';'))
                tmp_rec = ""
                count = 0
                for rec in list(set(tmp_query)):
                    rec_split = rec.split(';')
                    for l in rec_split:
                        tmp_rec += l+";"
                        count += 1
                tmp_str += grp + "\t" + ge.strip('\n') + "\t" + str(count) + "\t" + tmp_rec+"\n"
                if tmp_str not in final_res:
                    final_res.append(tmp_str)


unique_res = list(set(final_res))

for x in final_res:
    sys.stdout.write(x)