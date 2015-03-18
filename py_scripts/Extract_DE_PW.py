"""
__author__ = 'Aung'
# get DE sample specific features form pairwise comparison
# Dev: Aung
# Date: 05032015
"""
import sys

lessPval = sys.argv[1]
morePval = sys.argv[2]

lessPopen = open(lessPval,'r')# less p value means more records
morePopen = open(morePval,'r')
lessp_list=[]
lessp_id =[]
morep_list=[]
morep_id=[]
final_list=[]

for line in lessPopen:
    lessp_list.append(line.strip())
    lessp_split = line.split('\t')
    lessp_id.append(lessp_split[0].strip())

for line in morePopen:
    morep_list.append(line.strip())
    morep_split = line.split('\t')
    morep_id.append(morep_split[0].strip())

# subtract list1 from list 2
tmp_list = list(set(lessp_id) - set(morep_id))

for x in tmp_list:
    tmp_indx = lessp_id.index(x)
    print lessp_list[tmp_indx]

