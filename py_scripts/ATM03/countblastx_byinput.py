#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import ipdb();ipdb.set_trace()

blastx = sys.argv[1]
putATM03 = sys.argv[2]
putATM03S = sys.argv[3]
CI1BlastX = 0
CI2BlastX = 0
CI4BlastX = 0
CI7BlastX = 0
CI6BlastX = 0
CI8BlastX = 0
CUBlastX = 0
CCBlastX = 0
CDBlastX = 0
CEBlastX = 0
CFBlastX = 0
CGBlastX = 0

CI1BlastXS = 0
CI2BlastXS = 0
CI4BlastXS = 0
CI7BlastXS = 0
CI6BlastXS = 0
CI8BlastXS = 0
CUBlastXS = 0
CCBlastXS = 0
CDBlastXS = 0
CEBlastXS = 0
CFBlastXS = 0
CGBlastXS = 0

putid = []
with open(putATM03,'rb') as f1:
    for line in f1:
        line_split = line.split('\t')
        putid.append(line_split[0].strip('>').strip('\n'))

nonshrimpid = []
with open(putATM03S,'rb') as f2:
    for line2 in f2:
        line2_split = line2.split('\t')
        nonshrimpid.append(line2_split[0].strip('>').strip('\n'))

with open(blastx, 'rb') as f3:
    for l3 in f3:
        line3_split = l3.split('\t')
        qid = line3_split[0]
        qgroup = line3_split[1]

        if qgroup == 'I1' and qid in nonshrimpid:
            CI1BlastXS += 1
        elif qgroup == 'I2' and qid in nonshrimpid:
            CI2BlastXS += 1
        elif qgroup == 'I4' and qid in nonshrimpid:
            CI4BlastXS += 1
        elif qgroup == 'I7' and qid in nonshrimpid:
            CI7BlastXS += 1
        elif qgroup == 'I6' and qid in nonshrimpid:
            CI6BlastXS += 1
        elif qgroup == 'I8' and qid in nonshrimpid:
            CI8BlastXS += 1
        elif qgroup == 'U' and qid in nonshrimpid:
            CUBlastXS += 1
        elif qgroup == 'C' and qid in nonshrimpid:
            CCBlastXS += 1
        elif qgroup == 'D' and qid in nonshrimpid:
            CDBlastXS += 1
        elif qgroup == 'E' and qid in nonshrimpid:
            CEBlastXS += 1
        elif qgroup == 'F' and qid in nonshrimpid:
            CFBlastXS += 1
        elif qgroup == 'G' and qid in nonshrimpid:
            CGBlastXS += 1

        if qgroup == 'I1' and qid in putid:
            CI1BlastX += 1
        elif qgroup == 'I2' and qid in putid:
            CI2BlastX += 1
        elif qgroup == 'I4' and qid in putid:
            CI4BlastX += 1
        elif qgroup == 'I7' and qid in putid:
            CI7BlastX += 1
        elif qgroup == 'I6' and qid in putid:
            CI6BlastX += 1
        elif qgroup == 'I8' and qid in putid:
            CI8BlastX += 1
        elif qgroup == 'U' and qid in putid:
            CUBlastX += 1
        elif qgroup == 'C' and qid in putid:
            CCBlastX += 1
        elif qgroup == 'D' and qid in putid:
            CDBlastX += 1
        elif qgroup == 'E' and qid in putid:
            CEBlastX += 1
        elif qgroup == 'F' and qid in putid:
            CFBlastX += 1
        elif qgroup == 'G' and qid in putid:
            CGBlastX += 1



sys.stdout.write(str(CI1BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CI2BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CI4BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CI7BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CI6BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CUBlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CI8BlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CCBlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CDBlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CEBlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CFBlastX))
sys.stdout.write('\n')

sys.stdout.write(str(CGBlastX))
sys.stdout.write('\n')

sys.stdout.write('###############################\n')

sys.stdout.write(str(CI1BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CI2BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CI4BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CI7BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CI6BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CUBlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CI8BlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CCBlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CDBlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CEBlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CFBlastXS))
sys.stdout.write('\n')

sys.stdout.write(str(CGBlastXS))
sys.stdout.write('\n')