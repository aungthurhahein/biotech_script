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
    blastn.append(line_split[15].strip())
    blastx.append(line_split[16].strip('\n').strip())
print "QueryID\tBlastN\tBlastX\tQueryCatX\tQueryCatCX\tQueryCatCQ\tQueryCatQ"
for x, qid in enumerate(queryid):
    tmp = ""
    # 2.1 QueryCatX
    if blastx[x] != "-":
        tmp += "\t"+blastx[x]+"(X)"
    else:
        tmp += "\t"+blastn[x]+"(N)"
    xrec = blastx[x].strip('\n')
    nrec = blastn[x].strip('\n')
    # 2.2 QueryCatCX
    xc_prot = blastx[x].split('-')[0]
    nc_prot = blastn[x].split('-')[0]
    if xc_prot == nc_prot:
        tmp += "\t"+ xrec+"(X)"
    elif xc_prot == "6B":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6B":
        tmp += "\t" + nrec+"(N)"
    elif xc_prot == "6C":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6C":
        tmp += "\t" + nrec+"(N)"
    elif xc_prot == "6A":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6A":
        tmp += "\t" + nrec+"(N)"
    else:
        tmp += "\t" + xrec+"(X)"

    querycat = {"I1":1,"I2":2,"I4":3,"I7":4,"I6":5,"U":6,"I8":7,"C":8,"D":9,"E":10,"F":11,"G":12}

    # 2.3 QueryCatCQ
    if len(blastx[x].split('-')) > 1:
        xcq_prot = blastx[x].split('-')[1]
        if xcq_prot in querycat:
            xcq = querycat[xcq_prot]
        else:
            xcq_prot = "-"
            xcq = 0
    else:
        xcq_prot = "-"
        xcq = 0
    if len(blastn[x].split('-')) > 1:
        ncq_prot = blastn[x].split('-')[1]
        if ncq_prot in querycat:
            ncq = querycat[ncq_prot]
        else:
            ncq_prot = "-"
            ncq = 0
    else:
        ncq_prot = "-"
        ncq = 0

    if xc_prot == nc_prot:
        if xcq_prot == ncq_prot:
            tmp += "\t" + xrec+"(X)"
        elif xcq < ncq:
            tmp += "\t" + xrec+"(X)"
        elif xcq > ncq:
            tmp += "\t" + nrec+"(N)"
        else:
            tmp += "\t" + xrec+"(X)"
    elif xc_prot == "6B":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6B":
        tmp += "\t" + nrec+"(N)"
    elif xc_prot == "6C":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6C":
        tmp += "\t" + nrec+"(N)"
    elif xc_prot == "6A":
        tmp += "\t" + xrec+"(X)"
    elif nc_prot == "6A":
        tmp += "\t" + nrec+"(N)"
    elif xc_prot == "-":
        tmp += "\t" + nrec+"(N)"
    elif nc_prot == "-":
        tmp += "\t" + xrec+"(X)"
    else:
        tmp += "\t" + xrec+"(X)"

    # 2.4 QueryCatQ
    if xcq == ncq:
        tmp += "\t" + xrec+"(X)"
    elif xcq < ncq:
        tmp += "\t" + xrec+"(X)"
    elif xcq > ncq:
        tmp += "\t" + nrec+"(N)"
    else:
        tmp += "\t" + xrec+"(X)"

    sys.stdout.write(qid+"\t"+blastn[x]+"\t"+blastx[x]+tmp+"\n")
