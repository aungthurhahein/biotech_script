"""
#----------------------------------------#
#convert fastq sequence header into pair(/1,/2) format without Biopython
#usage change_header_fastq.py file1.fastq file2.fastq
# __author__ = 'atrx'
# Date: 22122014
#----------------------------------------#
"""
import sys

# read 2 fastq files
file1 = sys.argv[1]
file2 = sys.argv[2]

# open the files
file_read1 = open(file1)
file_read2 = open(file2)

# create 2 files
firstpair = open("{0}_1fmt.fastq".format(file1), "w")
secondpair = open("{0}_2fmt.fastq".format(file2), "w")

for line in file_read1:
    if ("@" in line) or ("+" in line):
        headerid = line.split(" ")
        id = "{0}/1".format(headerid[0])
        firstpair.write("{0} {1} {2}".format(id, headerid[1], headerid[2]))
    else:
        firstpair.write(line)

for line in file_read2:
    if ("@" in line) or ("+" in line):
        headerid = line.split(" ")
        id = "{0}/2".format(headerid[0])
        secondpair.write("{0} {1} {2}".format(id, headerid[1], headerid[2]))
    else:
        secondpair.write(line)

