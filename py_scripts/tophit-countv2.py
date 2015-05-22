#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
combinefile = sys.argv[1]
opencombinefile = open(combinefile, 'r')

BI198 = 0
BI298 = 0
BI498 = 0
BI798 = 0
BI698 = 0
BI898 = 0
BU98 = 0
BC98 = 0
BD98 = 0
BE98 = 0
BF98 = 0
CI198 = 0
CI298 = 0
CI498 = 0
CI798 = 0
CI698 = 0
CI898 = 0
CU98 = 0
CB98 = 0
CC98 = 0
CD98 = 0
CE98 = 0
CF98 = 0
AI198 = 0
AI298 = 0
AI498 = 0
AI798 = 0
AI698 = 0
AI898 = 0
AU98 = 0
AB98 = 0
AC98 = 0
AD98 = 0
AE98 = 0
AF98 = 0

BI195 = 0
BI295 = 0
BI495 = 0
BI795 = 0
BI695 = 0
BI895 = 0
BU95 = 0
BC95 = 0
BD95 = 0
BE95 = 0
BF95 = 0
CI195 = 0
CI295 = 0
CI495 = 0
CI795 = 0
CI695 = 0
CI895 = 0
CU95 = 0
CB95 = 0
CC95 = 0
CD95 = 0
CE95 = 0
CF95 = 0
AI195 = 0
AI295 = 0
AI495 = 0
AI795 = 0
AI695 = 0
AI895 = 0
AU95 = 0
AB95 = 0
AC95 = 0
AD95 = 0
AE95 = 0
AF95 = 0

BI190 = 0
BI290 = 0
BI490 = 0
BI790 = 0
BI690 = 0
BI890 = 0
BU90 = 0
BC90 = 0
BD90 = 0
BE90 = 0
BF90 = 0
CI190 = 0
CI290 = 0
CI490 = 0
CI790 = 0
CI690 = 0
CI890 = 0
CU90 = 0
CB90 = 0
CC90 = 0
CD90 = 0
CE90 = 0
CF90 = 0
AI190 = 0
AI290 = 0
AI490 = 0
AI790 = 0
AI690 = 0
AI890 = 0
AU90 = 0
AB90 = 0
AC90 = 0
AD90 = 0
AE90 = 0
AF90 = 0

BI185 = 0
BI285 = 0
BI485 = 0
BI785 = 0
BI685 = 0
BI885 = 0
BU85 = 0
BC85 = 0
BD85 = 0
BE85 = 0
BF85 = 0
CI185 = 0
CI285 = 0
CI485 = 0
CI785 = 0
CI685 = 0
CI885 = 0
CU85 = 0
CB85 = 0
CC85 = 0
CD85 = 0
CE85 = 0
CF85 = 0
AI185 = 0
AI285 = 0
AI485 = 0
AI785 = 0
AI685 = 0
AI885 = 0
AU85 = 0
AB85 = 0
AC85 = 0
AD85 = 0
AE85 = 0
AF85 = 0

BI180 = 0
BI280 = 0
BI480 = 0
BI780 = 0
BI680 = 0
BI880 = 0
BU80 = 0
BC80 = 0
BD80 = 0
BE80 = 0
BF80 = 0
CI180 = 0
CI280 = 0
CI480 = 0
CI780 = 0
CI680 = 0
CI880 = 0
CU80 = 0
CB80 = 0
CC80 = 0
CD80 = 0
CE80 = 0
CF80 = 0
AI180 = 0
AI280 = 0
AI480 = 0
AI780 = 0
AI680 = 0
AI880 = 0
AU80 = 0
AB80 = 0
AC80 = 0
AD80 = 0
AE80 = 0
AF80 = 0

# write to file
# 80
f6AI6 = open("6A-I6.80", 'w')
f6AI8 = open("6A-I8.80", 'w')
f6AD = open("6A-D.80", 'w')
f6AE = open("6A-E.80", 'w')

