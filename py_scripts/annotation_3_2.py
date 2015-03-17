"""
# mapped annotaion between 3 sample DE result and 2 sample pairwise comparison
# Dev: Aung ေအာင်သူရဟိန်း
# 11032015
__author__ = 'Aung ေအာင်သူရဟိန်း'
"""
import sys

annotation_2_file = sys.argv[1]
annotation_3_file = sys.argv[2]
p_value = sys.argv[3]

annotation_3_open = open(annotation_3_file, 'r')
annotation_2_open = open(annotation_2_file, 'r')
id_map = open("/home/aung/server_downloads/c01_3-2_annotationMap/c01_mira/pvalue-id.map",'a')

annotation_3_idlist = []
annotation_3_all = []
annotation_2_idlist = []
annotation_2_all = []

final_list = []

for line in annotation_3_open:
    line_split = line.split('\t')
    annotation_3_idlist.append(line_split[0].strip())
    annotation_3_all.append(line)

for line in annotation_2_open:
    line_split = line.split('\t')
    annotation_2_idlist.append(line_split[2].strip())
    annotation_2_all.append(line)

for id_3 in annotation_3_idlist:
        # look bad but work
        indices = [i for i, x in enumerate(annotation_2_idlist) if x == id_3]
        # annot_3index = annotation_3_idlist.index(id_3) # only got the first one if there is 2 columns with same ids
        annot_3index2 = [i for i, x in enumerate(annotation_3_idlist) if x == id_3]
        if len(indices) >= 1:
            for ind in indices:
                for annot3_ind in annot_3index2:
                    output = annotation_3_all[annot3_ind].strip()+"\t"+annotation_2_all[ind].strip()
                    if output not in final_list:
                        final_list.append(output)
                        id_map.write(id_3+"\t"+p_value+"\n")
        else:
            for annot3_ind in annot_3index2:
                output = annotation_3_all[annot3_ind].strip()
                if output not in final_list:
                    final_list.append(output)
for x in final_list:
    print x