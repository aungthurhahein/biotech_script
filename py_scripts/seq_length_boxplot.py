"""
draw a box plot from list of sequence length
__author__ = 'aung'
Date: 24022015
"""
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
# e01
e01_mira_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e01/e01_pv_out.unpadded.fasta_lngth_lngthcol")
e01_cap397_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e01/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.cap3097.contigs_lngth_lngthcol")
e01_cap3DF_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e01/pv_aunguniq_all.fasta.screen.cm.ge50.fasta.cap3DF.contigs_lngth_lngthcol")
e01_trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e01/Trinity.fasta_lngth_lngthcol")

# e02
e02_mira_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e02/e02_pv_out.unpadded.fasta_lngth_lngthcol")
e02_cap397_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e02/pv_aunguniq_all.fasta.screen.cm.fasta-50.masked.rm.fasta-50.fna.cap3097.contigs_lngth_lngthcol")
e02_cap3DF_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e02/pv_aunguniq_all.fasta.screen.cm.fasta-50.masked.rm.fasta-50.fna.cap3DF.contigs_lngth_lngthcol")
e02_trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PV/e02/Trinity.fasta_lngth_lngthcol")

e01_mira = Box(y = e01_mira_array, name = "e01pv_mira")
e01_cap397 = Box(y = e01_cap397_array, name = "e01pv_cap397")
e01_cap3DF = Box(y = e01_cap3DF_array, name = "e01pv_cap3DF")
e01_trinity = Box(y = e01_trinity_array, name = "e01pv_trinity")
e02_mira = Box(y = e02_mira_array, name = "e02pv_mira")
e02_cap397 = Box(y = e02_cap397_array, name = "e02pv_cap397")
e02_cap3DF = Box(y = e02_cap3DF_array, name = "e02pv_cap3DF")
e02_trinity = Box(y = e02_trinity_array, name = "e02pv_trinity")

layout1 = Layout(
    yaxis=YAxis(
        title="sequence lengtt(bp)",
        range=[0,2000]
    )
)

layout2 = Layout(
    yaxis=YAxis(
        title="sequence lengtt(bp)",
        range=[2000,6000]
    )
)

data = Data([e01_cap397, e01_cap3DF, e01_mira, e01_trinity,e02_cap397,e02_cap3DF,e02_mira,e02_trinity])
fig = Figure(data=data, layout=layout1)
fig2 = Figure(data=data, layout=layout2)
# plot_url = py.plot(fig, filename='Sequence Length Distribution')
py.image.save_as(fig, 'sequencelengthdistribution_pv_0_2k.png')
py.image.save_as(fig2, 'sequencelengthdistribution_pv_2k_16k.png')