f6BI6 = open("6B-I6.80", 'w')
f6BI8 = open("6B-I8.80", 'w')
f6BD = open("6B-D.80", 'w')
f6BE = open("6B-E.80", 'w')

f6CI6 = open("6C-I6.80", 'w')
f6CI8 = open("6C-I8.80", 'w')
f6CD = open("6C-D.80", 'w')
f6CE = open("6C-E.80", 'w')

for line in opencombinefile:
    line_split = line.split('\t')
    query_id = line_split[0].strip()
    atm98 = line_split[2].strip()
    atm95 = line_split[3].strip()
    atm90 = line_split[4].strip()
    atm85 = line_split[5].strip()
    atm80 = line_split[6].strip()
    v1_group = line_split[13].strip()  # v2

    # 98
    if v1_group == '6B-I1' and atm98 == 'y':
        BI198 += 1
    if v1_group == '6B-I2' and atm98 == 'y':
        BI298 += 1
    if v1_group == '6B-I4' and atm98 == 'y':
        BI498 += 1
    if v1_group == '6B-I7' and atm98 == 'y':
        BI798 += 1
    if v1_group == '6B-I6' and atm98 == 'y':
        BI698 += 1
    if v1_group == '6B-I8' and atm98 == 'y':
        BI898 += 1
    if v1_group == '6B-U' and atm98 == 'y':
        BU98 += 1
    if v1_group == '6B-C' and atm98 == 'y':
        BC98 += 1
    if v1_group == '6B-D' and atm98 == 'y':
        BD98 += 1
    if v1_group == '6B-E' and atm98 == 'y':
        BE98 += 1
    if v1_group == '6B-F' and atm98 == 'y':
        BF98 += 1

    if v1_group == '6C-I1' and atm98 == 'y':
        CI198 += 1
    if v1_group == '6C-I2' and atm98 == 'y':
        CI298 += 1
    if v1_group == '6C-I4' and atm98 == 'y':
        CI498 += 1
    if v1_group == '6C-I7' and atm98 == 'y':
        CI798 += 1
    if v1_group == '6C-I6' and atm98 == 'y':
        CI698 += 1
    if v1_group == '6C-I8' and atm98 == 'y':
        CI898 += 1
    if v1_group == '6C-U' and atm98 == 'y':
        CU98 += 1
    if v1_group == '6C-C' and atm98 == 'y':
        CC98 += 1
    if v1_group == '6C-D' and atm98 == 'y':
        CD98 += 1
    if v1_group == '6C-E' and atm98 == 'y':
        CE98 += 1
    if v1_group == '6C-F' and atm98 == 'y':
        CF98 += 1

    if v1_group == '6A-I1' and atm98 == 'y':
        AI198 += 1
    if v1_group == '6A-I2' and atm98 == 'y':
        AI298 += 1
    if v1_group == '6A-I4' and atm98 == 'y':
        AI498 += 1
    if v1_group == '6A-I7' and atm98 == 'y':
        AI798 += 1
    if v1_group == '6A-I6' and atm98 == 'y':
        AI698 += 1
    if v1_group == '6A-I8' and atm98 == 'y':
        AI898 += 1
    if v1_group == '6A-U' and atm98 == 'y':
        AU98 += 1
    if v1_group == '6A-C' and atm98 == 'y':
        AC98 += 1
    if v1_group == '6A-D' and atm98 == 'y':
        AD98 += 1
    if v1_group == '6A-E' and atm98 == 'y':
        AE98 += 1
    if v1_group == '6A-F' and atm98 == 'y':
        AF98 += 1

    # 95
    if v1_group == '6B-I1' and atm95 == 'y':
        BI195 += 1
    if v1_group == '6B-I2' and atm95 == 'y':
        BI295 += 1
    if v1_group == '6B-I4' and atm95 == 'y':
        BI495 += 1
    if v1_group == '6B-I7' and atm95 == 'y':
        BI795 += 1
    if v1_group == '6B-I6' and atm95 == 'y':
        BI695 += 1
    if v1_group == '6B-I8' and atm95 == 'y':
        BI895 += 1
    if v1_group == '6B-U' and atm95 == 'y':
        BU95 += 1
    if v1_group == '6B-C' and atm95 == 'y':
        BC95 += 1
    if v1_group == '6B-D' and atm95 == 'y':
        BD95 += 1
    if v1_group == '6B-E' and atm95 == 'y':
        BE95 += 1
    if v1_group == '6B-F' and atm95 == 'y':
        BF95 += 1

    if v1_group == '6C-I1' and atm95 == 'y':
        CI195 += 1
    if v1_group == '6C-I2' and atm95 == 'y':
        CI295 += 1
    if v1_group == '6C-I4' and atm95 == 'y':
        CI495 += 1
    if v1_group == '6C-I7' and atm95 == 'y':
        CI795 += 1
    if v1_group == '6C-I6' and atm95 == 'y':
        CI695 += 1
    if v1_group == '6C-I8' and atm95 == 'y':
        CI895 += 1
    if v1_group == '6C-U' and atm95 == 'y':
        CU95 += 1
    if v1_group == '6C-C' and atm95 == 'y':
        CC95 += 1
    if v1_group == '6C-D' and atm95 == 'y':
        CD95 += 1
    if v1_group == '6C-E' and atm95 == 'y':
        CE95 += 1
    if v1_group == '6C-F' and atm95 == 'y':
        CF95 += 1

    if v1_group == '6A-I1' and atm95 == 'y':
        AI195 += 1
    if v1_group == '6A-I2' and atm95 == 'y':
        AI295 += 1
    if v1_group == '6A-I4' and atm95 == 'y':
        AI495 += 1
    if v1_group == '6A-I7' and atm95 == 'y':
        AI795 += 1
    if v1_group == '6A-I6' and atm95 == 'y':
        AI695 += 1
    if v1_group == '6A-I8' and atm95 == 'y':
        AI895 += 1
    if v1_group == '6A-U' and atm95 == 'y':
        AU95 += 1
    if v1_group == '6A-C' and atm95 == 'y':
        AC95 += 1
    if v1_group == '6A-D' and atm95 == 'y':
        AD95 += 1
    if v1_group == '6A-E' and atm95 == 'y':
        AE95 += 1
    if v1_group == '6A-F' and atm95 == 'y':
        AF95 += 1

    # 90
    if v1_group == '6B-I1' and atm90 == 'y':
        BI190 += 1
    if v1_group == '6B-I2' and atm90 == 'y':
        BI290 += 1
    if v1_group == '6B-I4' and atm90 == 'y':
        BI490 += 1
    if v1_group == '6B-I7' and atm90 == 'y':
        BI790 += 1
    if v1_group == '6B-I6' and atm90 == 'y':
        BI690 += 1
    if v1_group == '6B-I8' and atm90 == 'y':
        BI890 += 1
    if v1_group == '6B-U' and atm90 == 'y':
        BU90 += 1
    if v1_group == '6B-C' and atm90 == 'y':
        BC90 += 1
    if v1_group == '6B-D' and atm90 == 'y':
        BD90 += 1
    if v1_group == '6B-E' and atm90 == 'y':
        BE90 += 1
    if v1_group == '6B-F' and atm90 == 'y':
        BF90 += 1

    if v1_group == '6C-I1' and atm90 == 'y':
        CI190 += 1
    if v1_group == '6C-I2' and atm90 == 'y':
        CI290 += 1
    if v1_group == '6C-I4' and atm90 == 'y':
        CI490 += 1
    if v1_group == '6C-I7' and atm90 == 'y':
        CI790 += 1
    if v1_group == '6C-I6' and atm90 == 'y':
        CI690 += 1
    if v1_group == '6C-I8' and atm90 == 'y':
        CI890 += 1
    if v1_group == '6C-U' and atm90 == 'y':
        CU90 += 1
    if v1_group == '6C-C' and atm90 == 'y':
        CC90 += 1
    if v1_group == '6C-D' and atm90 == 'y':
        CD90 += 1
    if v1_group == '6C-E' and atm90 == 'y':
        CE90 += 1
    if v1_group == '6C-F' and atm90 == 'y':
        CF90 += 1

    if v1_group == '6A-I1' and atm90 == 'y':
        AI190 += 1
    if v1_group == '6A-I2' and atm90 == 'y':
        AI290 += 1
    if v1_group == '6A-I4' and atm90 == 'y':
        AI490 += 1
    if v1_group == '6A-I7' and atm90 == 'y':
        AI790 += 1
    if v1_group == '6A-I6' and atm90 == 'y':
        AI690 += 1
    if v1_group == '6A-I8' and atm90 == 'y':
        AI890 += 1
    if v1_group == '6A-U' and atm90 == 'y':
        AU90 += 1
    if v1_group == '6A-C' and atm90 == 'y':
        AC90 += 1
    if v1_group == '6A-D' and atm90 == 'y':
        AD90 += 1
    if v1_group == '6A-E' and atm90 == 'y':
        AE90 += 1
    if v1_group == '6A-F' and atm90 == 'y':
        AF90 += 1

    # 85
    if v1_group == '6B-I1' and atm85 == 'y':
        BI185 += 1
    if v1_group == '6B-I2' and atm85 == 'y':
        BI285 += 1
    if v1_group == '6B-I4' and atm85 == 'y':
        BI485 += 1
    if v1_group == '6B-I7' and atm85 == 'y':
        BI785 += 1
    if v1_group == '6B-I6' and atm85 == 'y':
        BI685 += 1
    if v1_group == '6B-I8' and atm85 == 'y':
        BI885 += 1
    if v1_group == '6B-U' and atm85 == 'y':
        BU85 += 1
    if v1_group == '6B-C' and atm85 == 'y':
        BC85 += 1
    if v1_group == '6B-D' and atm85 == 'y':
        BD85 += 1
    if v1_group == '6B-E' and atm85 == 'y':
        BE85 += 1
    if v1_group == '6B-F' and atm85 == 'y':
        BF85 += 1

    if v1_group == '6C-I1' and atm85 == 'y':
        CI185 += 1
    if v1_group == '6C-I2' and atm85 == 'y':
        CI285 += 1
    if v1_group == '6C-I4' and atm85 == 'y':
        CI485 += 1
    if v1_group == '6C-I7' and atm85 == 'y':
        CI785 += 1
    if v1_group == '6C-I6' and atm85 == 'y':
        CI685 += 1
    if v1_group == '6C-I8' and atm85 == 'y':
        CI885 += 1
    if v1_group == '6C-U' and atm85 == 'y':
        CU85 += 1
    if v1_group == '6C-C' and atm85 == 'y':
        CC85 += 1
    if v1_group == '6C-D' and atm85 == 'y':
        CD85 += 1
    if v1_group == '6C-E' and atm85 == 'y':
        CE85 += 1
    if v1_group == '6C-F' and atm85 == 'y':
        CF85 += 1

    if v1_group == '6A-I1' and atm85 == 'y':
        AI185 += 1
    if v1_group == '6A-I2' and atm85 == 'y':
        AI285 += 1
    if v1_group == '6A-I4' and atm85 == 'y':
        AI485 += 1
    if v1_group == '6A-I7' and atm85 == 'y':
        AI785 += 1
    if v1_group == '6A-I6' and atm85 == 'y':
        AI685 += 1
    if v1_group == '6A-I8' and atm85 == 'y':
        AI885 += 1
    if v1_group == '6A-U' and atm85 == 'y':
        AU85 += 1
    if v1_group == '6A-C' and atm85 == 'y':
        AC85 += 1
    if v1_group == '6A-D' and atm85 == 'y':
        AD85 += 1
    if v1_group == '6A-E' and atm85 == 'y':
        AE85 += 1
    if v1_group == '6A-F' and atm85 == 'y':
        AF85 += 1

    # 80
    if v1_group == '6B-I1' and atm80 == 'y':
        BI180 += 1
    if v1_group == '6B-I2' and atm80 == 'y':
        BI280 += 1
    if v1_group == '6B-I4' and atm80 == 'y':
        BI480 += 1
    if v1_group == '6B-I7' and atm80 == 'y':
        BI780 += 1
    if v1_group == '6B-I6' and atm80 == 'y':
        BI680 += 1
        f6BI6.write(query_id+'\n')
    if v1_group == '6B-I8' and atm80 == 'y':
        BI880 += 1
        f6BI8.write(query_id + '\n')
    if v1_group == '6B-U' and atm80 == 'y':
        BU80 += 1
    if v1_group == '6B-C' and atm80 == 'y':
        BC80 += 1
    if v1_group == '6B-D' and atm80 == 'y':
        BD80 += 1
        f6BD.write(query_id + '\n')
    if v1_group == '6B-E' and atm80 == 'y':
        BE80 += 1
        f6BE.write(query_id + '\n')
    if v1_group == '6B-F' and atm80 == 'y':
        BF80 += 1

    if v1_group == '6C-I1' and atm80 == 'y':
        CI180 += 1
    if v1_group == '6C-I2' and atm80 == 'y':
        CI280 += 1
    if v1_group == '6C-I4' and atm80 == 'y':
        CI480 += 1
    if v1_group == '6C-I7' and atm80 == 'y':
        CI780 += 1
    if v1_group == '6C-I6' and atm80 == 'y':
        CI680 += 1
        f6CI6.write(query_id + '\n')
    if v1_group == '6C-I8' and atm80 == 'y':
        CI880 += 1
        f6CI8.write(query_id + '\n')
    if v1_group == '6C-U' and atm80 == 'y':
        CU80 += 1
    if v1_group == '6C-C' and atm80 == 'y':
        CC80 += 1
    if v1_group == '6C-D' and atm80 == 'y':
        CD80 += 1
        f6CD.write(query_id + '\n')
    if v1_group == '6C-E' and atm80 == 'y':
        CE80 += 1
        f6CE.write(query_id + '\n')
    if v1_group == '6C-F' and atm80 == 'y':
        CF80 += 1

    if v1_group == '6A-I1' and atm80 == 'y':
        AI180 += 1
    if v1_group == '6A-I2' and atm80 == 'y':
        AI280 += 1
    if v1_group == '6A-I4' and atm80 == 'y':
        AI480 += 1
    if v1_group == '6A-I7' and atm80 == 'y':
        AI780 += 1
    if v1_group == '6A-I6' and atm80 == 'y':
        AI680 += 1
        f6AI6.write(query_id + '\n')
    if v1_group == '6A-I8' and atm80 == 'y':
        AI880 += 1
        f6AI8.write(query_id + '\n')
    if v1_group == '6A-U' and atm80 == 'y':
        AU80 += 1
    if v1_group == '6A-C' and atm80 == 'y':
        AC80 += 1
    if v1_group == '6A-D' and atm80 == 'y':
        AD80 += 1
        f6AD.write(query_id + '\n')
    if v1_group == '6A-E' and atm80 == 'y':
        AE80 += 1
        f6AE.write(query_id + '\n')
    if v1_group == '6A-F' and atm80 == 'y':
        AF80 += 1

