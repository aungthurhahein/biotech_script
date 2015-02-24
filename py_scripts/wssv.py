__author__ = 'aung'

import MySQLdb
import sys
import re

database = "Mapping"
updatetable = sys.argv[1]
common = []

db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     passwd="",
                     db=database,
                     unix_socket="/opt/lampp/var/mysql/mysql.sock")
# db cursor
cur = db.cursor()
cur.execute(
    'select wssv.id from %s left join wssv on %s.transcript_id = wssv.id where wssv.id is not null and wssv.wssv= 1' % (
    updatetable, updatetable))
for row in cur.fetchall():
    common.append(row)
cur.close
db.close
print len(common)
if len(common) <= 0:
    print "No records"
else:
    for x in common:
        update_id = "'{0}'".format(x[0].strip())
        print x, update_id
        db4 = MySQLdb.connect(host="127.0.0.1",
                              user="root",
                              passwd="",
                              db=database,
                              unix_socket="/opt/lampp/var/mysql/mysql.sock")
        cur4 = db4.cursor()
        cur4.execute('update %s Set wssv = %s where transcript_id= %s' % (updatetable, '1', update_id))
        db4.commit()
        cur4.close
        db4.close