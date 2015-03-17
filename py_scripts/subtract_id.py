__author__ = 'Aung ေအာင်သူရဟိန်း'

import sys
import codesnippets

annotfile = sys.argv[1]
idlist = sys.argv[2]
annotfile_read = open(annotfile, 'r')
idlist_read = open(idlist, 'r')
id_list = []
annot_list = []

annot_list = codesnippets.file_read_line(annotfile_read)
id_list = codesnippets.file_read_line(idlist_read)

for x in annot_list:
    x_split = x.split('\t')
    # print x_split[0].strip()
    if x_split[0].strip() not in id_list:
        print x
