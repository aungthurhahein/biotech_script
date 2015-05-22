#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
Cal = sys.argv[1]
C1 = sys.argv[2]
C2 = sys.argv[3]
openCal = open(Cal, 'r')
openC1 = open(C1, 'r')
openC2 = open(C2, 'r')

cal_id = []
c1_id = []
c2_id = []
cal_div = []
c1_div = []
c2_div = []

for cal in openCal:
    cal_split = cal.split('\t')
    cal_id.append(cal_split[0].strip())
    cal_div.append(cal_split[1].strip())
for cal1 in openC1:
    cal1_split = cal1.split('\t')
    c1_id.append(cal1_split[0].strip())
    c1_div.append(cal1_split[1].strip())
for cal2 in openC2:
    cal2_split = cal2.split('\t')
    c2_id.append(cal2_split[0].strip())
    c2_div.append(cal2_split[1].strip())


print 'Query\tCal_Divistion\tC1_Division\tC2_Division'
for x, cal in enumerate(cal_id):
    sys.stdout.write(cal)
    sys.stdout.write('\t')
    sys.stdout.write(cal_div[x])
    sys.stdout.write('\t')
    if cal in c1_id:
        ind = c1_id.index(cal)
        sys.stdout.write(c1_div[ind])
        sys.stdout.write('\t')
        del c1_id[ind]
        del c1_div[ind]
    else:
        sys.stdout.write('-')
        sys.stdout.write('\t')
    if cal in c2_id:
        ind2 = c2_id.index(cal)
        sys.stdout.write(c2_div[ind2])
        sys.stdout.write('\t')
        del c2_id[ind2]
        del c2_div[ind2]
    else:
        sys.stdout.write('-')
        sys.stdout.write('\t')
    sys.stdout.write('\n')



# cleancal = {}

#Cal
# for x, calid in enumerate(cal_id):
#     indices = [i for i, x in enumerate(cal_id) if x == calid]
#     tmp = []
#     for ind in indices:
#         if cal_div[ind] not in tmp:
#             tmp.append(cal_div[ind])
#     if calid not in cleancal:
#         cleancal[calid] = tmp
#
# for key, value in cleancal.iteritems():
#     sys.stdout.write(key)
#     sys.stdout.write('\t')
#     for x in value:
#         sys.stdout.write(x)
#         if len(value) > 1:
#             sys.stdout.write('|')
#     sys.stdout.write('\n')


# for x, calid in enumerate(c1_id):
#     indices = [i for i, x in enumerate(c1_id) if x == calid]
#     tmp = []
#     for ind in indices:
#         if c1_div[ind] not in tmp:
#             tmp.append(c1_div[ind])
#     if calid not in cleancal:
#         cleancal[calid] = tmp
#
# for key, value in cleancal.iteritems():
#     sys.stdout.write(key)
#     sys.stdout.write('\t')
#     for x in value:
#         sys.stdout.write(x)
#         if len(value) > 1:
#             sys.stdout.write('|')
#     sys.stdout.write('\n')
#
#
# for x, calid in enumerate(c2_id):
#     indices = [i for i, x in enumerate(c2_id) if x == calid]
#     tmp = []
#     for ind in indices:
#         if c2_div[ind] not in tmp:
#             tmp.append(c2_div[ind])
#     if calid not in cleancal:
#         cleancal[calid] = tmp
#
# for key, value in cleancal.iteritems():
#     sys.stdout.write(key)
#     sys.stdout.write('\t')
#     for x in value:
#         sys.stdout.write(x)
#         if len(value) > 1:
#             sys.stdout.write('|')
#     sys.stdout.write('\n')
