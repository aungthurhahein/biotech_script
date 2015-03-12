__author__ = 'aung'

# enumerate file into list
def file_read(file_handle):
    temp_list=[]
    for line in file_handle:
        temp_list.append(line.strip())
    return temp_list

clstrfile = "/home/aung/server_downloads/allpool/by_division/inv_division/cdhit_bygroup/inv_cd-hit-est_#2_bykeywords_equal"
clstr_open = open(clstrfile,'r')
clstr_list = file_read(clstr_open)
clstr_to_analyze_file = open(clstrfile+"_analyze",'w')
clstr_withknown_file = open(clstrfile+"_samedesc",'w')
known_cat = []
unknown_cat = []

for x in clstr_list:
    j = x.split('\t')
    clstid = j[0].strip()
    for k in j:
        if (k == "unknown") or (k == "AFLP") or (k == "internal transcribed spacer") or (k == "microsatellite") or\
        (k == "miRNA") or (k == "SRAP marker"):
            if clstid not in unknown_cat:
                unknown_cat.append(clstid)

for line in clstr_list:
    j = line.split('\t')
    clstid = j[0].strip()
    if clstid not in unknown_cat:
        known_cat.append(clstid)

for line in unknown_cat:
    clstr_to_analyze_file.write(line+"\n")

for line in known_cat:
    clstr_withknown_file.write(line+"\n")

print len(known_cat),len(unknown_cat)
