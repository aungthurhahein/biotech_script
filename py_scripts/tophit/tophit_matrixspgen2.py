#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
mapfile = sys.argv[1]

group = []
div =[]
spgen = []
count = []
NCountList = []
XCountList = []
with open(mapfile, 'r') as f1:
    for line in f1:
        line_split = line.split('\t')
        group.append(line_split[0].split('-')[0])
        div.append(line_split[0].split('-')[1])
        spgen.append(line_split[1])
        count.append(line_split[2])
        NCount = 0
        XCount = 0
        for qid in line_split[3].split(';'):
            if len(qid.split('-')) > 1:
                if qid.split('-')[1] == "N":
                    NCount += 1
                elif qid.split('-')[1] == "X":
                    XCount += 1
        print NCount,XCount,line_split
        NCountList.append(NCount)
        XCountList.append(XCount)

uniq_div = sorted(list(set(div)))
uniq_spgen = sorted(list(set(spgen)))
sys.stdout.write("Division\tSpecies/Genus\t6A\t6B\t6C\tNCount\tXCount\tTotal(N+X)|(A+B+C)\n")
for d in uniq_div:
    div_ind = [i for i,e in enumerate(div) if e == d]
    # by div
    tmp_6A = []
    tmp_6Agen = []
    tmp_6Acount = []
    tmp_6B = []
    tmp_6Bgen = []
    tmp_6Bcount = []
    tmp_6C = []
    tmp_6Cgen = []
    tmp_6Ccount = []
    Atmp_NCount = []
    Atmp_XCount = []
    Btmp_NCount = []
    Btmp_XCount = []
    Ctmp_NCount = []
    Ctmp_XCount = []
    for ind in div_ind:
        if group[ind] == "6A":
            tmp_6A.append(ind)
            tmp_6Agen.append(spgen[ind])
            tmp_6Acount.append(count[ind])
            Atmp_NCount.append(NCountList[ind])
            Atmp_XCount.append(XCountList[ind])
        elif group[ind] == "6B":
            tmp_6B.append(ind)
            tmp_6Bgen.append(spgen[ind])
            tmp_6Bcount.append(count[ind])
            Btmp_NCount.append(NCountList[ind])
            Btmp_XCount.append(XCountList[ind])
        elif group[ind] == "6C":
            tmp_6C.append(ind)
            tmp_6Cgen.append(spgen[ind])
            tmp_6Ccount.append(count[ind])
            Ctmp_NCount.append(NCountList[ind])
            Ctmp_XCount.append(XCountList[ind])
    for feat in uniq_spgen:
        tmp_str = ""
        tmptotal = 0
        tmpNCount = 0
        tmpXCount = 0
        if feat in tmp_6Agen:
            tmpi = tmp_6Agen.index(feat)
            tmp_str += tmp_6Acount[tmpi]+ "\t"
            tmptotal += int(tmp_6Acount[tmpi])
            tmpNCount += int(Atmp_NCount[tmpi])
            tmpXCount += int(Atmp_XCount[tmpi])
        else:
            tmp_str += "0" + "\t"

        if feat in tmp_6Bgen:
            tmpi = tmp_6Bgen.index(feat)
            tmp_str += tmp_6Bcount[tmpi]+ "\t"
            tmptotal += int(tmp_6Bcount[tmpi])
            tmpNCount += int(Btmp_NCount[tmpi])
            tmpXCount += int(Btmp_XCount[tmpi])
        else:
            tmp_str += "0" + "\t"

        if feat in tmp_6Cgen:
            tmpi = tmp_6Cgen.index(feat)
            tmp_str += tmp_6Ccount[tmpi]
            tmptotal += int(tmp_6Ccount[tmpi])
            tmpNCount += int(Ctmp_NCount[tmpi])
            tmpXCount += int(Ctmp_XCount[tmpi])
        else:
            tmp_str += "0"

        if tmp_str != "0\t0\t0":
            sys.stdout.write(d+"\t"+feat+ "\t"+tmp_str+"\t"+str(tmpNCount)+"\t"+str(tmpXCount)+"\t"+str(tmptotal)+"\n")

