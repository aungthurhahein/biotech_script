__author__ = 'aung'
file1="/home/aung/server_downloads/c01_MIRA_CDHIT/mira_org_trinity.txt"
file_read= open(file1,'r')
id_map=[]
for i in file_read:
    id_map.append(i)
for x in id_map:
    x_split = x.split('\t')
    id = x_split[1].split()
    print x_split[0].strip(),'\t',
    final_id =id[0].split('_')
    print "{0}_{1}".format(final_id[0],final_id[1])