# B
# BA
sys.stdout.write(str(BI198))
sys.stdout.write('\t')
sys.stdout.write(str(BI195))
sys.stdout.write('\t')
sys.stdout.write(str(BI190))
sys.stdout.write('\t')
sys.stdout.write(str(BI185))
sys.stdout.write('\t')
sys.stdout.write(str(BI180))
sys.stdout.write('\n')

sys.stdout.write(str(BI298))
sys.stdout.write('\t')
sys.stdout.write(str(BI295))
sys.stdout.write('\t')
sys.stdout.write(str(BI290))
sys.stdout.write('\t')
sys.stdout.write(str(BI285))
sys.stdout.write('\t')
sys.stdout.write(str(BI280))
sys.stdout.write('\n')

sys.stdout.write(str(BI498))
sys.stdout.write('\t')
sys.stdout.write(str(BI495))
sys.stdout.write('\t')
sys.stdout.write(str(BI490))
sys.stdout.write('\t')
sys.stdout.write(str(BI485))
sys.stdout.write('\t')
sys.stdout.write(str(BI480))
sys.stdout.write('\n')

sys.stdout.write(str(BI798))
sys.stdout.write('\t')
sys.stdout.write(str(BI795))
sys.stdout.write('\t')
sys.stdout.write(str(BI790))
sys.stdout.write('\t')
sys.stdout.write(str(BI785))
sys.stdout.write('\t')
sys.stdout.write(str(BI780))
sys.stdout.write('\n')

