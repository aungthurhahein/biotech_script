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

BA98 = 0
BB98 = 0
BC98 = 0
BD98 = 0
BE98 = 0
BF98 = 0
CA98 = 0
CB98 = 0
CC98 = 0
CD98 = 0
CE98 = 0
CF98 = 0
AA98 = 0
AB98 = 0
AC98 = 0
AD98 = 0
AE98 = 0
AF98 = 0

BA95 = 0
BB95 = 0
BC95 = 0
BD95 = 0
BE95 = 0
BF95 = 0
CA95 = 0
CB95 = 0
CC95 = 0
CD95 = 0
CE95 = 0
CF95 = 0
AA95 = 0
AB95 = 0
AC95 = 0
AD95 = 0
AE95 = 0
AF95 = 0

BA90 = 0
BB90 = 0
BC90 = 0
BD90 = 0
BE90 = 0
BF90 = 0
CA90 = 0
CB90 = 0
CC90 = 0
CD90 = 0
CE90 = 0
CF90 = 0
AA90 = 0
AB90 = 0
AC90 = 0
AD90 = 0
AE90 = 0
AF90 = 0

BA85 = 0
BB85 = 0
BC85 = 0
BD85 = 0
BE85 = 0
BF85 = 0
CA85 = 0
CB85 = 0
CC85 = 0
CD85 = 0
CE85 = 0
CF85 = 0
AA85 = 0
AB85 = 0
AC85 = 0
AD85 = 0
AE85 = 0
AF85 = 0

BA80 = 0
BB80 = 0
BC80 = 0
BD80 = 0
BE80 = 0
BF80 = 0
CA80 = 0
CB80 = 0
CC80 = 0
CD80 = 0
CE80 = 0
CF80 = 0
AA80 = 0
AB80 = 0
AC80 = 0
AD80 = 0
AE80 = 0
AF80 = 0

