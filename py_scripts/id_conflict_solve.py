#! /usr/bin/env/ python

"""
# 
# usage:
# output: 
# Dev: __author__ = 'aung' 
# Date: 
"""
import MySQLdb
database = "SequenceDB"
addedto_seqDB = open("addedto_seqDB_lv.txt", 'w')
lv_updated = open("lvupdated.txt", 'w')


def loop_query(seq):
    db2 = MySQLdb.connect(host="127.0.0.1",
                          user="root",
                          passwd="",
                          db=database,
                          unix_socket="/opt/lampp/var/mysql/mysql.sock")

    cur2 = db2.cursor()
    cur2.execute('select Seq_ID from SeqDB_Org where Sequence = %s' % seq)
    for row2 in cur2.fetchall():
        return row2
    cur2.close
    db2.close


def notfound_update(updatedid, seq):
    # update datatable
    db4 = MySQLdb.connect(host="127.0.0.1",
                          user="root",
                          passwd="",
                          db=database,
                          unix_socket="/opt/lampp/var/mysql/mysql.sock")

    cur4 = db4.cursor()
    cur4.execute(
        'Insert into SeqDB_Org (Seq_ID,Sequence) Values(%s,%s)' % (updatedid, seq))
    db4.commit()
    cur4.close
    db4.close


def found_update(updateid, existingid):
    db5 = MySQLdb.connect(host="127.0.0.1",
                          user="root",
                          passwd="",
                          db=database,
                          unix_socket="/opt/lampp/var/mysql/mysql.sock")

    cur5 = db5.cursor()
    cur5.execute(
        'update LV_Org Set SeqID = %s where SeqID = %s' % (updateid, existingid))
    db5.commit()
    cur5.close
    db5.close

# db con
db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     passwd="",
                     db=database,
                     unix_socket="/opt/lampp/var/mysql/mysql.sock")
# db cursor
cur = db.cursor()

cur.execute('select * from LV_Org')
for row in cur.fetchall():
    id_split = row[0].split('|')
    # not found
    if loop_query("'{0}'".format(row[1].strip())) is None:
        addedto_seqDB.write(row[0] + '\n')
        notfound_update("'{0}'".format(id_split[0].strip()), "'{0}'".format(row[1].strip()))  # id Sequence
    # found
    else:
        oldupdatedID = loop_query("'{0}'".format(row[1].strip()))
        print "found " + row[0] + "oldid " + oldupdatedID[0]
        Updateddid = oldupdatedID[0] + '|' + id_split[1] + '|' + id_split[2] + '|'
        lv_updated.write(row[0] + '\t' + oldupdatedID[0] + '\n')  # newid #oldid
        found_update("'{0}'".format(oldupdatedID[0].strip()), "'{0}'".format(Updateddid.strip()))
