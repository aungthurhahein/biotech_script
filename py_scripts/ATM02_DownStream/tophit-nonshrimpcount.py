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

AI1CatX = 0
AI2CatX = 0
AI4CatX = 0
AI7CatX = 0
AI6CatX = 0
AI8CatX = 0
AUCatX = 0
ACCatX = 0
ADCatX = 0
AECatX = 0
AFCatX = 0
AGCatX = 0

BI1CatX = 0
BI2CatX = 0
BI4CatX = 0
BI7CatX = 0
BI6CatX = 0
BI8CatX = 0
BUCatX = 0
BCCatX = 0
BDCatX = 0
BECatX = 0
BFCatX = 0
BGCatX = 0

CI1CatX = 0
CI2CatX = 0
CI4CatX = 0
CI7CatX = 0
CI6CatX = 0
CI8CatX = 0
CUCatX = 0
CCCatX = 0
CDCatX = 0
CECatX = 0
CFCatX = 0
CGCatX = 0

for line in openfile:
    line_split = line.split('\t')
    CatX = line_split[2].split('(')[0]

    # B
    if CatX == '6B-I1':
        BI1CatX += 1
    elif CatX == '6B-I2':
        BI2CatX += 1
    elif CatX == '6B-I4':
        BI4CatX += 1
    elif CatX == '6B-I7':
        BI7CatX += 1
    elif CatX == '6B-I6':
        BI6CatX += 1
    elif CatX == '6B-I8':
        BI8CatX += 1
    elif CatX == '6B-U':
        BUCatX += 1
    elif CatX == '6B-C':
        BCCatX += 1
    elif CatX == '6B-D':
        BDCatX += 1
    elif CatX == '6B-E':
        BECatX += 1
    elif CatX == '6B-F':
        BFCatX += 1
    elif CatX == '6B-G':
        BGCatX += 1

    # C
    if CatX == '6C-I1':
        CI1CatX += 1
    elif CatX == '6C-I2':
        CI2CatX += 1
    elif CatX == '6C-I4':
        CI4CatX += 1
    elif CatX == '6C-I7':
        CI7CatX += 1
    elif CatX == '6C-I6':
        CI6CatX += 1
    elif CatX == '6C-I8':
        CI8CatX += 1
    elif CatX == '6C-U':
        CUCatX += 1
    elif CatX == '6C-C':
        CCCatX += 1
    elif CatX == '6C-D':
        CDCatX += 1
    elif CatX == '6C-E':
        CECatX += 1
    elif CatX == '6C-F':
        CFCatX += 1
    elif CatX == '6C-G':
        CGCatX += 1
    
    # A
    if CatX == '6A-I1':
        AI1CatX += 1
    elif CatX == '6A-I2':
        AI2CatX += 1
    elif CatX == '6A-I4':
        AI4CatX += 1
    elif CatX == '6A-I7':
        AI7CatX += 1
    elif CatX == '6A-I6':
        AI6CatX += 1
    elif CatX == '6A-I8':
        AI8CatX += 1
    elif CatX == '6A-U':
        AUCatX += 1
    elif CatX == '6A-C':
        ACCatX += 1
    elif CatX == '6A-D':
        ADCatX += 1
    elif CatX == '6A-E':
        AECatX += 1
    elif CatX == '6A-F':
        AFCatX += 1
    elif CatX == '6A-G':
        AGCatX += 1

sys.stdout.write(str("6B"))
sys.stdout.write('\t')
sys.stdout.write(str("6C"))
sys.stdout.write('\t')
sys.stdout.write(str("6A"))
sys.stdout.write('\n')


sys.stdout.write(str(BI1CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI1CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI1CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI2CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI2CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI2CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI4CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI4CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI4CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI7CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI7CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI7CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI6CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI6CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI6CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BUCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CUCatX))
sys.stdout.write('\t')
sys.stdout.write(str(AUCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI8CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI8CatX))
sys.stdout.write('\t')
sys.stdout.write(str(AI8CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BCCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CCCatX))
sys.stdout.write('\t')
sys.stdout.write(str(ACCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BDCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CDCatX))
sys.stdout.write('\t')
sys.stdout.write(str(ADCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BECatX))
sys.stdout.write('\t')
sys.stdout.write(str(CECatX))
sys.stdout.write('\t')
sys.stdout.write(str(AECatX))
sys.stdout.write('\n')

sys.stdout.write(str(BFCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CFCatX))
sys.stdout.write('\t')
sys.stdout.write(str(AFCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BGCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CGCatX))
sys.stdout.write('\t')
sys.stdout.write(str(AGCatX))
sys.stdout.write('\n')
