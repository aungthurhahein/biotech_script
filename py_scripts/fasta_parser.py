#-------------------------------------------------------------------------#
# fasta parser
# date: 29.10.2014
# __author__ = 'atrx'
#-------------------------------------------------------------------------#
from Bio import SeqIO

# file validation
def filetype_validation(f):
    if f == "q":
        filetype = "fastq"
    elif f == "a":
        filetype = "fasta"
    else:
        "please type q or a for fastq and fasta filetype"
    return filetype


print("Is it fastq or fasta(q/a) file?")
fastqora = raw_input(">")

filetype= filetype_validation(fastqora)


for seq_record in SeqIO.parse("t1.fastq", filetype):
    print(seq_record.id)
    print(repr(seq_record.seq))