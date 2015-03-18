#!/usr/bin/env python
"""
#-------------------------------------------------------------------------#
#To import tsv file to database
#Usage
# $ python tsv_importer.py dbname tablename filename
# For table creation,it is required to change the variable,createtable
#Dev: Aung
#Time:17/10/2014
#-------------------------------------------------------------------------#
"""
import MySQLdb
import sys
import codesnippets

dbname = sys.argv[1]
tablename = sys.argv[2]
filename = sys.argv[3]
createtable = "Create table %s(col1 text,col2 text)%s"
insertquery = "Insert into table1"
fileopen = open(filename, 'r')
file_list = codesnippets.tsv_split(fileopen)

# create table
codesnippets.create_table(dbname, createtable)

# insert file list into table
codesnippets.insert_table(dbname, tablename, file_list, insertquery)



