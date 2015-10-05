#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
lst = sys.argv[1]

blastn_all = "/mnt/nfs/media/Aung/ofint.genus/infiles/ATM02.blstn.tophits.all.update"
blastx_all = "/mnt/nfs/media/Aung/ofint.genus/infiles/ATM02.blstx.tophits.all.update"

blastn_tophit = "/mnt/nfs/media/Aung/ofint.genus/infiles/gi_tophit/ATM02_tophit_gi.catx_blastn_uniq"
blastx_tophit = "/mnt/nfs/media/Aung/ofint.genus/infiles/gi_tophit/ATM02_tophit_gi.catx_blastx_uniq"

blastn_gi = "/mnt/nfs/media/Aung/ofint.genus/infiles/gi_tophit/ATM02_tophit_gi.catx_blastn_gi_uniq.gi.hdracc.t"
blastx_gi = "/mnt/nfs/media/Aung/ofint.genus/infiles/gi_tophit/ATM02_tophit_gi.catx_blastx_gi_uniq.gi.hdracc.t"

n_gi = []
n_gidesc = []
with open(blastn_gi,'rb') as fgi:
    for lgi in fgi:
        lgi_s = lgi.split('\t')
        n_gi.append(lgi_s[0])
        n_gidesc.append(lgi_s[1].strip('\n'))

x_gi = []
x_gidesc = []
with open(blastx_gi,'rb') as fgi2:
    for lgi2 in fgi2:
        lgi2_s = lgi2.split('\t')
        x_gi.append(lgi2_s[0])
        x_gidesc.append(lgi2_s[1].strip('\n'))


ngroup = []
nid = []
nline = []
ngiid = []
with open(blastn_all,'rb') as f1:
    for l1 in f1:
        l1_s = l1.split('\t')
        ngroup.append(l1_s[0].strip())
        nid.append(l1_s[1].strip('>').strip())
        nline.append(l1.strip().strip('\n'))
        ngiid.append(l1_s[5].strip().strip('\n'))

xgroup = []
xid = []
xline = []
xgiid = []
with open(blastx_all, 'rb') as f2:
    for l2 in f2:
        l2_s = l2.split('\t')
        xgroup.append(l2_s[0].strip())
        xid.append(l2_s[1].strip('>').strip())
        xline.append(l2.strip().strip('\n'))
        xgiid.append(l2_s[5].strip().strip('\n'))

nmapgroup = []
nmapid = []
nmapline = []
nmapgi = []
nmaptaxon = []
with open(blastn_tophit, 'rb') as f3:
    for l3 in f3:
        l3_s = l3.split('\t')
        nmapid.append(l3_s[0].strip('>').strip())
        nmapgroup.append(l3_s[1])
        nmapgi.append(l3_s[3])
        nmapline.append(l3)
        nmaptaxon.append(l3_s[4].strip('\n'))

xmapgroup = []
xmapid = []
xmapline = []
xmaptaxon = []
xmapgi = []
xmaptaxon = []
with open(blastx_tophit, 'rb') as f4:
    for l4 in f4:
        l4_s = l4.split('\t')
        xmapid.append(l4_s[0].strip('>').strip())
        xmapgroup.append(l4_s[1])
        xmapgi.append(l4_s[3])
        xmapline.append(l4)
        xmaptaxon.append(l4_s[4].strip('\n'))

# o = open(lst+"_gi",'w')
o2 = open(lst+"_desc",'w')
with open(lst,'rb') as f5:
    for l5 in f5:
        l5_split = l5.split('\t')
        tid = l5_split[1].strip().strip('\n')
        sys.stdout.write(">"+l5)

        indexes = [x for x,e in enumerate(nmapid) if e == tid]
        sys.stdout.write("#BlastN\n")
        for hid in indexes:
            gi = nmapgi[hid]
            gp = nmapgroup[hid]
            tx = nmaptaxon[hid]
            if gi in n_gi:
                gi_desc = n_gidesc[n_gi.index(gi)]
            sys.stdout.write("#Desc"+'\t'+nmapline[hid].strip('\n') + '\t' + gi_desc + '\n')
            o2.write(nmapline[hid].strip('\n') + '\t' + gi_desc + '\n')
            allind = [x for x, e in enumerate(nid) if e == nmapid[hid]]
            for i in allind:
                if ngroup[i] == "#XC1":
                    gpc = "6B"
                elif ngroup[i] == "#XC2":
                    gpc = "6C"
                elif ngroup[i] == "#XCal":
                    gpc = "6A"
                if ngiid[i] == gi and gpc == gp.split('-')[0]:
                    sys.stdout.write(nline[i] + '\n')
        #
        # indexes = [x for x, e in enumerate(xmapid) if e == tid]
        # sys.stdout.write("#BlastX\n")
        # for hid in indexes:
        #     gi = xmapgi[hid]
        #     gp = xmapgroup[hid]
        #     tx = xmaptaxon[hid]
        #     if gi in x_gi:
        #         gi_desc = x_gidesc[x_gi.index(gi)]
        #     sys.stdout.write("#Desc"+'\t'+xmapline[hid].strip('\n') + '\t' + gi_desc + '\n')
        #     o2.write(xmapline[hid].strip('\n') + '\t' + gi_desc + '\n')
        #     allind = [x for x, e in enumerate(xid) if e == xmapid[hid]]
        #     for i in allind:
        #         if xgroup[i] == "#XC1":
        #             gpc = "6B"
        #         elif xgroup[i] == "#XC2":
        #             gpc = "6C"
        #         elif xgroup[i] == "#XCal":
        #             gpc = "6A"
        #         if xgiid[i] == gi and gpc == gp.split('-')[0]:
        #             sys.stdout.write(xline[i] + '\n')