"""
draw a box plot from list of sequence length
__author__ = 'Aung'
Date: 24022015
"""
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
# e01
trinity_SRR988098 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR988098_Trinity_lngth_lngthcol")
trinity_SRR1037362 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/SRR1037362.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037363 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/SRR1037363.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037364 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/SRR1037364.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037365 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/SRR1037365.Trinity.fasta_lngth_lngthcol")
trinity_SRR1037366 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/SRR1037366.Trinity.fasta_lngth_lngthcol")
trinity_SRR839236 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR839236.Trinity.fasta_lngth_lngthcol")
trinity_SRR842572 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR842572.Trinity.fasta_lngth_lngthcol")
trinity_SRR842625 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR842625.Trinity.fasta_lngth_lngthcol")
trinity_SRR842627 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR842627.Trinity.fasta_lngth_lngthcol")
trinity_SRR653437 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR653437.Trinity.fasta_lngth_lngthcol")
trinity_SRR1039534 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                   "trinity_SE/Trinity_SRR1039534_out.Trinity.fasta_lngth_lngthcol")
trinity_SRR839222 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei"
                                  "/trinity_SE/SRR839222.Trinity.fasta_lngth_lngthcol")
trinity_SRR839222 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "trinity_SE/SRR839222.Trinity.fasta_lngth_lngthcol")

trinity_SRX020083 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "SRX/SRX020083.Trinity.fasta_lngth_lngthcol")
trinity_SRX181883 = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/SRA_Lvannamei/"
                                  "SRX/SRX181883.Trinity.fasta_lngth_lngthcol")

trinity_SRR988098_box = Box(y =trinity_SRR988098, name = "SRR988098_Trinity")
trinity_SRR1037362_box = Box(y =trinity_SRR1037362, name = "SRR1037362_Trinity")
trinity_SRR1037363_box = Box(y =trinity_SRR1037363, name = "SRR1037363_Trinity")
trinity_SRR1037364_box = Box(y =trinity_SRR1037364, name = "SRR1037364_Trinity")
trinity_SRR1037365_box = Box(y =trinity_SRR1037365, name = "SRR1037365_Trinity")
trinity_SRR1037366_box = Box(y =trinity_SRR1037366, name = "SRR1037366_Trinity")
trinity_SRR839236_box = Box(y =trinity_SRR839236, name = "SRR839236_Trinity")
trinity_SRR842572_box = Box(y =trinity_SRR842572, name = "SRR842572_Trinity")
trinity_SRR842625_box = Box(y =trinity_SRR842625, name = "SRR842625_Trinity")
trinity_SRR842627_box = Box(y =trinity_SRR842627, name = "SRR842627_Trinity")
trinity_SRR653437_box = Box(y =trinity_SRR653437, name = "SRR653437_Trinity")
trinity_SRR1039534_box = Box(y =trinity_SRR1039534, name = "SRR1039534_Trinity")
trinity_SRR839222_box = Box(y =trinity_SRR839222, name = "SRR839222_Trinity")

trinity_SRX181883_box = Box(y =trinity_SRX181883, name = "SRX181883.Trinity")
trinity_SRX020083_box = Box(y =trinity_SRX020083, name = "SRX020083.Trinity")

layout1 = Layout(
    yaxis=YAxis(
        title="sequence lengtt(bp)",
        range=[0,2000]
    )
)

layout2 = Layout(
    yaxis=YAxis(
        title="sequence lengtt(bp)",
        range=[2000,16000]
    )
)

data = Data([trinity_SRR988098_box, trinity_SRR1037362_box, trinity_SRR1037363_box, trinity_SRR1037364_box,
             trinity_SRR1037365_box, trinity_SRR1037366_box, trinity_SRR839236_box, trinity_SRR842572_box,
             trinity_SRR842625_box, trinity_SRR842627_box, trinity_SRR653437_box, trinity_SRR1039534_box,
             trinity_SRR839222_box, trinity_SRX181883_box,trinity_SRX020083_box])
fig = Figure(data=data, layout=layout1)
fig2 = Figure(data=data, layout=layout2)
# plot_url = py.plot(fig, filename='Sequence Length Distribution')
py.image.save_as(fig, 'sequencelengthdistribution_pv_illumina_SR_0_2k.png')
py.image.save_as(fig2, 'sequencelengthdistribution_pv_illumina_SR_2k_16k.png')