for line in opencombinefile:
    line_split = line.split('\t')
    atm98 = line_split[2].strip()
    atm95 = line_split[3].strip()
    atm90 = line_split[4].strip()
    atm85 = line_split[5].strip()
    atm80 = line_split[6].strip()
    v1_group = line_split[12].strip()  # v1

    # 98
    if v1_group == '6B-A' and atm98 == 'y':
        BA98 += 1
    if v1_group == '6B-B' and atm98 == 'y':
        BB98 += 1
    if v1_group == '6B-C' and atm98 == 'y':
        BC98 += 1
    if v1_group == '6B-D' and atm98 == 'y':
        BD98 += 1
    if v1_group == '6B-E' and atm98 == 'y':
        BE98 += 1
    if v1_group == '6B-F' and atm98 == 'y':
        BF98 += 1
    if v1_group == '6C-A' and atm98 == 'y':
        CA98 += 1
    if v1_group == '6C-B' and atm98 == 'y':
        CB98 += 1
    if v1_group == '6C-C' and atm98 == 'y':
        CC98 += 1
    if v1_group == '6C-D' and atm98 == 'y':
        CD98 += 1
    if v1_group == '6C-E' and atm98 == 'y':
        CE98 += 1
    if v1_group == '6C-F' and atm98 == 'y':
        CF98 =+ 1
    if v1_group == '6A-A' and atm98 == 'y':
        AA98 += 1
    if v1_group == '6A-B' and atm98 == 'y':
        AB98 += 1
    if v1_group == '6A-C' and atm98 == 'y':
        AC98 += 1
    if v1_group == '6A-D' and atm98 == 'y':
        AD98 += 1
    if v1_group == '6A-E' and atm98 == 'y':
        AE98 += 1
    if v1_group == '6A-F' and atm98 == 'y':
        AF98 += 1

    # 95
    if v1_group == '6B-A' and atm95 == 'y':
        BA95 += 1
    if v1_group == '6B-B' and atm95 == 'y':
        BB95 += 1
    if v1_group == '6B-C' and atm95 == 'y':
        BC95 += 1
    if v1_group == '6B-D' and atm95 == 'y':
        BD95 += 1
    if v1_group == '6B-E' and atm95 == 'y':
        BE95 += 1
    if v1_group == '6B-F' and atm95 == 'y':
        BF95 += 1
    if v1_group == '6C-A' and atm95 == 'y':
        CA95 += 1
    if v1_group == '6C-B' and atm95 == 'y':
        CB95 += 1
    if v1_group == '6C-C' and atm95 == 'y':
        CC95 += 1
    if v1_group == '6C-D' and atm95 == 'y':
        CD95 += 1
    if v1_group == '6C-E' and atm95 == 'y':
        CE95 += 1
    if v1_group == '6C-F' and atm95 == 'y':
        CF95 = + 1
    if v1_group == '6A-A' and atm95 == 'y':
        AA95 += 1
    if v1_group == '6A-B' and atm95 == 'y':
        AB95 += 1
    if v1_group == '6A-C' and atm95 == 'y':
        AC95 += 1
    if v1_group == '6A-D' and atm95 == 'y':
        AD95 += 1
    if v1_group == '6A-E' and atm95 == 'y':
        AE95 += 1
    if v1_group == '6A-F' and atm95 == 'y':
        AF95 += 1

    # 90
    if v1_group == '6B-A' and atm90 == 'y':
        BA90 += 1
    if v1_group == '6B-B' and atm90 == 'y':
        BB90 += 1
    if v1_group == '6B-C' and atm90 == 'y':
        BC90 += 1
    if v1_group == '6B-D' and atm90 == 'y':
        BD90 += 1
    if v1_group == '6B-E' and atm90 == 'y':
        BE90 += 1
    if v1_group == '6B-F' and atm90 == 'y':
        BF90 += 1
    if v1_group == '6C-A' and atm90 == 'y':
        CA90 += 1
    if v1_group == '6C-B' and atm90 == 'y':
        CB90 += 1
    if v1_group == '6C-C' and atm90 == 'y':
        CC90 += 1
    if v1_group == '6C-D' and atm90 == 'y':
        CD90 += 1
    if v1_group == '6C-E' and atm90 == 'y':
        CE90 += 1
    if v1_group == '6C-F' and atm90 == 'y':
        CF90 = + 1
    if v1_group == '6A-A' and atm90 == 'y':
        AA90 += 1
    if v1_group == '6A-B' and atm90 == 'y':
        AB90 += 1
    if v1_group == '6A-C' and atm90 == 'y':
        AC90 += 1
    if v1_group == '6A-D' and atm90 == 'y':
        AD90 += 1
    if v1_group == '6A-E' and atm90 == 'y':
        AE90 += 1
    if v1_group == '6A-F' and atm90 == 'y':
        AF90 += 1

    # 85
    if v1_group == '6B-A' and atm85 == 'y':
        BA85 += 1
    if v1_group == '6B-B' and atm85 == 'y':
        BB85 += 1
    if v1_group == '6B-C' and atm85 == 'y':
        BC85 += 1
    if v1_group == '6B-D' and atm85 == 'y':
        BD85 += 1
    if v1_group == '6B-E' and atm85 == 'y':
        BE85 += 1
    if v1_group == '6B-F' and atm85 == 'y':
        BF85 += 1
    if v1_group == '6C-A' and atm85 == 'y':
        CA85 += 1
    if v1_group == '6C-B' and atm85 == 'y':
        CB85 += 1
    if v1_group == '6C-C' and atm85 == 'y':
        CC85 += 1
    if v1_group == '6C-D' and atm85 == 'y':
        CD85 += 1
    if v1_group == '6C-E' and atm85 == 'y':
        CE85 += 1
    if v1_group == '6C-F' and atm85 == 'y':
        CF85 = + 1
    if v1_group == '6A-A' and atm85 == 'y':
        AA85 += 1
    if v1_group == '6A-B' and atm85 == 'y':
        AB85 += 1
    if v1_group == '6A-C' and atm85 == 'y':
        AC85 += 1
    if v1_group == '6A-D' and atm85 == 'y':
        AD85 += 1
    if v1_group == '6A-E' and atm85 == 'y':
        AE85 += 1
    if v1_group == '6A-F' and atm85 == 'y':
        AF85 += 1

    # 80
    if v1_group == '6B-A' and atm80 == 'y':
        BA80 += 1
    if v1_group == '6B-B' and atm80 == 'y':
        BB80 += 1
    if v1_group == '6B-C' and atm80 == 'y':
        BC80 += 1
    if v1_group == '6B-D' and atm80 == 'y':
        BD80 += 1
    if v1_group == '6B-E' and atm80 == 'y':
        BE80 += 1
    if v1_group == '6B-F' and atm80 == 'y':
        BF80 += 1
    if v1_group == '6C-A' and atm80 == 'y':
        CA80 += 1
    if v1_group == '6C-B' and atm80 == 'y':
        CB80 += 1
    if v1_group == '6C-C' and atm80 == 'y':
        CC80 += 1
    if v1_group == '6C-D' and atm80 == 'y':
        CD80 += 1
    if v1_group == '6C-E' and atm80 == 'y':
        CE80 += 1
    if v1_group == '6C-F' and atm80 == 'y':
        CF80 = + 1
    if v1_group == '6A-A' and atm80 == 'y':
        AA80 += 1
    if v1_group == '6A-B' and atm80 == 'y':
        AB80 += 1
    if v1_group == '6A-C' and atm80 == 'y':
        AC80 += 1
    if v1_group == '6A-D' and atm80 == 'y':
        AD80 += 1
    if v1_group == '6A-E' and atm80 == 'y':
        AE80 += 1
    if v1_group == '6A-F' and atm80 == 'y':
        AF80 += 1

