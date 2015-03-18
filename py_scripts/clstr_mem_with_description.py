
# ~/github_repos/biotech_script$ sudo python py_scripts/clstr_mem_with_description.py ~aung/server_downloads/allpool/by_division/inv_division/cdhit_bygroup/inv_cd-hit-est_#1_bykeywords_equal_analyze ~aung/server_downloads/allpool/by_division/inv_division/inv_div_lin#1.clstr.parse2 ~aung/server_downloads/allpool/by_division/inv_division/inv_div.txt > ~aung/server_downloads/allpool/by_division/inv_division/cdhit_bygroup/inv_cd-hit-est_#1_bykeywords_equal_analyze_result

__author__ = 'Aung'
import sys
# enumerate file into list
def file_read(file_handle):
    temp_list=[]
    for line in file_handle:
        temp_list.append(line.strip())
    return temp_list

mainclsterfile= sys.argv[1]
clstr_wMember = sys.argv[2]
desc_file = sys.argv[3]

mainclstr_open = open(mainclsterfile,'r')
mainclstr_list = file_read(mainclstr_open)

clstr_open = open(clstr_wMember,'r')
clstr_list = file_read(clstr_open)

desc_open = open(desc_file,'r')
desc_id =[]
desc_description=[]
final={}
for line in desc_open:
    line_split= line.split('\t')
    desc_id.append(line_split[0].strip())
    desc_description.append(line_split[3].strip())

for clstr in clstr_list:
    clstr_split = clstr.split('\t')
    if clstr_split[0].strip() in mainclstr_list:
        print clstr_split[0]
        for clstr_mem in clstr_split[1:]:
            clstr_mem_split = clstr_mem.split('-')
            if clstr_mem_split[1].strip() in desc_id:
                tmp_indx= desc_id.index(clstr_mem_split[1].strip())
                print desc_id[tmp_indx],desc_description[tmp_indx]
                # final[clstr_split[0].strip()+"_"+desc_id[tmp_indx]] = desc_description[tmp_indx]

# for x in final:
#     print x,final[x]

