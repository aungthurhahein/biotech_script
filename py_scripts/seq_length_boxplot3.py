__author__ = 'Aung'
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

il_pe_path = "/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/trinity_PE/"
il_mira_path = "/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/PE_MIRA/"

trinity_SRR1037362 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1037362_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037363 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1037363_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037364 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1037364_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037365 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1037365_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037366 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1037366_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR1039534 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR1039534_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR839222 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR839222_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR839236 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR839236_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR842572 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR842572_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR842625 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR842625_Out.Trinity.fasta_lngth_lngthcol")
trinity_SRR842627 = np.genfromtxt(il_pe_path+"Trinity_PE_SRR842627_Out.Trinity.fasta_lngth_lngthcol")

mira_SRR1037362 = np.genfromtxt(il_mira_path+"SRR1037362_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR1037363 = np.genfromtxt(il_mira_path+"SRR1037363_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR1037364 = np.genfromtxt(il_mira_path+"SRR1037364_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR1037365 = np.genfromtxt(il_mira_path+"SRR1037365_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR1037366 = np.genfromtxt(il_mira_path+"SRR1037366_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR839222 = np.genfromtxt(il_mira_path+"SRR839222_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR839236 = np.genfromtxt(il_mira_path+"SRR839236_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR842572 = np.genfromtxt(il_mira_path+"SRR842572_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR842625 = np.genfromtxt(il_mira_path+"SRR842625_manifest_out.unpadded.fasta_lngth_lngthcol")
mira_SRR842627 = np.genfromtxt(il_mira_path+"SRR842627_manifest_out.unpadded.fasta_lngth_lngthcol")


trinity_SRR1037362_box = Box(y =trinity_SRR1037362, name = "SRR1037362_Trinity_PE")
trinity_SRR1037363_box = Box(y =trinity_SRR1037363, name = "SRR1037363_Trinity_PE")
trinity_SRR1037364_box = Box(y =trinity_SRR1037364, name = "SRR1037364_Trinity_PE")
trinity_SRR1037365_box = Box(y =trinity_SRR1037365, name = "SRR1037365_Trinity_PE")
trinity_SRR1037366_box = Box(y =trinity_SRR1037366, name = "SRR1037366_Trinity_PE")
trinity_SRR839236_box = Box(y =trinity_SRR839236, name = "SRR839236_Trinity_PE")
trinity_SRR842572_box = Box(y =trinity_SRR842572, name = "SRR842572_Trinity_PE")
trinity_SRR842625_box = Box(y =trinity_SRR842625, name = "SRR842625_Trinity_PE")
trinity_SRR842627_box = Box(y =trinity_SRR842627, name = "SRR842627_Trinity_PE")
trinity_SRR1039534_box = Box(y =trinity_SRR1039534, name = "SRR1039534_Trinity_PE")
trinity_SRR839222_box = Box(y =trinity_SRR839222, name = "SRR839222_Trinity_PE")

mira_SRR1037362_box = Box(y =mira_SRR1037362, name = "SRR1037362_IL_PE")
mira_SRR1037363_box = Box(y =mira_SRR1037363, name = "SRR1037363_IL_PE")
mira_SRR1037364_box = Box(y =mira_SRR1037364, name = "SRR1037364_IL_PE")
mira_SRR1037365_box = Box(y =mira_SRR1037365, name = "SRR1037365_IL_PE")
mira_SRR1037366_box = Box(y =mira_SRR1037366, name = "SRR1037366_IL_PE")
mira_SRR839236_box = Box(y =mira_SRR839236, name = "SRR839236_IL_PE")
mira_SRR842572_box = Box(y =mira_SRR842572, name = "SRR842572_IL_PE")
mira_SRR842625_box = Box(y =mira_SRR842625, name = "SRR842625_IL_PE")
mira_SRR842627_box = Box(y =mira_SRR842627, name = "SRR842627_IL_PE")
# mira_SRR1039534_box = Box(y =mira_SRR1039534, name = "SRR1039534_IL_PE")
mira_SRR839222_box = Box(y =mira_SRR839222, name = "SRR839222_IL_PE")


layout1 = Layout(
    yaxis=YAxis(
        title="sequence length(bp)",
        range=[0,2000]
    )
)

layout2 = Layout(
    yaxis=YAxis(
        title="sequence length(bp)",
        range=[2000,10000]
    )
)

data = Data([trinity_SRR1037362_box, mira_SRR1037362_box, trinity_SRR1037363_box, mira_SRR1037363_box, trinity_SRR1037364_box, mira_SRR1037364_box, trinity_SRR1037365_box,mira_SRR1037365_box, trinity_SRR1037366_box, mira_SRR1037366_box, trinity_SRR839236_box, mira_SRR839236_box, trinity_SRR842572_box, mira_SRR842572_box,trinity_SRR842625_box, mira_SRR842625_box, trinity_SRR842627_box, mira_SRR842627_box, trinity_SRR839222_box, mira_SRR839222_box])

fig = Figure(data=data, layout=layout1)
fig2 = Figure(data=data, layout=layout2)
# plot_url = py.plot(fig, filename='Sequence Length Distribution')
py.image.save_as(fig, 'sequencelengthdistribution_pv_illumina_SR_0_2k.png')
py.image.save_as(fig2, 'sequencelengthdistribution_pv_illumina_SR_2k_16k.png')