sys.stdout.write(str(BI698))
sys.stdout.write('\t')
sys.stdout.write(str(BI695))
sys.stdout.write('\t')
sys.stdout.write(str(BI690))
sys.stdout.write('\t')
sys.stdout.write(str(BI685))
sys.stdout.write('\t')
sys.stdout.write(str(BI680))
sys.stdout.write('\n')

sys.stdout.write(str(BI898))
sys.stdout.write('\t')
sys.stdout.write(str(BI895))
sys.stdout.write('\t')
sys.stdout.write(str(BI890))
sys.stdout.write('\t')
sys.stdout.write(str(BI885))
sys.stdout.write('\t')
sys.stdout.write(str(BI880))
sys.stdout.write('\n')

# BB
sys.stdout.write(str(BU98))
sys.stdout.write('\t')
sys.stdout.write(str(BU95))
sys.stdout.write('\t')
sys.stdout.write(str(BU90))
sys.stdout.write('\t')
sys.stdout.write(str(BU85))
sys.stdout.write('\t')
sys.stdout.write(str(BU80))
sys.stdout.write('\n')

# BC
sys.stdout.write(str(BC98))
sys.stdout.write('\t')
sys.stdout.write(str(BC95))
sys.stdout.write('\t')
sys.stdout.write(str(BC90))
sys.stdout.write('\t')
sys.stdout.write(str(BC85))
sys.stdout.write('\t')
sys.stdout.write(str(BC80))
sys.stdout.write('\n')

