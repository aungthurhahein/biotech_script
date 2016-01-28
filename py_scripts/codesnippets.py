# ---------------------------------------------------------#
__author__ = 'Aung'
# ---------------------------------------------------------#
# import MySQLdb

"""
# file read/write
"""
# read file by line and return each lines as a list item
def file_read_line(fileinput):
    file_list = []
    with open(fileinput,'rb') as f1:
        for line in f1:
            file_list.append(line.strip('\n'))
    return file_list


# write list to files
def write_file(writelist, filename):
    f1 = open(filename, 'w')
    for x in writelist:
        f1.write(x + "\n")
    print filename + " written"


# split csv file from file and return each lines as a list item
def csv_split(csv_list):
    csv_splitlist = []
    for line in csv_list:
        line_split = line.split(',')
        csv_splitlist.append(line_split)
    return csv_splitlist


# split tsv file
def tsv_split(tsv_list):
    tsv_splitlist = []
    for line in tsv_list:
        line_split = line.split('\t')
        tsv_splitlist.append(line_split)
    return tsv_splitlist


"""
# counting
"""
# count occurences of a string from list
def count_occurence(list, string):
    count = 0
    for item in list:
        if string.strip() in list:
            count += 1
    return count


# get the first index of a string from list
def get_index(list, string):
    if string in list:
        return list.index(string.strip())


"""
# sorting
"""


def sorted_list(list):
    return sorted(list)


# """
# #  mysql functions for local connection
# """
# # create table
# def create_table(dbname, querystring):
#     db = MySQLdb.connect(host="127.0.0.1",
#                          user="root",
#                          passwd="",
#                          db=dbname,
#                          unix_socket="/opt/lampp/var/mysql/mysql.sock")
#     cur = db.open
#     cur.execute(querystring)
#     cur.close
#     db.close
#
#
# #  select all columns form a specific table
# def select_table(dbname, tablename):
#     db = MySQLdb.connect(host="127.0.0.1",
#                          user="root",
#                          passwd="",
#                          db=dbname,
#                          unix_socket="/opt/lampp/var/mysql/mysql.sock")
#     cur = db.open
#     cur.execute("Select * from %s" % tablename)
#     cur.close
#     db.close
#
#
# def insert_table(dbname, tablename, list, query):
#     for i in list:
#         db = MySQLdb.connect(host="127.0.0.1",
#                              user="root",
#                              passwd="",
#                              db=dbname,
#                              unix_socket="/opt/lampp/var/mysql/mysql.sock")
#         cur = db.open
#         # cur.execute(query, % )
#         cur.close
#         db.close
#
