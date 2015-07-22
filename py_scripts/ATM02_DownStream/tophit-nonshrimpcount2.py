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
    NX = line_split[1].split('-')[1]

    # N
    if NX == 'I1(N)':
        BI1CatX += 1
    elif NX == 'I2(N)':
        BI2CatX += 1
    elif NX == 'I4(N)':
        BI4CatX += 1
    elif NX == 'I7(N)':
        BI7CatX += 1
        print NX
    elif NX == 'I6(N)':
        BI6CatX += 1
    elif NX == 'I8(N)':
        BI8CatX += 1
    elif NX == 'U(N)':
        BUCatX += 1
    elif NX == 'C(N)':
        BCCatX += 1
    elif NX == 'D(N)':
        BDCatX += 1
    elif NX == 'E(N)':
        BECatX += 1
    elif NX == 'F(N)':
        BFCatX += 1
    elif NX == 'G(N)':
        BGCatX += 1
    elif NX == 'I1(X)':
        CI1CatX += 1
    elif NX == 'I2(X)':
        CI2CatX += 1
    elif NX == 'I4(X)':
        CI4CatX += 1
    elif NX == 'I7(X)':
        CI7CatX += 1
    elif NX == 'I6(X)':
        CI6CatX += 1
    elif NX == 'I8(X)':
        CI8CatX += 1
    elif NX == 'U(X)':
        CUCatX += 1
    elif NX == 'C(X)':
        CCCatX += 1
    elif NX == 'D(X)':
        CDCatX += 1
    elif NX == 'E(X)':
        CECatX += 1
    elif NX == 'F(X)':
        CFCatX += 1
    elif NX == 'G(X)':
        CGCatX += 1
        # else:
        #     print CatX.split('-')

sys.stdout.write(str("N"))
sys.stdout.write('\t')
sys.stdout.write(str("X"))
sys.stdout.write('\n')

sys.stdout.write(str(BI1CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI1CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI2CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI2CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI4CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI4CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI7CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI7CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI6CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI6CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BUCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CUCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BI8CatX))
sys.stdout.write('\t')
sys.stdout.write(str(CI8CatX))
sys.stdout.write('\n')

sys.stdout.write(str(BCCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CCCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BDCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CDCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BECatX))
sys.stdout.write('\t')
sys.stdout.write(str(CECatX))
sys.stdout.write('\n')

sys.stdout.write(str(BFCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CFCatX))
sys.stdout.write('\n')

sys.stdout.write(str(BGCatX))
sys.stdout.write('\t')
sys.stdout.write(str(CGCatX))
sys.stdout.write('\n')