# BD
sys.stdout.write(str(BD98))
sys.stdout.write('\t')
sys.stdout.write(str(BD95))
sys.stdout.write('\t')
sys.stdout.write(str(BD90))
sys.stdout.write('\t')
sys.stdout.write(str(BD85))
sys.stdout.write('\t')
sys.stdout.write(str(BD80))
sys.stdout.write('\n')

# BE
sys.stdout.write(str(BE98))
sys.stdout.write('\t')
sys.stdout.write(str(BE95))
sys.stdout.write('\t')
sys.stdout.write(str(BE90))
sys.stdout.write('\t')
sys.stdout.write(str(BE85))
sys.stdout.write('\t')
sys.stdout.write(str(BE80))
sys.stdout.write('\n')

# BF
sys.stdout.write(str(BF98))
sys.stdout.write('\t')
sys.stdout.write(str(BF95))
sys.stdout.write('\t')
sys.stdout.write(str(BF90))
sys.stdout.write('\t')
sys.stdout.write(str(BF85))
sys.stdout.write('\t')
sys.stdout.write(str(BF80))
sys.stdout.write('\n')

# C
# CA
sys.stdout.write(str(CI198))
sys.stdout.write('\t')
sys.stdout.write(str(CI195))
sys.stdout.write('\t')
sys.stdout.write(str(CI190))
sys.stdout.write('\t')
sys.stdout.write(str(CI185))
sys.stdout.write('\t')
sys.stdout.write(str(CI180))
sys.stdout.write('\n')

