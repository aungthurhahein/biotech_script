"""
draw a box plot from list of sequence length
__author__ = 'Aung'
Date: 24022015
"""
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

# a01
a01_mira_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/a01/a01_mira_lngth.txt_lngthcol")
a01_454_trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/"
                                      "a01/a01_454_Trinity_lngth.txt_lngthcol")

# e01
e01pm_cap397_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e01/"
                                  "e01_pm.fasta.fna.cap3097.contigs_lngth.txt_lngthcol")
e01pm_cap3DF_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e01/"
                                 "e01_pm.fasta.fna.cap3DF.contigs_lngth.txt_lngthcol")
e01pm_mira_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e01/"
                                 "e01_pm_out.unpadded.fasta_lngth.txt_lngthcol")
e01pm_trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e01/"
                                 "Trinity.fasta_lngth.txt_lngthcol")
# e02
e02pm_cap397_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e02/"
                                   "e02_pm.fasta.fna.cap3097.contigs_lngth.txt_lngthcol")
e02pm_cap3DF_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e02/"
                                   "e02_pm.fasta.fna.cap3DF.contigs_lngth.txt_lngthcol")
e02pm_mira_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e02/"
                                 "e02_pm_out.unpadded.fasta_lngth.txt_lngthcol")
e02pm_trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/e02/"
                                 "Trinity.fasta_lngth.txt_lngthcol")

# illumina_trinity_PE
illumina_trinity_SRR388207_PE_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/illumina_trinity_PE/"
                                                 "Trinity_SRR388207_out.fasta_lngth.txt_lngthcol")
illumina_trinity_SRR388221_PE_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/illumina_trinity_PE/"
                                                "illumina_SRR388221_out.Trinity.fasta_lngth.txt_lngthcol")
illumina_trinity_SRR388222_PE_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/illumina_trinity_PE/"
                                                 "Trinity_SRR388222_out.fasta_lngth.txt_lngthcol")
# illumina_trinity_SR
illumina_trinity_SRR388207_SR_array = np.genfromtxt(
                                    "/home/aung/server_downloads/length_distribution/PM/illumina_trinity_SR/"
                                    "illumina_SRR388207_out.Trinity.fasta_lngth.txt_lngthcol")
illumina_trinity_SRR388221_SR_array = np.genfromtxt(
                                    "/home/aung/server_downloads/length_distribution/PM/illumina_trinity_SR/"
                                    "illumina_SR388221_out.Trinity.fasta_lngth.txt_lngthcol")
illumina_trinity_SRR388222_SR_array = np.genfromtxt(
                                    "/home/aung/server_downloads/length_distribution/PM/illumina_trinity_SR/"
                                    "illumina_SR388222_out.Trinity.fasta_lngth.txt_lngthcol")
# c01
c01_MIRA_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/c01/c01_MIRA_lngth.txt_lngthcol")
c01_Trinity_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/c01/c01_Trinity_lngth.txt_lngthcol")
c01_newbler_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/454Isotigs.fna_lngth_lngthcol")

Testis_Ovary_array = np.genfromtxt("/home/aung/server_downloads/length_distribution/PM/all_pmonodon.fasta.lngth_lngthcol")

a01_mira = Box(
    y=a01_mira_array,
    name= "a01_mira"
)
a01_454_trinity = Box(
    y=a01_454_trinity_array,
    name="a01_454_trinity"
)
e01pm_cap397= Box(
    y= e01pm_cap397_array,
    name = "e01pm_cap397"
)
e01pm_cap3DF= Box(
    y= e01pm_cap3DF_array,
    name="e01pm_cap3DF"
)
e01pm_mira= Box(
    y= e01pm_mira_array,
    name="e01pm_mira"
)
e01pm_trinity= Box(
    y= e01pm_trinity_array,
    name="e01pm_trinity"
)
e02pm_cap397 = Box(
    y= e02pm_cap397_array,
    name="e02_pm_cap397"
)
e02pm_cap3DF = Box(
    y= e02pm_cap3DF_array,
    name="e02_pm_cap3DF"
)
e02pm_mira = Box(
    y=e02pm_mira_array,
    name="e02pm_mira"
)
e02pm_trinity = Box(
    y=e02pm_trinity_array,
    name="e02pm_trinity"
)
illumina_trinity_SRR388207_PE = Box(
    y=illumina_trinity_SRR388207_PE_array,
    name="illumina_trinity_SRR388207_PE"
)
illumina_trinity_SRR388221_PE = Box(
    y=illumina_trinity_SRR388221_PE_array,
    name="illumina_trinity_SRR388221_PE"
)
illumina_trinity_SRR388222_PE = Box(
    y= illumina_trinity_SRR388222_PE_array,
    name="illumina_trinity_SRR388222_PE"
)

illumina_trinity_SRR388207_SR = Box(
    y=illumina_trinity_SRR388207_SR_array,
    name="illumina_trinity_SRR388207_SR"
)
illumina_trinity_SRR388221_SR = Box(
    y=illumina_trinity_SRR388221_SR_array,
    name="illumina_trinity_SRR388221_SR"
)
illumina_trinity_SRR388222_SR = Box(
    y= illumina_trinity_SRR388222_SR_array,
    name="illumina_trinity_SRR388222_SR"
)
c01_MIRA = Box(
    y= c01_MIRA_array,
    name="c01_MIRA"
)
c01_Trinity = Box(
    y= c01_Trinity_array,
    name="C01_Trinity"
)
c01_newbler = Box(
    y= c01_newbler_array,
    name="C01_Newbler"
)
Testis_Ovary = Box(
    y=Testis_Ovary_array,
    name="Testis_Ovary"
)

layout1 = Layout(
    yaxis=YAxis(
        range=[0,2000]
    )
)

layout2 = Layout(
    yaxis=YAxis(
        range=[2000,16000]
    )
)

data = Data([a01_mira, a01_454_trinity, e01pm_cap397, e01pm_cap3DF, e01pm_mira, e01pm_trinity,e02pm_cap397,e02pm_cap3DF, e02pm_mira, e02pm_trinity,illumina_trinity_SRR388207_PE,illumina_trinity_SRR388221_PE,illumina_trinity_SRR388222_PE,illumina_trinity_SRR388207_SR,illumina_trinity_SRR388221_SR,illumina_trinity_SRR388222_SR, c01_MIRA, c01_Trinity, c01_newbler, Testis_Ovary])
fig = Figure(data=data, layout=layout1)
fig2 = Figure(data=data, layout=layout2)
# plot_url = py.plot(fig, filename='Sequence Length Distribution')
py.image.save_as(fig, 'sequencelengthdistribution_PM_0_2k.png')
py.image.save_as(fig2, 'sequencelengthdistribution_PM_2k_16k.png')