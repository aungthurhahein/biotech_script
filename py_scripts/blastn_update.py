__author__ = 'Aung'

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
cur.execute('select blastn.id,blastn.description from %s left join blastn on'
            ' %s.transcript_id = blastn.id where blastn.id is not null' % (updatetable, updatetable))
for row in cur.fetchall():
    common.append(row)
cur.close
db.close

if len(common) <= 0:
    print "No records"
else:
    for x in common:
        update_id = "'{0}'".format(x[0].strip())
        temp1 = re.sub('[\']', '', x[1].strip())
        if len(temp1) > 750:
            temp1 = temp1[0:750]
        update_info = "'{0}'".format(temp1)
        print update_id
        db4 = MySQLdb.connect(host="127.0.0.1",
                              user="root",
                              passwd="",
                              db=database,
                              unix_socket="/opt/lampp/var/mysql/mysql.sock")
        cur4 = db4.cursor()
        cur4.execute('update %s Set BLASTN = %s where transcript_id= %s' % (updatetable, update_info, update_id))
        db4.commit()
        cur4.close
        db4.close