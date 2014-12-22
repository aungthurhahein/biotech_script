#----------------------------------------#
# convert fastq sequence header into pair format
# __author__ = 'atrx'
# Date: 19122014
#----------------------------------------#
import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

file = sys.argv[1]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                final_records=[]
for seq_record in SeqIO.parse(file, "fastq"):
    print seq_record.format("fastq")
    #read header
    header =seq_record.id
    #add /1 at the end
    header ="{0}/1".format(header)
    # print(repr(seq_record.seq))
    record = SeqRecord(seq_record.seq,id=header,description=seq_record.description)
    final_records.append(record)
SeqIO.write(final_records, "my_example.fastq", "fastq")