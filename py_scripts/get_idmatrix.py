import sys

Canu_other = "Canu_other.id2"
Fal_other = "FALCON_other.id2"
Hgap_other = "HGAP_other.id2"
Canu_noblast = "Canu.fasta_astran.fasta.blstn_scal_qcov.noblast.id"
Fal_noblast = "FALCON.fasta_astran.fasta.blstn_scal_qcov.noblast.id"
Hgap_noblast = "HGAP.fasta_astran.fasta.blstn_scal_qcov.noblast.id"

def file_read_line(fileinput):
    file_list = []
    with open(fileinput,'rb') as f1:
        for line in f1:
            file_list.append(line.strip('\n'))
    return file_list

Canu_other_lst = file_read_line(Canu_other)
Fal_other_lst = file_read_line(Fal_other)
Hgap_other_lst = file_read_line(Hgap_other)
Canu_noblast_lst = file_read_line(Canu_noblast)
Fal_noblast_lst = file_read_line(Fal_noblast)
Hgap_noblast_lst = file_read_line(Hgap_noblast)

uniqid = list(set(Canu_other_lst+Fal_other_lst+Hgap_other_lst+Canu_noblast_lst+Fal_noblast_lst+Hgap_noblast_lst))

for x in uniqid:
	tmp = x
	if x in Canu_other_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	if x in Fal_other_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	if x in Hgap_other_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	if x in Canu_noblast_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	if x in Fal_noblast_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	if x in Hgap_noblast_lst:
		tmp += "\t"+"Y"
	else:
		tmp += "\t"+"-"
	sys.stdout.write(tmp+"\n")
	