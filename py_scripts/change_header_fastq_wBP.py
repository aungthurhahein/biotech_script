#----------------------------------------#
#convert fastq sequence header into pair(/1,/2) format without Biopython
#usage change_header_fastq_wBP.py file1.fastq file2.fastq
# __author__ = 'atrx'
# Date: 23122014
#----------------------------------------#

import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

file1 = sys.argv[1];file2= sys.argv[2]
final_records=[];final_records2=[]

for seq_record in SeqIO.parse(file1, "fastq"):
    #read header
    header =seq_record.id
    #add /1 at the end
    header ="{0}/1".format(header)
    seq_record.id = header
    # record = SeqRecord(seq_record.seq,id=header,description=seq_record.description)
    #transfer
    # record.letter_annotations["phred_quality"]=seq_record.letter_annotations["phred_quality"]
    final_records.append(seq_record)
SeqIO.write(final_records,"{0}_1fmt.fastq".format(file1), "fastq")

for seq_record in SeqIO.parse(file2, "fastq"):
    #read header
    header =seq_record.id
    #add /1 at the end
    header ="{0}/2".format(header)
    seq_record.id = header
    # record = SeqRecord(seq_record.seq,id=header,description=seq_record.description)
    # record.letter_annotations["phred_quality"]=seq_record.letter_annotations["phred_quality"]
    final_records2.append(seq_record)
SeqIO.write(final_records2, "{0}_2fmt.fastq".format(file2), "fastq")