#!/usr/bin/env bash
# files nned
blastparse="stepFe0106input.fasta_out.clstr.parse"
blastrep="stepFe0106input.fasta_out.clstr.rep"
descriptionfile="/fs/home/card/Aung/Known/Fknown20150820/description/Fknown20150820_astran.desc.uniq"
lenfile="stepFe0106input.fasta_lngth"
C_Clst="C_representativeseq_G2-kShort_S2_cluster.txt"
idmap="/fs/home/card/Assembly/AsTranIDs/E01/e01_pv_cap97_idmap.txt"
G2clust="stepFe0106input.fasta_out.clstr.parse_G2"
org_trinity_fasta="nonC_Trinity.fasta_trinity.fasta"
#_--------------------------------_#
longext="_G2_flong"
shortext="_G2_fshrot"
S1ext="_trinityID_S1"
S2ext="_trinityID_S2"
flongclust=$G2clust$longext
fshortclust=$G2clust$shortext
fS1=$blastparse$S1ext
fS2=$blastparse$S2ext


mkdir summaryfiles
python py/cdhit-classifier.py $blastparse
python py/compare_len.py $G2clust $lenfile
python py/foundF_Desc.py $flongclust $lenfile $descriptionfile > summaryfiles/F_G2-fLong.description
python py/foundF_Desc.py $fshortclust $lenfile $descriptionfile > summaryfiles/F_G2-fShort.description
python py/Frepseq_mem_g2f.py $blastrep $flongclust flong > summaryfiles/F_representativeseq_G2-fLong.txt
python py/Frepseq_mem_g2f.py $blastrep $fshortclust fshort > summaryfiles/F_representativeseq_G2-fShort_S2.txt

#need to change id in scripts
python py/stpF-ClstexpandC.py $C_Clst summaryfiles/F_G2-fLong.description $idmap > summaryfiles/G2-fLong.description.allCmembers
python py/stpF-ClstexpandC.py $C_Clst summaryfiles/F_G2-fShort.description $idmap > summaryfiles/G2-fShort.description.allCmembers

#fastafiles
python py/idprint.py $flongclust > flongall.id
python py/idprint.py $fshortclust > fshortall.id
python py/idprint.py $fS1 > fS1.id
python py/idprint.py $fS2 > fS2.id
python /fs/home/card/bin/get_fasta_seq_byid.py flongall.id $org_trinity_fasta
python /fs/home/card/bin/get_fasta_seq_byid.py fshortall.id  $org_trinity_fasta
python /fs/home/card/bin/get_fasta_seq_byid.py fS1.id  $org_trinity_fasta
python /fs/home/card/bin/get_fasta_seq_byid.py fS2.id  $org_trinity_fasta

mv flongall.id.fasta summaryfiles/F_foundF_Trinity.fasta
cat fshortall.id.fasta  > summaryfiles/nonF.id.fasta
cat fS1.id.fasta >> summaryfiles/nonF.id.fasta
cat fS2.id.fasta >> summaryfiles/nonF.id.fasta

python /fs/home/card/bin/AsTranid_Convert.py summaryfiles/nonF.id.fasta $idmap