# B
# BA
sys.stdout.write(str(BA98))
sys.stdout.write('\t')
sys.stdout.write(str(BA95))
sys.stdout.write('\t')
sys.stdout.write(str(BA90))
sys.stdout.write('\t')
sys.stdout.write(str(BA85))
sys.stdout.write('\t')
sys.stdout.write(str(BA80))
sys.stdout.write('\n')

# BB
sys.stdout.write(str(BB98))
sys.stdout.write('\t')
sys.stdout.write(str(BB95))
sys.stdout.write('\t')
sys.stdout.write(str(BB90))
sys.stdout.write('\t')
sys.stdout.write(str(BB85))
sys.stdout.write('\t')
sys.stdout.write(str(BB80))
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
sys.stdout.write(str(CA98))
sys.stdout.write('\t')
sys.stdout.write(str(CA95))
sys.stdout.write('\t')
sys.stdout.write(str(CA90))
sys.stdout.write('\t')
sys.stdout.write(str(CA85))
sys.stdout.write('\t')
sys.stdout.write(str(CA80))
sys.stdout.write('\n')

# CB
sys.stdout.write(str(CB98))
sys.stdout.write('\t')
sys.stdout.write(str(CB95))
sys.stdout.write('\t')
sys.stdout.write(str(CB90))
sys.stdout.write('\t')
sys.stdout.write(str(CB85))
sys.stdout.write('\t')
sys.stdout.write(str(CB80))
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
# AA
sys.stdout.write(str(AA98))
sys.stdout.write('\t')
sys.stdout.write(str(AA95))
sys.stdout.write('\t')
sys.stdout.write(str(AA90))
sys.stdout.write('\t')
sys.stdout.write(str(AA85))
sys.stdout.write('\t')
sys.stdout.write(str(AA80))
sys.stdout.write('\n')

# AB
sys.stdout.write(str(AB98))
sys.stdout.write('\t')
sys.stdout.write(str(AB95))
sys.stdout.write('\t')
sys.stdout.write(str(AB90))
sys.stdout.write('\t')
sys.stdout.write(str(AB85))
sys.stdout.write('\t')
sys.stdout.write(str(AB80))
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