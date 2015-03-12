__author__ = 'aung'

import sys

annot_mappedfile= sys.argv[1]
openannot_mappedfile = open(annot_mappedfile,'r')
annotfile_list=[]
all_id =[]
idwith_dup={}

for x in openannot_mappedfile:
    x = x.split('\t')
    all_id.append(x[0].strip())
    annotfile_list.append(x)

def find_index(inputid):
    index_list=[]
    for ind,id in enumerate(all_id):
        if id == inputid:
            index_list.append(ind)
    return index_list

for record in annotfile_list:
    occurence = find_index(record[0].strip())
    if record[0].strip() not in idwith_dup:
        idwith_dup[record[0].strip()] = occurence

for x,v in idwith_dup.items():
    if len(v) > 1:
        for index in v:
            tmp_count = 0
            for record in annotfile_list[index]:
                record_split = record.split('\t')
                for count in record_split:
                    if count == ".":
                        tmp_count += 1

            count_with_id[x] = tmp_count

    # else:
    #     print annotfile_list[index]


