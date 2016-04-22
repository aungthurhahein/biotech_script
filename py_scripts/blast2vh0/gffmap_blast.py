#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
blastfile = sys.argv[1]
gfffile = sys.argv[2]

chid = []
start = []
end = []
allrecords = []
with open(gfffile, 'rb') as f1:
    for l1 in f1:
        l1_split = l1.split()        
        allrecords.append(l1)
        chid.append(l1_split[0]) 
        if int(l1_split[3]) > int(l1_split[4]):
            start.append(int(l1_split[4]))    
            end.append(int(l1_split[3]))    
        else:
            start.append(int(l1_split[3]))    
            end.append(int(l1_split[4]))

with open(blastfile,'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        cid = l2_split[1]        
        if int(l2_split[8]) > int(l2_split[9]):
            a = int(l2_split[9])
            b = int(l2_split[8])    
        else:
            a = int(l2_split[8])
            b = int(l2_split[9])    
        # indexes = [i for i,e in enumerate(chid) if e == cid]
        #   a----------------------------b
        #       c-----------------d
        #c---------------d
        #                   c------------------------d           
        # c----------------------------------------d
        for i,x in enumerate(chid):
            c = start[i]
            d = end[i]
            # print a,b
            # print c,d                  
            if a >= c and a <= d:
                sys.stdout.write(l2.strip('\n')+'\t'+allrecords[i])
            elif b >= c and b <= d:
                sys.stdout.write(l2.strip('\n')+'\t'+allrecords[i])
            # else
            #     sys.stdout.write(l2)
            # if a >= c and b <= d:                
            #     sys.stdout.write(allrecords[i])
            # elif a <= c and a > d and b <= d:                
            #     sys.stdout.write(allrecords[i])            
            # elif a >= c and a < d and  b >= d:                
            #     sys.stdout.write(allrecords[i])                            
            # elif a < c and b > d:                
            #     sys.stdout.write(allrecords[i])                                    

# python gffblastmap.py KritSSH01-Vh020150913.megablast.bls2seq.qc95 Vc1114-20150427.gff > KritSSH01-Vh020150913.megablast.bls2seq.qc95.map
# python gffblastmap.py KritSSH01-Vh020150913.megablast.bls2seq.qcL95 Vc1114-20150427.gff > KritSSH01-Vh020150913.megablast.bls2seq.qcL95.map
# python gffblastmap2.py rescreESTs-Vh020150913.megablast.bls2seq.qc95 Vc1114-20150427.gff > rescreESTs-Vh020150913.megablast.bls2seq.qc95.map2
# python gffblastmap2.py rescreESTs-Vh020150913.megablast.bls2seq.qcL95 Vc1114-20150427.gff > rescreESTs-Vh020150913.megablast.bls2seq.qcl95.map2

# python  gff_map.py KritSSH01-vhs1.megablast.bls2seq.qc95 vhs1.f125cmbNL21O53a29000bp.gff3 > KritSSH01-vhs1.megablast.bls2seq.qc95.map2
# python  gff_map.py KritSSH01-vhs1.megablast.bls2seq.qcL95 vhs1.f125cmbNL21O53a29000bp.gff3 > KritSSH01-vhs1.megablast.bls2seq.qcL95.map2
# python  gff_map.py rescreESTs-vhs1.megablast.bls2seq.qc95 vhs1.f125cmbNL21O53a29000bp.gff3 > rescreESTs-vhs1.megablast.bls2seq.qc95.map2
# python  gff_map.py rescreESTs-vhs1.megablast.bls2seq.qcL95 vhs1.f125cmbNL21O53a29000bp.gff3 > rescreESTs-vhs1.megablast.bls2seq.qcL95.map2
