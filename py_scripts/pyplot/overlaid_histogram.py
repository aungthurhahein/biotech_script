#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

a1 = np.genfromtxt('/home/aung/server_downloads/histogram/A1.lngth')
a2 = np.genfromtxt('/home/aung/server_downloads/histogram/A2.lngth')
a3 = np.genfromtxt('/home/aung/server_downloads/histogram/A3.lngth')
a4 = np.genfromtxt('/home/aung/server_downloads/histogram/A4.lngth')
b1 = np.genfromtxt('/home/aung/server_downloads/histogram/B1.lngth')
b2 = np.genfromtxt('/home/aung/server_downloads/histogram/B2.lngth')
b3 = np.genfromtxt('/home/aung/server_downloads/histogram/B3.lngth')
b4 = np.genfromtxt('/home/aung/server_downloads/histogram/B4.lngth')

A1 = Histogram(
    x=a1,
    name='A1',
    marker=Marker(
        color='#1b9e77',
        line= Line(
            color='grey',
            width=0
        ),
        opacity=0.75
    )
)
A2 = Histogram(
    x=a2,
    name='A2',
    marker=Marker(
        color='#d95f02',
        opacity=0.75
    )
)
A3 = Histogram(
    x=a3,
    name='A3',
    marker=Marker(
        color='#7570b3',
        opacity=0.75
    )
)
A4 = Histogram(
    x=a4,
    name='A4',
    marker=Marker(
        color='#e7298a',
        opacity=0.75
    )
)
B1 = Histogram(
    x=b1,
    name='B1',
    marker=Marker(
        color='#66a61e',
        opacity=0.75
    )
)
B2 = Histogram(
    x=b2,
    name='B2',
    marker=Marker(
        color='#e6ab02',
        opacity=0.75
    )
)
B3 = Histogram(
    x=b3,
    name='B3',
    marker=Marker(
        color='#a6761d',
        opacity=0.75
    )
)
B4 = Histogram(
    x=b4,
    name='B4',
    marker=Marker(
        color='#666666',
        opacity=0.75
    )
)

data = Data([A1, A2, A3, A4, B1, B2, B3, B4])

layout = Layout(
    barmode='stack',
    yaxis=YAxis(
        range=[0, 2000]
    )
)
layout2 = Layout(
    barmode='stack',
    yaxis=YAxis(
        range=[2000, 20000]
    )
)

fig = Figure(data=data, layout=layout)
fig2 = Figure(data=data, layout=layout2)

py.image.save_as(fig, 'histogram-stack1.jpeg')
py.image.save_as(fig2, 'histogram-stack2.jpeg')