#! /usr/bin/env/ python

"""
#
# usage:
# output:
# Dev: __author__ = 'aung'
# Date:
"""
import re
import sys
allidlist = sys.argv[1]

base = "/mnt/nfs/media/LIN_eclipse/2015/20150903/Ortho_20150902/analysis/description_MCL/description_ortholog/"
contigs = base+"contigsV22.desc"
e0102 = base+"E0102.desc"
siest = base+"SIEST.desc"
protv22= base+"prov22.desc.sort"
nucl =  base+"Nucl.desc"


# Pool_contigsV22_
contigs_id = []
contigs_desc = []
with open(contigs,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        contigs_id.append(l1_split[0])
        contigs_desc.append(l1_split[1].strip('\n'))

# PVPM_E0102_10001
e0102_id = []
e0102_desc = []
with open(e0102, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        e0102_id.append(l2_split[0])
        e0102_desc.append(l2_split[1].strip('\n'))

# V3_SIEST01_100001
siest_id = []
siest_desc = []
with open(siest, 'rb') as f3:
    for l3 in f3:
        l3_split = l3.split('\t')
        siest_id.append(l3_split[0])
        siest_desc.append(l3_split[1].strip('\n'))

# gi -protein
protv22_id = []
protv22_desc = []
with open(protv22, 'rb') as f4:
    for l4 in f4:
        l4_split = l4.split('\t')
        protv22_id.append(l4_split[0])
        protv22_desc.append(l4_split[1].strip('\n'))

# gpatNuclV3-113
nucl_id = []
nucl_desc = []
with open(nucl, 'rb') as f5:
    for l5 in f5:
        l5_split = l5.split('\t')
        nucl_id.append(l5_split[0])
        nucl_desc.append(l5_split[3].strip('\n'))

# o = open(allidlist+".desc",'w')
# yeso = open(allidlist+".yesdesc",'w')
# noo = open(allidlist+".nodesc",'w')
with open(allidlist,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        mem = l1_split[2].split(';')
        # tmp_desc = ""
        # print groupid
        groupid = l1_split[1]
        sys.stdout.write(">" + groupid + '\n')
        for m in mem:
            tmp_desc = ""
            m = m.strip('\n')
            est = re.search(r'V3_SIEST01_\w+', m)
            contig = re.search(r'Pool_contigsV22_\w+', m)
            e0102 = re.search(r'Prot_PVPM_E0102_\w+', m)
            nucl = re.search(r'gpatNuclV3-\w+', m)
            prot = re.search(r'gi|\w+', m)
            if est:
                indexes = [i for i,e in enumerate(siest_id) if e == m]
                for ind in indexes:
                    out = re.sub(r'\{[^}]*\}', '', siest_desc[ind])
                    sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + out.rstrip('|').rstrip(';').strip() + '\n')
            elif contig:
                indexes = [i for i, e in enumerate(contigs_id) if e == m]
                for ind in indexes:
                    out = re.sub(r'\{[^}]*\}','', contigs_desc[ind])
                    sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + out.rstrip('|').rstrip(';').strip() + '\n')
            elif e0102:
                m_2 = m.split('_')[1] + "_" + m.split('_')[2] + "_" + m.split('_')[3]
                indexes = [i for i, e in enumerate(e0102_id) if e == m_2]
                for ind in indexes:
                    out = re.sub(r'\{[^}]*\}', '', e0102_desc[ind])
                    sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + out.rstrip('|').rstrip(';').strip() + '\n')
            elif nucl:
                indexes = [i for i, e in enumerate(nucl_id) if e == m]
                for ind in indexes:
                    out = re.sub(r'\{[^}]*\}', '', nucl_desc[ind])
                    sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + out.rstrip('|').rstrip(';').strip() + '\n')
            elif prot:
                # print m
                m_2 = m.split('|')[1]
                indexes = [i for i, e in enumerate(protv22_id) if e == m_2]
                for ind in indexes:
                    out = re.sub(r'\{[^}]*\}', '',protv22_desc[ind])
                    sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + out.rstrip('|').rstrip(';').strip() + '\n')

            # else:
                # print m
            # if tmp_desc != "":
            #     sys.stdout.write(groupid + "\t" + ">gi|X|ref|A| " + tmp_desc.rstrip('|').rstrip(';').strip() + '\n')
        sys.stdout.write("//"+'\n')
        # o.write(l1.strip('\n')+'\t'+tmp_desc+'\n')
        # checkdesc = [i for i in tmp_desc.split(";") if i == "NoDesc"]
        # if len(checkdesc) == len(tmp_desc.split(";")):
        #     noo.write(l1.strip('\n')+'\t'+tmp_desc+'\n')
        # else:
        #     yeso.write(l1.strip('\n')+'\t'+tmp_desc+'\n')