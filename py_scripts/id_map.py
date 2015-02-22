import sys

orgfile= sys.argv[1]
libfile= sys.argv[2]
org_open = open(orgfile,'r')
lib_open = open(libfile,'r')

org_id=[]
org_PM_id=[]

ref_id=[]
ref_contig_id=[]

for line in org_open:
  main_id = line.split()
  org_PM_id.append(main_id[1].strip())
  org_id.append(main_id[2].strip())

for x in lib_open:
  x_split=x.split()
  split_again=x_split[0].split('>')
  ref_id.append(split_again[1].strip())
  ref_contig_id.append(x_split[1].strip())

for count,org_pm in enumerate(org_PM_id):
  if org_pm in ref_id:
    ind = ref_id.index(org_pm)
    # PM #OrgId #contig
    print org_pm,"\t",org_id[count],"\t",ref_contig_id[ind]
