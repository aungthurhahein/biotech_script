#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
matrix = sys.argv[1]
open_matrix = open(matrix,'r')
matrix_list = []

for line in open_matrix:
    matrix_list.append(line)

count98 = 0
count95 = 0
count90 = 0
count85 = 0
count80 = 0
f= open(matrix+"_changeid",'w')
for x in matrix_list:
    x_split = x.strip('\n').split('\t')
    id = x_split[0]
    len = x_split[1]
    cd98 = x_split[2]
    cd95 = x_split[3]
    cd90 = x_split[4]
    cd85 = x_split[5]
    cd80 = x_split[6]
    if cd98 != 'y':
        f.write(id+'\n')
        cd95 = ' '
        cd90 = ' '
        cd85 = ' '
        cd80 = ' '
    elif cd98 != 'y' and cd95 == 'y':
        f.write(id + '\n')
        cd95 = ' '
        cd90 = ' '
        cd85 = ' '
        cd80 = ' '
    elif cd98 != 'y' and cd95 != 'y' and cd90 == 'y':
        f.write(id + '\n')
        cd90 = ' '
        cd85 = ' '
        cd80 = ' '
    elif cd98 != 'y' and cd95 != 'y' and cd90 != 'y' and cd85 == 'y':
        f.write(id + '\n')
        cd85 = ' '
        cd80 = ' '
    elif cd98 != 'y' and cd95 != 'y' and cd90 != 'y' and cd85 != 'y' and cd80 == 'y':
        f.write(id + '\n')
        cd80 = ' '

    elif cd98 == 'y' and cd95 != 'y':
        f.write(id + '\n')
        cd95 = ' '
        cd90 = ' '
        cd85 = ' '
        cd80 = ' '
    elif cd98 == 'y' and cd95 == 'y' and cd90 != 'y':
        f.write(id + '\n')
        cd90 = ' '
        cd85 = ' '
        cd80 = ' '
    elif cd98 == 'y' and cd95 == 'y' and cd90 == 'y' and cd85 != 'y':
        f.write(id + '\n')
        cd85 = ' '
        cd80 = ' '
    elif cd98 == 'y' and cd95 == 'y' and cd90 == 'y' and cd85 == 'y' and cd80 != 'y':
        f.write(id + '\n')
        cd80 = ' '
    print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(id, len, cd98, cd95, cd90, cd85, cd80)
