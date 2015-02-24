#! /usr/bin/env python
# --------------------------------------------------------------------------#
# reduce annotation report duplication by reducing text with more information
# Date: 1501015
# Usage: reduce_duplicated.py xxx.txt
# __author__ = 'atrx'
#--------------------------------------------------------------------------#

import sys
import linecache
import re

usage = "Usage %s infile" % sys.argv[0]  #specific massage for no input
try:
    annotationfile = sys.argv[1]
except:
    print usage, sys.exit(1)

annotfile = open(annotationfile, 'r')
final_result = []

for line in annotfile:
    count = count + 1
    annot_split = re.split(r'\t+', line)
    id = annot_split[1]
    annotfile2 = open(annotationfile, 'r')
    for line2 in annotfile2:
        count2 = count2 + 1
        annot_split2 = re.split(r'\t+', line2)
        id2 = annot_split2[1]

        if id.strip() == id2.strip():
            match = '.'
            line_dot = reduce(lambda count, char: count + 1 if char == match else count, line, 0)
            line_dot2 = reduce(lambda count, char: count + 1 if char == match else count, line2, 0)
            if int(line_dot) > int(line_dot2):
                if any(id in s for s in final_result):
                    break
                else:
                    final_result.append(line)
                    break
            elif int(line_dot) < int(line_dot2):
                if any(id in s for s in final_result):
                    break
                else:
                    final_result.append(line2)
                    break
            else:
                if any(id in s for s in final_result):
                    break
                else:
                    final_result.append(line)
                    break
    else:
        annotfile2.close()

for result in final_result:
    print result
