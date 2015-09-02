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
addedto_seqDB = open("addedto_PVAung_NotFound.txt", 'w')
pm_updated = open("PVAungFoundupdated.txt", 'w')


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
        'update LV2_Org Set SeqID = %s where SeqID = %s' % (updateid, existingid))
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
cur.execute('select * from LV2_Org')
finalid = 333076
for row in cur.fetchall():
    id_split = row[0].split('|')
    # not found
    if loop_query("'{0}'".format(row[1].strip())) is None:
        newid = str(finalid+1)
        finalid += 1
        addedto_seqDB.write(newid+"|"+row[0]+'\n')
        notfound_update("'{0}'".format(newid), "'{0}'".format(row[1].strip()))  # id Sequence
        print "Not Found:" + row[0] + "   " + newid

        # update file with newid
        Updateddid = newid + '|' + id_split[0] + '|' + id_split[1]
        found_update("'{0}'".format(Updateddid.strip()), "'{0}'".format(row[0].strip()))

    # found
    else:
        oldupdatedID = loop_query("'{0}'".format(row[1].strip()))
        Updateddid = oldupdatedID[0]+'|'+id_split[0]+'|'+id_split[1]
        print "found " + row[0] + " oldid " + oldupdatedID[0]
        pm_updated.write(row[0] + '\t' + oldupdatedID[0] + '\n')  # newid #oldid
        found_update("'{0}'".format(Updateddid.strip()), "'{0}'".format(row[0].strip()))

