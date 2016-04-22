# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-29 14:58:06
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-29 15:35:53
import sys
from Bio import SeqIO
start = int(sys.argv[1])
end = int(sys.argv[2])
rmidfile = "/colossus/home/anuphap/Ortho20151125_Compare/Removeseq/rm_reg2.id"
smallfile_base="/colossus/home/anuphap/Ortho20151125_Compare/Removeseq/smallchunks-HI/RepSeq_allprot_HI."

id_list = []
with open(rmidfile,'rb') as f1:
    for l1 in f1:
        id_list.append(l1.strip('>').strip('\n'))

for i in range(start,end):
    fasta_file = smallfile_base+str(format(i+1,'04'))+".fasta"
    out_file = open(fasta_file+"flt","w")
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        id_ = str(seq_record.id)
        if id_ not in id_list:
            out_file.write(id_+"\n")
            out_file.write(str(seq_record.seq)+"\n")
