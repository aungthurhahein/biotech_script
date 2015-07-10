#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import codesnippets
ATM = sys.argv[1]
base="/fs/home/card/Aung/ATM02-Task13-B/"
A1 = base+"ATM02-A11.fasta_out.clstr_parse2.id"
A2 = base+"ATM02-A12.fasta_out.clstr_parse2.id"
A3 = base+"ATM02-A13.fasta_out.clstr_parse2.id"
A4 = base+"ATM02-A14.fasta_out.clstr_parse2.id"
A5 = base+"ATM02-A15.fasta_out.clstr_parse2.id"
A6 = base+"ATM02-A16.fasta_out.clstr_parse2.id"
A7 = base+"ATM02-A17.fasta_out.clstr_parse2.id"
A8 = base+"ATM02-A18.fasta_out.clstr_parse2.id"
A9 = base+"ATM02-A19.fasta_out.clstr_parse2.id"
A10 = base+"ATM02-A110.fasta_out.clstr_parse2.id"
A11 = base+"ATM02-A111.fasta_out.clstr_parse2.id"
A12 = base+"ATM02-A112.fasta_out.clstr_parse2.id"
A13 = base+"ATM02-A113.fasta_out.clstr_parse2.id"
A14 = base+"ATM02-A114.fasta_out.clstr_parse2.id"
A15 = base+"ATM02-A115.fasta_out.clstr_parse2.id"
A16 = base+"ATM02-A116.fasta_out.clstr_parse2.id"

ATMid = codesnippets.file_read_line(ATM)
A1id = codesnippets.file_read_line(A1)
A2id = codesnippets.file_read_line(A2)
A3id = codesnippets.file_read_line(A3)
A4id = codesnippets.file_read_line(A4)
A5id = codesnippets.file_read_line(A5)
A6id = codesnippets.file_read_line(A6)
A7id = codesnippets.file_read_line(A7)
A8id = codesnippets.file_read_line(A8)
A9id = codesnippets.file_read_line(A9)
A10id = codesnippets.file_read_line(A10)
A11id = codesnippets.file_read_line(A11)
A12id = codesnippets.file_read_line(A12)
A13id = codesnippets.file_read_line(A13)
A14id = codesnippets.file_read_line(A14)
A15id = codesnippets.file_read_line(A15)
A16id = codesnippets.file_read_line(A16)

print "QueryID\tNonShrimp\tATM02-A11\tATM02-A12\tATM02-A13\tATM02-A14\tATM02-A15\tATM02-A16\tATM02-A17" \
      "\tATM02-A18\tATM02-A19\tATM02-A110\tATM02-A111\tATM02-A112\tATM02-A113\tATM02-A114\tATM02-A115\tATM02-A116"
for ATM02id in ATMid:
    A1cond = ATM02id in A1id
    A2cond = ATM02id in A2id
    A3cond = ATM02id in A3id
    A4cond = ATM02id in A4id
    A5cond = ATM02id in A5id
    A6cond = ATM02id in A6id
    A7cond = ATM02id in A7id
    A8cond = ATM02id in A8id
    A9cond = ATM02id in A9id
    A10cond = ATM02id in A10id
    A11cond = ATM02id in A11id
    A12cond = ATM02id in A12id
    A13cond = ATM02id in A13id
    A14cond = ATM02id in A14id
    A15cond = ATM02id in A15id
    A16cond = ATM02id in A16id
    tmpstr = ATM02id.strip('\n')+"\t"
    if A1cond == A2cond == A3cond == A4cond == A5cond == A6cond == A7cond == A8cond == A9cond == A10cond == A11cond == \
            A12cond == A13cond == A14cond == A15cond == A16cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A1cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A2cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A3cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A4cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A5cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A6cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A7cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A8cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A9cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A10cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A11cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A12cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A13cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A14cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A15cond:
        tmpstr += "y\t"
    else:
        tmpstr += "n\t"

    if A16cond:
        tmpstr += "y\n"
    else:
        tmpstr += "n\n"
    sys.stdout.write(tmpstr)