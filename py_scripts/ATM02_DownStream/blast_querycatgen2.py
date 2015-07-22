#! /usr/bin/env/ python
"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
ifile = sys.argv[1]
openfile = open(ifile, 'r')
queryid = []
blastn = []
blastx = []
for line in openfile:
    line_split = line.split('\t')
    queryid.append(line_split[0].strip())
    blastn.append(line_split[9].strip())
    blastx.append(line_split[10].strip('\n').strip())
print "QueryID\tBlastN\tBlastX\tQueryCatX\tQueryCatCX\tQueryCatCQ\tQueryCatQ"
for x, qid in enumerate(queryid):
    tmp = ""
    # 2.1 QueryCatX
    if blastx[x] != "-":
        tmp += "\t"+blastx[x]
    else:
        tmp += "\t"+blastn[x]
    xrec = blastx[x].strip('\n')
    nrec = blastn[x].strip('\n')
    # 2.2 QueryCatCX
    xc_prot = blastx[x].split('-')[0]
    nc_prot = blastn[x].split('-')[0]
    if xc_prot == nc_prot:
        tmp += "\t"+ xrec
    elif xc_prot == "6B":
        tmp += "\t" + xrec
    elif nc_prot == "6B":
        tmp += "\t" + nrec
    elif xc_prot == "6C":
        tmp += "\t" + xrec
    elif nc_prot == "6C":
        tmp += "\t" + nrec
    elif xc_prot == "6A":
        tmp += "\t" + xrec
    elif nc_prot == "6A":
        tmp += "\t" + nrec
    else:
        tmp += "\t" + xrec
    querycat = {"I1":1,"I2":2,"I4":3,"I7":4,"I6":5,"U":6,"I8":7,"C":8,"D":9,"E":10,"F":11,"G":12}

    # 2.3 QueryCatCQ
    if len(blastx[x].split('-')) > 1:
        xcq_prot = blastx[x].split('-')[1]
        if xcq_prot in querycat:
            xcq = querycat[xcq_prot]
        else:
            xcq_prot = "-"
            xcq = 13
    else:
        xcq_prot = "-"
        xcq = 13
    if len(blastn[x].split('-')) > 1:
        ncq_prot = blastn[x].split('-')[1]
        if ncq_prot in querycat:
            ncq = querycat[ncq_prot]
        else:
            ncq_prot = "-"
            ncq = 13
    else:
        ncq_prot = "-"
        ncq = 13

    if xc_prot == nc_prot:
        if xcq_prot == ncq_prot:
            tmp += "\t" + xrec
        elif xcq < ncq:
            tmp += "\t" + xrec
        elif xcq > ncq:
            tmp += "\t" + nrec
        else:
            tmp += "\t" + xrec
    elif xc_prot == "6B":
        tmp += "\t" + xrec
    elif nc_prot == "6B":
        tmp += "\t" + nrec
    elif xc_prot == "6C":
        tmp += "\t" + xrec
    elif nc_prot == "6C":
        tmp += "\t" + nrec
    elif xc_prot == "6A":
        tmp += "\t" + xrec
    elif nc_prot == "6A":
        tmp += "\t" + nrec
    elif xc_prot == "-":
        tmp += "\t" + nrec
    elif nc_prot == "-":
        tmp += "\t" + xrec
        if ncq_prot in querycat:
            ncq = querycat[ncq_prot]
        else:
            ncq_prot = "-"
            ncq = 13
    else:
        ncq_prot = "-"
        ncq = 13

    if xc_prot == nc_prot:
        if xcq_prot == ncq_prot:
            tmp += "\t" + xrec
        elif xcq < ncq:
            tmp += "\t" + xrec
        elif xcq > ncq:
            tmp += "\t" + nrec
        else:
            tmp += "\t" + xrec
    elif xc_prot == "6B":
        tmp += "\t" + xrec
    elif nc_prot == "6B":
        tmp += "\t" + nrec
    elif xc_prot == "6C":
        tmp += "\t" + xrec
    elif nc_prot == "6C":
        tmp += "\t" + nrec
    elif xc_prot == "6A":
        tmp += "\t" + xrec
    elif nc_prot == "6A":
        tmp += "\t" + nrec
    elif xc_prot == "-":
        tmp += "\t" + nrec
    elif nc_prot == "-":
        tmp += "\t" + xrec
    else:
        tmp += "\t" + xrec

    # 2.4 QueryCatQ
    if xcq == ncq:
        tmp += "\t" + xrec
    elif xcq < ncq:
        tmp += "\t" + xrec
    elif xcq > ncq:
        tmp += "\t" + nrec
    else:
        tmp += "\t" + xrec

    sys.stdout.write(qid+"\t"+blastn[x]+"\t"+blastx[x]+tmp+"\n")
