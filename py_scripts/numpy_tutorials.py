__author__ = 'aung'

from numpy import *
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
"""
array
"""
a = arange(20).reshape(4, 5)
b = array([6, 7, 8])
print b
# row,column
print a.shape
# dimension
print a.ndim
# datatype
print a.dtype.name
# size of each tuple
print a.itemsize
# no. of tuple
print a.size
# type of object
print type(a)
print a

"""
panda dataframe
"""
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print s

# read from tsv
data = pd.read_table('/home/aung/server_downloads/c01_MIRA_DE/trans/21.tsv')
print data
print data.dtypes
print data.mean()

f = '/home/aung/server_downloads/c01_MIRA_DE/trans/21.tsv'
f1 = open(f, 'r')

# print f1.readlines()

for item, index in enumerate(f1):
    print item, index
