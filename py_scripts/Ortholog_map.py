#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""

import sys
filea = sys.argv[1]
filec = sys.argv[2]

cDNA = "/mnt/nfs/media/LIN_eclipse/2015/20150907_ortho201410/check_description_Ay/group2members/inv_div.txt_uniqueseqID.txt_keyword_col.gpatID"

Protein = "/mnt/nfs/media/LIN_eclipse/2015/20150907_ortho201410/check_description_Ay/proteinV3_desc/Scylla_paramamosain_protein.txt.desc"

Contig = "/mnt/nfs/media/LIN_eclipse/2015/20150907_ortho201410/check_description_Ay/BlastDescription.tsv_blastxp.tophit_org.id"

EST = "/mnt/nfs/media/LIN_eclipse/2015/20150907_ortho201410/check_description_Ay/BlastDescription.tsv_blasxp.tophit.summary_orgid"

groupType = []
clstID = []
SeqType = []
SeqIDList = []
species = []
with open(filea,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        groupType.append(l1_split[0])
        clstID.append(l1_split[1])
        species.append(l1_split[2])
        SeqType.append(l1_split[3])
        SeqIDList.append(l1_split[4])

cDNA_id = []
cDNA_desc = []
with open(cDNA, 'rb') as fc:
    for lc in fc:
        lc_split = lc.split('\t')
        cDNA_id.append(lc_split[0].strip())
        cDNA_desc.append(lc_split[3])

Protein_id = []
Protein_desc = []
with open(Protein, 'rb') as fd:
    for ld in fd:
        ld_split = ld.split('\t')
        Protein_id.append(ld_split[0].strip())
        Protein_desc.append(ld_split[3])

contig_id = []
contig_desc = []
with open(Contig, 'rb') as fe:
    for le in fe:
        le_split = le.split('\t')
        contig_id.append(le_split[0].strip())
        contig_desc.append(le_split[1].strip('\n'))

est_id = []
est_desc = []
with open(EST, 'rb') as ff:
    for lf in ff:
        lf_split = lf.split('\t')
        est_id.append(lf_split[0].strip())
        est_desc.append(lf_split[1].strip('\n'))


with open(filec, 'rb') as f2:
    for l2 in f2:
        l2_split = l2.split('\t')
        clst = l2_split[0]
        gtype = l2_split[1]
        clstind = [i for i,e in enumerate(clstID) if e == clst and gtype == groupType[i]]

        sys.stdout.write("#\n")
        sys.stdout.write(l2)
        for ind in clstind:
            allseqid = SeqIDList[ind].split(',')
            desc = ""
            tmp = "-"
            if SeqType[ind] == "EST":
                for sid in allseqid:
                    if sid.strip() in est_id:
                        if desc == "":
                            desc = est_desc[est_id.index(sid.strip())]
                        else:
                            desc += est_desc[est_id.index(sid.strip())]
                tmp = clstID[ind] + '\t' + groupType[ind] + '\t' + species[ind] + '\t' + SeqType[ind] + "\t" + str(len(SeqIDList[ind].split(','))) + "\t" + desc

            elif SeqType[ind] == "Contigs" or SeqType[ind] == "CONTIGs":
                for sid in allseqid:
                    if sid.strip() in contig_id:
                        if desc == "":
                            desc = contig_desc[contig_id.index(sid.strip())]
                        else:
                            desc += contig_desc[contig_id.index(sid.strip())]
                tmp = clstID[ind] + '\t' + groupType[ind] + '\t' + species[ind] + '\t' + SeqType[ind] + "\t" + str(len(SeqIDList[ind].split(','))) + "\t" + desc

            elif SeqType[ind] == "cDNA":
                for sid in allseqid:
                    if sid.strip() in cDNA_id:
                        if desc == "":
                            desc = cDNA_desc[cDNA_id.index(sid.strip())]
                        else:
                            desc += cDNA_desc[cDNA_id.index(sid.strip())]
                tmp = clstID[ind]+'\t'+groupType[ind]+'\t'+species[ind]+'\t'+ SeqType[ind] + "\t" +str(len(SeqIDList[ind].split(','))) + "\t" + desc

            elif SeqType[ind] == "Protein":
                for sid in allseqid:
                    if sid in Protein_id:
                        if desc == "":
                            desc = Protein_desc[Protein_id.index(sid)]
                        else:
                            desc += Protein_desc[Protein_id.index(sid)]
                tmp = clstID[ind]+'\t'+groupType[ind]+'\t'+species[ind]+'\t' + SeqType[ind] + "\t" + str(len(SeqIDList[ind].split(','))) + "\t" + desc
            sys.stdout.write(tmp+'\n')

