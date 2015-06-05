#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import sys
import xml.dom.minidom
import re
from xml.dom import minidom

xml = sys.argv[1]
openxml = open(xml, 'r')

# xmldoc = minidom.parse(xml)
# print xmldoc.childNodes[1].toxml()
# xmlTag = xmldoc.getElementsByTagName('Id')
# runs = xmldoc.getElementsByTagName('Item')

for e, x in enumerate(openxml):
    print x
    # sys.stdout.write(x.toxml().replace('<Run>','').replace('</Run>',''))
    temp = x.replace('<Item Name="Runs" Type="String">&lt;Run acc=&quot;', '')
    temp_I1 = re.match(r'SRR*[\w+\s+]*', temp)
    print temp_I1.group()
    # sys.stdout.write(temp_I1)
    # sys.stdout.write('\n')
