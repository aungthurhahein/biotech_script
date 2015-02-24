__author__ = 'atrx'

import MySQLdb
import sys
import re

updatetable = sys.argv[1]  # E3 E1
datatable = sys.argv[2]
database = "Mapping"
common = [];

db = MySQLdb.connect(host="127.0.0.1",
                     user="root",
                     passwd="",
                     db=database,
                     unix_socket="/opt/lampp/var/mysql/mysql.sock")
# db cursor
cur = db.cursor()
# read table with queries
# get common id
cur.execute(
    'select DISTINCT %s.transcript_id from  %s left join %s on %s.transcript_id = %s.transcript_id where %s.ID is not null' % (
    datatable, datatable, updatetable, updatetable, datatable, updatetable ))
for row in cur.fetchall():
    common.append(row)
cur.close
db.close
#---------------------------------------------------#

def get_data(table, id):
    data_list = []
    db2 = MySQLdb.connect(host="127.0.0.1",
                          user="root",
                          passwd="",
                          db=database,
                          unix_socket="/opt/lampp/var/mysql/mysql.sock")
    cur2 = db2.cursor()
    cur2.execute(
        'select gene_id, Transcript_id, sprot_Top_BLASTX_hit, TrEMBL_Top_BLASTX_hit, RNAMMER, prot_id, prot_coords, sprot_Top_BLASTP_hit, TrEMBL_Top_BLASTP_hit, Pfam, SignalP, TmHMM, eggnog, gene_ontology_blast, gene_ontology_pfam, transcript, peptide from %s where transcript_id = %s' % (
        table, id ))

    for row in cur2.fetchall():
        data_list.append(row)
    cur2.close
    db2.close
    return data_list


def get_status(id):
    data_list = []
    db3 = MySQLdb.connect(host="127.0.0.1",
                          user="root",
                          passwd="",
                          db=database,
                          unix_socket="/opt/lampp/var/mysql/mysql.sock")
    cur3 = db3.cursor()
    cur3.execute('select blastx_source,blastp_source from %s where transcript_id= %s' % (datatable, id))
    for row in cur3.fetchall():
        data_list.append(row)
    cur3.close
    db3.close
    return data_list

#main
if len(common) <= 0:
    print "No common records"
    exit(0)
else:
    for id in common:
        #get data from update table
        idformat = "'{0}'".format(id[0])
        updatedata = get_data(updatetable, idformat)
        #get data from datatable
        data_exist = get_data(datatable, idformat)

        for x in range(0, len(data_exist)):
            final_update = []
            for i in range(0, len(data_exist[x])):
                if data_exist[x][i] == '.':
                    temp1 = re.sub('[\']', '', updatedata[0][i])
                    final_update.append("'{0}'".format(temp1))
                else:
                    temp2 = re.sub('[\']', '', data_exist[x][i])
                    final_update.append("'{0}'".format(temp2))

            if (data_exist[x][2].strip() == '.') and (updatedata[0][2].strip() != '.'):
                blastx_source = "'{0}'".format(updatetable)
            else:
                blastx_existing_id = get_status(idformat)
                if blastx_existing_id[0][0] == "E5":
                    blastx_source = "'E5'"
                else:
                    blastx_source = "'{0}'".format(blastx_existing_id[0][0])

            if (data_exist[x][7].strip() == '.') and (updatedata[0][7].strip() != '.'):
                blastp_source = "'{0}'".format(updatetable)
            else:
                blastp_existing_id = get_status(idformat)
                if blastp_existing_id[0][1] == "E5":
                    blastp_source = "'E5'"
                else:
                    blastp_source = "'{0}'".format(blastp_existing_id[0][1])

            #update datatable
            db4 = MySQLdb.connect(host="127.0.0.1",
                                  user="root",
                                  passwd="",
                                  db=database,
                                  unix_socket="/opt/lampp/var/mysql/mysql.sock")

            cur4 = db4.cursor()
            cur4.execute(
                'update %s Set gene_id = %s,Transcript_id= %s,sprot_Top_BLASTX_hit= %s,TrEMBL_Top_BLASTX_hit= %s,RNAMMER= %s,prot_id= %s,prot_coords= %s,sprot_Top_BLASTP_hit= %s,TrEMBL_Top_BLASTP_hit= %s,Pfam= %s,SignalP= %s,TmHMM= %s,eggnog= %s,gene_ontology_blast= %s,gene_ontology_pfam= %s,transcript= %s,peptide= %s,Blastx_source=%s,Blastp_source=%s where transcript_id= %s'
                % (datatable, final_update[0], final_update[1], final_update[2], final_update[3], final_update[4],
                   final_update[5], final_update[6], final_update[7],
                   final_update[8], final_update[9], final_update[10], final_update[11], final_update[12],
                   final_update[13], final_update[14], final_update[15], final_update[16], blastx_source, blastp_source,
                   idformat))
            db4.commit()
            cur4.close
            db4.close

            # print "record updated"
