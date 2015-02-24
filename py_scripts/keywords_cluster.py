__author__ = 'aung'

# enumerate file into list
def file_read(file_handle):
    temp_list=[]
    for line in file_handle:
        temp_list.append(line)
    return temp_list

clstrfile = "/home/aung/server_downloads/allpool/by_division/inv_division/inv_cd-hit-est_#1_bykeywords"
clstr_open = open(clstrfile,'r')
clstr_list = file_read(clstr_open)

for x in clstr_list:
    clst_split = x.split('\t')
    if len(clst_split) > 2:
        for line in range(len(clst_split)):
            print range(len(clst_split))
        # for line in clst_split[1:]: