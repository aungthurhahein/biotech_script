import sys

mainfile= sys.argv[1]
libfile= sys.argv[2]
lib_id=[]
lib_count=[]

def read_file(file_handle):
  file_open = open(file_handle,'r')
  tmp_list = []
  for line in file_open:
    main_id = line.split()
    tmp_list.append(main_id[1].strip())
  return sorted(tmp_list)

def read_file2(file_handle):
  file_open = open(file_handle,'r')
  for line in file_open:
    id_split = line.split()
    lib_id.append(id_split[1].strip())
    lib_count.append(id_split[0].strip())

main_list = read_file(mainfile)
read_file2(libfile)

for line in main_list:
  if line in lib_id:
    ind = lib_id.index(line)
    print line, lib_count[ind]
  else:
    print line,"0"


