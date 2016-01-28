import sys
import numpy as np

lenfile = sys.argv[1]
len_list = []
with open(lenfile,'rb') as f1:
    for l1 in f1:
        l1_split = l1.split('\t')
        len_list.append(int(l1_split[1].strip('\n')))

print np.std(len_list,ddof=1)
