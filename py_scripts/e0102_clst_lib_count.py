# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-05-03 13:53:29
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-05-04 16:25:16
import sys

clstfile = "/mnt/nfs/media/Aung/e0102_cdhit_lib/unmap_cdhit_out.clstr.parse_G3reflib"

def readfile(file):
    listname = []
    with open(file,'rb') as f1:
        for l1 in f1:
            l1_split = l1.split()
            listname.append(l1_split[0].strip().strip('>'))
    return listname

#chula
chula = "/mnt/nfs/media/Aung/EST_lib_IDs/pm/slect_bytissues_pm_chula/"
Tw_N = readfile(chula+"PM82_wTempLibID_04092014.txt.PmTwN.seqID")
Tw_I = readfile(chula+"PM82_wTempLibID_04092014.txt.PmTwI.seqID")
HC_NN = readfile(chula+"PM82_wTempLibID_04092014.txt.HC-N-N01.seqID")
HC_NS = readfile(chula+"PM82_wTempLibID_04092014.txt.HC-N-S01.seqID")
HC_V = readfile(chula+"PM82_wTempLibID_04092014.txt.HC-V-S01.seqID")
HC_W = readfile(chula+"PM82_wTempLibID_04092014.txt.HC-W-S01.seqID")
LP_NN = readfile(chula+"PM82_wTempLibID_04092014.txt.LP-N-N01.seqID")
LP_NS = readfile(chula+"PM82_wTempLibID_04092014.txt.LP-N-S01.seqID")
LP_V = readfile(chula+"PM82_wTempLibID_04092014.txt.LP-V-S01.seqID")
LP_Y = readfile(chula+"PM82_wTempLibID_04092014.txt.LP-Y-S01.seqID")

#ncbi
ncbi = "/mnt/nfs/media/Aung/EST_lib_IDs/pm/slect_bytissues_pm/"
Gill_N = readfile(ncbi+"NCBI01-Gill-N.fasta_lngth")
Gill_W = readfile(ncbi+"NCBI01-Gill-W.fasta_lngth")
HC_N = readfile(ncbi+"NCBI01-HC-N.fasta_lngth")
HC_W2 = readfile(ncbi+"NCBI01-HC-W.fasta_lngth")
HC_Y = readfile(ncbi+"NCBI01-HC-Y.fasta_lngth")
HC_V2 = readfile(ncbi+"NCBI01-HC-V.fasta_lngth")
LY_N = readfile(ncbi+"NCBI01-LY-N.fasta_lngth")
LY_Y = readfile(ncbi+"NCBI01-LY-Y.fasta_lngth")
LY_V = readfile(ncbi+"NCBI01-LY-V.fasta_lngth")
WH_W = readfile(ncbi+"NCBI01-WH-W.fasta_lngth")
WH_N = readfile(ncbi+"NCBI01-WH-N.fasta_lngth")
WH_V = readfile(ncbi+"NCBI01-WH-V.fasta_lngth")
ML_W = readfile(ncbi+"NCBI01-ML-W.fasta_lngth")
ML_N = readfile(ncbi+"NCBI01-ML-N.fasta_lngth")

pv = "/mnt/nfs/media/Aung/EST_lib_IDs/pv/sequencebySets/"
PVGill_N = readfile(pv+"GillN.fasta_lngth")
PVGill_W = readfile(pv+"GillW.fasta_lngth")
PVHP_N  = readfile(pv+"HPN.fasta_lngth")
PVHP_W = readfile(pv+"HPW.fasta_lngth")
PVHe_N  = readfile(pv+"HeN.fasta_lngth")
PVHe_W = readfile(pv+"HeW.fasta_lngth")