sys.stdout.write(str(CI298))
sys.stdout.write('\t')
sys.stdout.write(str(CI295))
sys.stdout.write('\t')
sys.stdout.write(str(CI290))
sys.stdout.write('\t')
sys.stdout.write(str(CI285))
sys.stdout.write('\t')
sys.stdout.write(str(CI280))
sys.stdout.write('\n')

sys.stdout.write(str(CI498))
sys.stdout.write('\t')
sys.stdout.write(str(CI495))
sys.stdout.write('\t')
sys.stdout.write(str(CI490))
sys.stdout.write('\t')
sys.stdout.write(str(CI485))
sys.stdout.write('\t')
sys.stdout.write(str(CI480))
sys.stdout.write('\n')

sys.stdout.write(str(CI798))
sys.stdout.write('\t')
sys.stdout.write(str(CI795))
sys.stdout.write('\t')
sys.stdout.write(str(CI790))
sys.stdout.write('\t')
sys.stdout.write(str(CI785))
sys.stdout.write('\t')
sys.stdout.write(str(CI780))
sys.stdout.write('\n')

sys.stdout.write(str(CI698))
sys.stdout.write('\t')
sys.stdout.write(str(CI695))
sys.stdout.write('\t')
sys.stdout.write(str(CI690))
sys.stdout.write('\t')
sys.stdout.write(str(CI685))
sys.stdout.write('\t')
sys.stdout.write(str(CI680))
sys.stdout.write('\n')

