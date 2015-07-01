#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import sys
catv2file = sys.argv[1]
openfile = open(catv2file, 'r')


qid = []
div20 = []
div12 = []
qrecord = []
for line in openfile:
    line_split = line.split('\t')
    qid.append(line_split[1])
    div20.append(line_split[5])
    div12.append(line_split[6].strip('\n'))
    qrecord.append(line)

uniqueid_list = [e for i, e in enumerate(qid) if qid.index(e) == i ]  # get unique records

for unidiq in uniqueid_list:
    indexes = [i for i, e in enumerate(qid) if e == unidiq]
    tmp_dic = {}
    tmp_dic2 = {}
    tmp_high = []
    ind2 = ""
    for ind in indexes:
        if tmp_dic.has_key(div20[ind]) != 1:
            tmp_dic[div20[ind]] = 1
        else:
            tmp_dic[div20[ind]] += 1

        if tmp_dic2.has_key(div12[ind]) != 1:
            tmp_dic2[div12[ind]] = 1
        else:
            tmp_dic2[div12[ind]] += 1

        tmp_high.append(div12[ind])

    if "I1" in tmp_high:
        ind2 = indexes[tmp_high.index("I1")]
    elif "I2" in tmp_high:
        ind2 = indexes[tmp_high.index("I2")]
    elif "I4" in tmp_high:
        ind2 = indexes[tmp_high.index("I4")]
    elif "I7" in tmp_high:
        ind2 = indexes[tmp_high.index("I7")]
    elif "I6" in tmp_high:
        ind2 = indexes[tmp_high.index("I6")]
    elif "U" in tmp_high:
        ind2 = indexes[tmp_high.index("U")]
    elif "I8" in tmp_high:
        ind2 = indexes[tmp_high.index("I8")]
    elif "C" in tmp_high:
        ind2 = indexes[tmp_high.index("C")]
    elif "D" in tmp_high:
        ind2 = indexes[tmp_high.index("D")]
    elif "E" in tmp_high:
        ind2 = indexes[tmp_high.index("E")]
    elif "F" in tmp_high:
        ind2 = indexes[tmp_high.index("F")]
    elif "G" in tmp_high:
        ind2 = indexes[tmp_high.index("G")]
    # print indexes
    # print tmp_dic,tmp_high,ind2

    rec = qrecord[int(ind2)].split('\t')
    outline = ""
    outline += rec[0]+"\t"+rec[1]+"\t"
    for key, value in tmp_dic.iteritems():
        outline += key + "(" + str(value) + ")|"
    outline += "\t"
    for key2, value2 in tmp_dic2.iteritems():
        outline += key2 + "(" + str(value2) + ")|"
    outline += "\t"
    outline += div12[ind2] + "\n"
    sys.stdout.write(outline)

