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

A1 = Data([
    Histogram(
        x=a1,
        marker=Marker(
            color='#1b9e77')
    )
])
A2 = Data([
    Histogram(
        x=a2,
        marker=Marker(
            color='#d95f02')
    )
])
A3 = Data([
    Histogram(
        x=a3,
        marker=Marker(
            color='#7570b3')
    )
])
A4 = Data([
    Histogram(
        x=a4,
        marker=Marker(
            color='#e7298a')
    )
])
B1 = Data([
    Histogram(
        x=b1,
        marker=Marker(
            color='#66a61e')
    )
])
B2 = Data([
    Histogram(
        x=b2,
        marker=Marker(
            color='#e6ab02')
    )
])
B3 = Data([
    Histogram(
        x=b3,
        marker=Marker(
            color='#a6761d')
    )
])
B4 = Data([
    Histogram(
        x=b4,
        marker=Marker(
            color='#666666')
    )
])

py.image.save_as(A1, 'histogram-A1.jpeg')
py.image.save_as(A2, 'histogram-A2.jpeg')
py.image.save_as(A3, 'histogram-A3.jpeg')
py.image.save_as(A4, 'histogram-A4.jpeg')
py.image.save_as(B1, 'histogram-B1.jpeg')
py.image.save_as(B2, 'histogram-B2.jpeg')
py.image.save_as(B3, 'histogram-B3.jpeg')
py.image.save_as(B4, 'histogram-B4.jpeg')
