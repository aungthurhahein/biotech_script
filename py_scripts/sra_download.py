#! /usr/bin/env/ python
"""
# download sra files from NCBI
# usage: sra_download.py sra_run_list.txt
# output: downloaded sra file is written to working DIR with verbose output
# Dev: __author__ = 'aung' 
# Date: 03062015
"""
# wget might not be in your system; try pip install wget
import wget
import sys
import os

sra_list = sys.argv[1]
open_sra = open(sra_list, 'r')

for x in open_sra:
    base = "ftp://ftp-trace.ncbi.nih.gov"
    first3 = x[0:3].strip()
    first6 = x[0:6].strip()
    sra_run = x.strip().strip('\n')
    sra_file = sra_run+".sra"
    # check for existence of same file
    if os.path.isfile(sra_file) is False:
        url = base+"/sra/sra-instant/reads/ByRun/sra/"+first3+"/"+first6+"/"+sra_run+"/"+sra_file
        print "#-----------------------------------#"
        print url
        filename = wget.download(url)
        print sra_file + " downloaded..."
        print "#-----------------------------------#"
    else:
        print "#-----------------------------------#"
        print sra_file + " is already downloaded!!!"
        print "#-----------------------------------#"