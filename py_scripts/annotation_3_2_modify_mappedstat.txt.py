__author__ = 'Aung ေအာင်သူရဟိန်း'
import sys

annotation_2_file = sys.argv[1]
pvaluemap_file = sys.argv[2]

annotation_2_open = open(annotation_2_file, 'r')
pvaluemap_open = open(pvaluemap_file, 'r')

p_id = []
p_value = []
annotation_list = []
annotation_id = []
for x in pvaluemap_open:
    x_split = x.split("\t")
    p_id.append(x_split[0].strip())
    p_value.append(x_split[1].strip())

for line in annotation_2_open:
    annot2_split = line.split('\t')
    annotation_id.append(annot2_split[2].strip())
    annotation_list.append(line.strip('\n'))

for ind, pid in enumerate(p_id):
    indices = [i for i, x in enumerate(annotation_id) if x == pid]
    for indx in indices:
        annotation_list[indx] += "\t"+p_value[ind]
for x in annotation_list:
    print x