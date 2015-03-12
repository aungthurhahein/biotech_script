__author__ = 'aung'

# enumerate file into list
def file_read(file_handle):
    temp_list=[]
    for line in file_handle:
        temp_list.append(line.strip())
    return temp_list

clstrfile = "/home/aung/server_downloads/allpool/by_division/inv_division/inv_cd-hit-est_#2_bykeywords"
clstr_open = open(clstrfile,'r')
clstr_list = file_read(clstr_open)
equal_clstr_file = open(clstrfile+"_equal",'w')
unequal_clstr_file = open(clstrfile+"_unequal",'w')
singleton_clstr_file = open(clstrfile+"_singleton",'w')
equal_count = 0
unequal_count = 0
singleton = 0

# spent 20 minutes for this
def all_same(items):
    return all(x == items[0] for x in items)

for x in clstr_list:
    clst_split = x.split('\t')

    if len(clst_split) > 2:
        yesorno = all_same(clst_split[1:])
        print clst_split,yesorno
        if yesorno == 1:
            equal_clstr_file.write(x+"\n")
            equal_count += 1
        else:
            unequal_clstr_file.write(x+"\n")
            unequal_count += 1
    else:
        singleton_clstr_file.write(x+"\n")
        singleton += 1

print singleton, equal_count, unequal_count