sys.stdout.write(str(CI898))
sys.stdout.write('\t')
sys.stdout.write(str(CI895))
sys.stdout.write('\t')
sys.stdout.write(str(CI890))
sys.stdout.write('\t')
sys.stdout.write(str(CI885))
sys.stdout.write('\t')
sys.stdout.write(str(CI880))
sys.stdout.write('\n')

# CB
sys.stdout.write(str(CU98))
sys.stdout.write('\t')
sys.stdout.write(str(CU95))
sys.stdout.write('\t')
sys.stdout.write(str(CU90))
sys.stdout.write('\t')
sys.stdout.write(str(CU85))
sys.stdout.write('\t')
sys.stdout.write(str(CU80))
sys.stdout.write('\n')

# CC
sys.stdout.write(str(CC98))
sys.stdout.write('\t')
sys.stdout.write(str(CC95))
sys.stdout.write('\t')
sys.stdout.write(str(CC90))
sys.stdout.write('\t')
sys.stdout.write(str(CC85))
sys.stdout.write('\t')
sys.stdout.write(str(CC80))
sys.stdout.write('\n')

# CD
sys.stdout.write(str(CD98))
sys.stdout.write('\t')
sys.stdout.write(str(CD95))
sys.stdout.write('\t')
sys.stdout.write(str(CD90))
sys.stdout.write('\t')
sys.stdout.write(str(CD85))
sys.stdout.write('\t')
sys.stdout.write(str(CD80))
sys.stdout.write('\n')

# CE
sys.stdout.write(str(CE98))
sys.stdout.write('\t')
sys.stdout.write(str(CE95))
sys.stdout.write('\t')
sys.stdout.write(str(CE90))
sys.stdout.write('\t')
sys.stdout.write(str(CE85))
sys.stdout.write('\t')
sys.stdout.write(str(CE80))
sys.stdout.write('\n')

# CF
sys.stdout.write(str(CF98))
sys.stdout.write('\t')
sys.stdout.write(str(CF95))
sys.stdout.write('\t')
sys.stdout.write(str(CF90))
sys.stdout.write('\t')
sys.stdout.write(str(CF85))
sys.stdout.write('\t')
sys.stdout.write(str(CF80))
sys.stdout.write('\n')

