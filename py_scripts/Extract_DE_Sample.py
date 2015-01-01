#-------------------------------------------------------------------------#
#!/usr/bin/env python
#To extract DE sample by expression levels and sample specific
#Usage
# $ python Extract_DE_Sample.py table1 table2 db
#Dev: Aung
#Time:17/10/2014
#-------------------------------------------------------------------------#
import MySQLdb
import sys

# table1 = 'G000001'
# table2 = 'G0000001'

table1 = sys.argv[1]
table2 = sys.argv[2]
database = sys.argv[3]
mainquery=[]
mainquery_C=[]
mainquery_M=[]
mainquery_S=[]
CM=[]
CS=[]
MS=[]
SM=[]
MC=[]
SC=[]
C=[]
M=[]
S=[]
MS2=[]

#DE comparision function
def loop_query(t1,t2,query,list):
    db2 = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                      passwd="",
                      db=database,
                      unix_socket="/opt/lampp/var/mysql/mysql.sock")

    cur2 = db2.cursor()
    cur2.execute(query % (table1,table1,table2,table1,table2,table2,table1,table1))

    for row in cur2.fetchall():
        for col in row:
           list.append(col)
    cur2.close
    db2.close

#sample specific function
def Specific_loop_query(t1,t2,query,list):
    db3 = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                      passwd="",
                      db=database,
                      unix_socket="/opt/lampp/var/mysql/mysql.sock")
    cur3 = db3.cursor()
    cur3.execute(query % (table1,table1,table2,table1,table2,table2,table1,table1,table1))
    for row in cur3.fetchall():
        for col in row:
            list.append(col)
    cur3.close
    db3.close

#main query
#-----------------------------------------#
#db con
db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                      passwd="",
                      db=database,
                      unix_socket="/opt/lampp/var/mysql/mysql.sock")
#db cursor
cur = db.cursor()
# read table with queries
cur.execute('SELECT %s.Feature,%s.C,%s.M,%s.S FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null' % (table1,table1,table1,table1,table1,table2,table1,table2,table2))

# put into list
for row in cur.fetchall() :
        mainquery.append(row[0])
        mainquery_C.append(row[1])
        mainquery_M.append(row[2])
        mainquery_S.append(row[3])
cur.close
db.close
#-----------------------------------------#
#CM
CM_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C > %s.M'
loop_query(table1,table2,CM_q,CM)
#CS
CS_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C > %s.S'
loop_query(table1,table2,CS_q,CS)
#MC
MC_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.M > %s.C'
loop_query(table1,table2,MC_q,MC)
#SC
SC_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.S > %s.C'
loop_query(table1,table2,MC_q,SC)
#SM
SM_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.S > %s.M'
loop_query(table1,table2,SM_q,SM)
#MS
MS_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.M > %s.S'
loop_query(table1,table2,MS_q,MS)

#C_Spec
C_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C > 0 and %s.M = 0 and %s.S = 0'
M_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C = 0 and %s.M > 0 and %s.S = 0'
S_q = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C = 0 and %s.M = 0 and %s.S > 0'
MS_q2 = 'SELECT %s.Feature FROM %s left join %s ON %s.Feature = %s.Feature where %s.Feature is null and %s.C = 0 and (%s.M > 0 or %s.S > 0)'
Specific_loop_query(table1,table2,C_q,C)
Specific_loop_query(table1,table2,M_q,M)
Specific_loop_query(table1,table2,S_q,S)
Specific_loop_query(table1,table2,MS_q2,MS2)

# loop all query and find match with others
# and print out with tabular form
print "ID\tC\tM\tS\tCM\tCS\tMC\tMS\tSC\tSM\tC\tM\tS\tMS"
count=0
for i in mainquery:
    print i,
    print "\t",
    print mainquery_C[count],
    print "\t",
    print mainquery_M[count],
    print "\t",
    print mainquery_S[count],
    print "\t",
    count = count+1
    if i in CM:
        print 1,
    print "\t",
    if i in CS:
        print 1,
    print "\t",
    if i in MC:
        print 1,
    print "\t",
    if i in MS:
        print 1,
    print "\t",
    if i in SC:
        print 1,
    print "\t",
    if i in SM:
        print 1,
    print "\t",
    if i in C:
        print 1,
    print "\t",
    if i in M:
        print 1,
    print "\t",
    if i in S:
        print 1,
    print "\t",
    if i in MS2:
        print 1,
    print "\t"
