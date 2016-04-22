# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-04-04 13:44:31
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-04-04 15:19:12
import sys
file_ = sys.argv[1]

CM = open(file_+'_CM','w')
CS = open(file_+'_CS','w')
MC = open(file_+'_MC','w')
SC = open(file_+'_SC','w')
SM = open(file_+'_SM','w')
MS = open(file_+'_MS','w')
C = open(file_+'_C','w')
M = open(file_+'_M','w')
S = open(file_+'_S','w')
O = open(file_+'_other','w')

with open(file_,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        C_val = l1_split[7]
        M_val = l1_split[8]
        S_val = l1_split[9] 

        if float(C_val) > 0 and float(M_val) == 0 and float(S_val) == 0:
            C.write(l1)
        if float(C_val) == 0 and float(M_val) > 0 and float(S_val) == 0:
            M.write(l1)
        if float(C_val) == 0 and float(M_val) == 0 and float(S_val) > 0:
            S.write(l1)
        if C_val > M_val:
            CM.write(l1)
        if C_val > S_val:
            CS.write(l1)
        if M_val > C_val:
            MC.write(l1)
        if S_val > C_val:
            SC.write(l1)
        if S_val > M_val:
            SM.write(l1)
        if M_val > S_val:
            MS.write(l1)
        # else:
        #     O.write(l1)