# A
sys.stdout.write(str(AI198))
sys.stdout.write('\t')
sys.stdout.write(str(AI195))
sys.stdout.write('\t')
sys.stdout.write(str(AI190))
sys.stdout.write('\t')
sys.stdout.write(str(AI185))
sys.stdout.write('\t')
sys.stdout.write(str(AI180))
sys.stdout.write('\n')

sys.stdout.write(str(AI298))
sys.stdout.write('\t')
sys.stdout.write(str(AI295))
sys.stdout.write('\t')
sys.stdout.write(str(AI290))
sys.stdout.write('\t')
sys.stdout.write(str(AI285))
sys.stdout.write('\t')
sys.stdout.write(str(AI280))
sys.stdout.write('\n')

sys.stdout.write(str(AI498))
sys.stdout.write('\t')
sys.stdout.write(str(AI495))
sys.stdout.write('\t')
sys.stdout.write(str(AI490))
sys.stdout.write('\t')
sys.stdout.write(str(AI485))
sys.stdout.write('\t')
sys.stdout.write(str(AI480))
sys.stdout.write('\n')

sys.stdout.write(str(AI798))
sys.stdout.write('\t')
sys.stdout.write(str(AI795))
sys.stdout.write('\t')
sys.stdout.write(str(AI790))
sys.stdout.write('\t')
sys.stdout.write(str(AI785))
sys.stdout.write('\t')
sys.stdout.write(str(AI780))
sys.stdout.write('\n')

sys.stdout.write(str(AI698))
sys.stdout.write('\t')
sys.stdout.write(str(AI695))
sys.stdout.write('\t')
sys.stdout.write(str(AI690))
sys.stdout.write('\t')
sys.stdout.write(str(AI685))
sys.stdout.write('\t')
sys.stdout.write(str(AI680))
sys.stdout.write('\n')

sys.stdout.write(str(AI898))
sys.stdout.write('\t')
sys.stdout.write(str(AI895))
sys.stdout.write('\t')
sys.stdout.write(str(AI890))
sys.stdout.write('\t')
sys.stdout.write(str(AI885))
sys.stdout.write('\t')
sys.stdout.write(str(AI880))
sys.stdout.write('\n')

# AB
sys.stdout.write(str(AU98))
sys.stdout.write('\t')
sys.stdout.write(str(AU95))
sys.stdout.write('\t')
sys.stdout.write(str(AU90))
sys.stdout.write('\t')
sys.stdout.write(str(AU85))
sys.stdout.write('\t')
sys.stdout.write(str(AU80))
sys.stdout.write('\n')

# AC
sys.stdout.write(str(AC98))
sys.stdout.write('\t')
sys.stdout.write(str(AC95))
sys.stdout.write('\t')
sys.stdout.write(str(AC90))
sys.stdout.write('\t')
sys.stdout.write(str(AC85))
sys.stdout.write('\t')
sys.stdout.write(str(AC80))
sys.stdout.write('\n')

# AD
sys.stdout.write(str(AD98))
sys.stdout.write('\t')
sys.stdout.write(str(AD95))
sys.stdout.write('\t')
sys.stdout.write(str(AD90))
sys.stdout.write('\t')
sys.stdout.write(str(AD85))
sys.stdout.write('\t')
sys.stdout.write(str(AD80))
sys.stdout.write('\n')

# AE
sys.stdout.write(str(AE98))
sys.stdout.write('\t')
sys.stdout.write(str(AE95))
sys.stdout.write('\t')
sys.stdout.write(str(AE90))
sys.stdout.write('\t')
sys.stdout.write(str(AE85))
sys.stdout.write('\t')
sys.stdout.write(str(AE80))
sys.stdout.write('\n')

# AF
sys.stdout.write(str(AF98))
sys.stdout.write('\t')
sys.stdout.write(str(AF95))
sys.stdout.write('\t')
sys.stdout.write(str(AF90))
sys.stdout.write('\t')
sys.stdout.write(str(AF85))
sys.stdout.write('\t')
sys.stdout.write(str(AF80))
sys.stdout.write('\n')