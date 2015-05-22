__author__ = 'Aung'
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

il_pe_path = "/home/aung/server_downloads/all_lngth/"
il_mira_path = "/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/PE_MIRA/"

trinity_1 = np.genfromtxt(il_pe_path+"1.txt")
trinity_2 = np.genfromtxt(il_pe_path+"2.txt")
trinity_3 = np.genfromtxt(il_pe_path+"3.txt")
trinity_4 = np.genfromtxt(il_pe_path+"4.txt")
trinity_5 = np.genfromtxt(il_pe_path+"5.txt")
trinity_6 = np.genfromtxt(il_pe_path+"6.txt")
trinity_7 = np.genfromtxt(il_pe_path+"7.txt")
trinity_81 = np.genfromtxt(il_pe_path+"81.txt")
trinity_82 = np.genfromtxt(il_pe_path+"82.txt")
trinity_83 = np.genfromtxt(il_pe_path+"83.txt")
trinity_84 = np.genfromtxt(il_pe_path+"84.txt")
trinity_85 = np.genfromtxt(il_pe_path+"85.txt")
trinity_86 = np.genfromtxt(il_pe_path+"86.txt")
trinity_87 = np.genfromtxt(il_pe_path+"87.txt")
trinity_88 = np.genfromtxt(il_pe_path+"88.txt")


trinity_1_box = Box(y =trinity_1, name = "ATM")
trinity_2_box = Box(y =trinity_2, name = "NonATM")
trinity_3_box = Box(y =trinity_3, name = "ATM Specific (98%)")
trinity_4_box = Box(y =trinity_4, name = "ATM.C01.tophits")
trinity_5_box = Box(y =trinity_5, name = "ATM.C02.tophits")
trinity_6_box = Box(y =trinity_6, name = "ATM.Cal.tophits")
trinity_7_box = Box(y =trinity_7, name = "Sequnce not in ATM.CAl but in ATM Specific")
trinity_81_box = Box(y =trinity_81, name = "95% ID  ATM-specific")
trinity_82_box = Box(y =trinity_82, name = "95% ID  nonShrimp ATM-specific")
trinity_83_box = Box(y =trinity_83, name = "90% ID  ATM-specific")
trinity_84_box = Box(y =trinity_84, name = "90% ID  nonShrimp ATM-specific")
trinity_85_box = Box(y =trinity_85, name = "85% ID  ATM-specific")
trinity_86_box = Box(y =trinity_86, name = "85% ID  nonShrimp ATM-specific")
trinity_87_box = Box(y =trinity_87, name = "80% ID  ATM-specific")
trinity_88_box = Box(y =trinity_88, name = "80% ID  nonShrimp ATM-specific")

layout1 = Layout(
    yaxis=YAxis(
        title="sequence length(bp)",
        range=[0,6000]
    )
)

layout2 = Layout(
    yaxis=YAxis(
        title="sequence length(bp)",
        range=[6000,16000]
    )
)
layout3 = Layout(
    yaxis=YAxis(
        title="sequence length(bp)",
        range=[16000,32000]
    )
)
data = Data([trinity_1_box,trinity_2_box,trinity_3_box,trinity_4_box,trinity_5_box,trinity_6_box,trinity_7_box,trinity_81_box,trinity_82_box,trinity_83_box,trinity_84_box,trinity_85_box,trinity_86_box,trinity_87_box,trinity_88_box])

fig = Figure(data=data, layout=layout1)
fig2 = Figure(data=data, layout=layout2)
fig3 = Figure(data=data, layout=layout3)
# plot_url = py.plot(fig, filename='Sequence Length Distribution')
# py.image.save_as(fig, 'sequencelengthdistribution_ATM_0_6k.png')
py.image.save_as(fig2, 'sequencelengthdistribution_ATM_6k_16k.png')
py.image.save_as(fig3, 'sequencelengthdistribution_ATM_16k_32k.png')