with open(clstfile,'rb') as f2:
        for l2 in f2:
            pm_id = "-"
            pv_id = "-"
            Tw_N_count = 0 
            Tw_I_count = 0
            HC_NN_count = 0
            HC_NS_count = 0
            HC_V_count = 0
            HC_W_count = 0
            LP_NN_count = 0
            LP_NS_count = 0
            LP_V_count = 0
            LP_Y_count = 0

            Gill_N_count = 0
            Gill_W_count = 0
            HC_N_count = 0
            HC_W2_count = 0
            HC_Y_count = 0
            HC_V2_count = 0
            LY_N_count = 0
            LY_Y_count = 0
            LY_V_count = 0
            WH_W_count = 0
            WH_N_count = 0
            WH_V_count = 0
            ML_W_count = 0
            ML_N_count = 0

            PVGill_N_count = 0
            PVGill_W_count = 0
            PVHP_N_count = 0
            PVHP_W_count = 0
            PVHe_N_count = 0
            PVHe_W_count = 0

            for m in l2.split('\t'):
                m = m.strip('>').strip()
                print m
                if "Cluster" in m:
                    id_ = m
                elif "PM_e" in m:
                    if pm_id == "-":                        
                        pm_id = m
                    else:
                        pm_id += ";"+m
                elif "PV_e" in m:
                    if pv_id == "-":                        
                        pv_id = m
                    else:
                        pv_id += ";"+m                
                elif m in Tw_N:
                    Tw_N_count +=1
                elif m in Tw_I:
                    Tw_I_count +=1
                elif m in HC_NN:
                    HC_NN_count +=1
                elif m in HC_NS:
                    HC_NS_count +=1
                elif m in HC_V:
                    HC_V_count +=1
                elif m in HC_W:
                    HC_W_count +=1
                elif m in LP_NN:
                    LP_NN_count +=1
                elif m in LP_NS:
                    LP_NS_count +=1
                elif m in LP_V:
                    LP_V_count +=1
                elif m in LP_Y:
                    LP_Y_count +=1

                elif m in Gill_N:
                    Gill_N_count +=1
                elif m in Gill_W:
                    Gill_W_count +=1
                elif m in HC_N:
                    HC_N_count +=1
                elif m in HC_W2:
                    HC_W2_count +=1
                elif m in HC_Y:
                    HC_Y_count +=1
                elif m in HC_V2:
                    HC_V2_count +=1
                elif m in LY_N:
                    LY_N_count +=1
                elif m in LY_Y:
                    LY_Y_count +=1
                elif m in LY_V:
                    LY_V_count +=1
                elif m in WH_W:
                    WH_W_count +=1
                elif m in WH_N:
                    WH_N_count +=1
                elif m in WH_V:
                    WH_V_count +=1
                elif m in ML_W:
                    ML_W_count +=1
                elif m in ML_N:               
                    ML_N_count +=1

                elif m in PVGill_N:
                    PVGill_N_count += 1
                elif m in PVGill_W:
                    PVGill_W_count += 1
                elif m in PVHP_N:
                    PVHP_N_count += 1
                elif m in PVHP_W:
                    PVHP_W_count += 1
                elif m in PVHe_N:
                    PVHe_N_count += 1
                elif m in PVHe_W:
                    PVHe_W_count += 1           
            sys.stdout.write(id_+'\t'+pm_id+'\t'+pv_id+'\t'+str(Tw_N_count)+"\t"+str(Tw_I_count)+"\t"+str(HC_NN_count)+"\t"+str(HC_NS_count)
            +"\t"+str(HC_V_count)+"\t"+str(HC_W_count)+"\t"+str(LP_NN_count)+"\t"+str(LP_NS_count)+"\t"+str(LP_V_count)+"\t"+
            str(Gill_N_count)+"\t"+str(Gill_W_count)+"\t"+str(HC_N_count)+"\t"+str(HC_W2_count)+"\t"+str(HC_Y_count)+"\t"+
            str(HC_V2_count)+"\t"+str(LY_N_count)+"\t"+str(LY_Y_count)+"\t"+str(LY_V_count)+"\t"+str(WH_W_count)+"\t"+
            str(WH_N_count)+"\t"+str(WH_V_count)+"\t"+str(ML_W_count)+"\t"+str(PVGill_N_count)+"\t"+str(PVGill_W_count)+
            "\t"+str(PVHP_N_count)+"\t"+str(PVHP_W_count)+"\t"+str(PVHe_N_count)+"\t"+str(PVHe_W_count)+"\n")



            Tw_N_count 
            Tw_I_count 
            HC_NN_count 
            HC_NS_count 
            HC_V_count 
            HC_W_count 
            LP_NN_count 
            LP_NS_count 
            LP_V_count 
            LP_Y_count 

            Gill_N_count 
            Gill_W_count 
            HC_N_count 
            HC_W2_count 
            HC_Y_count 
            HC_V2_count 
            LY_N_count 
            LY_Y_count 
            LY_V_count 
            WH_W_count 
            WH_N_count 
            WH_V_count 
            ML_W_count 
            ML_N_count 

            PVGill_N_count 
            PVGill_W_count 
            PVHP_N_count 
            PVHP_W_count 
            PVHe_N_count 
            PVHe_W_count 
            Tw_N_count 
            Tw_I_count 
            HC_NN_count 
            HC_NS_count 
            HC_V_count 
            HC_W_count 
            LP_NN_count 
            LP_NS_count 
            LP_V_count 
            LP_Y_count 

            Gill_N_count 
            Gill_W_count 
            HC_N_count 
            HC_W2_count 
            HC_Y_count 
            HC_V2_count 
            LY_N_count 
            LY_Y_count 
            LY_V_count 
            WH_W_count 
            WH_N_count 
            WH_V_count 
            ML_W_count 
            ML_N_count 

            PVGill_N_count
            PVGill_W_count
            PVHP_N_count
            PVHP_W_count
            PVHe_N_count
            PVHe_W_count