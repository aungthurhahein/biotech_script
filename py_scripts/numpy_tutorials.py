__author__ = 'aung'

from numpy import *

"""
array
"""
a = arange(20).reshape(4,5)
b = array([6,7,8])
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
