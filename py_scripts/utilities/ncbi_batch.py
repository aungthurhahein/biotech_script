# !/usr/bin/python
"""
# Download Contents from NCBI database
# usage: ncbi_batch.py --help
# output: esummary.xml, sequence.fasta/gb and stdout
# Dev: __author__ = 'aung'
# Date: 22052015
"""
import argparse
import urllib
import urllib2
import re
# TODO:: xml parsing

def parse_command_line():
    parser = argparse.ArgumentParser('Download Contents from NCBI database')
    parser.add_argument('-db', '--db', help="database")
    parser.add_argument('-term', '--term', help="Entrez text query")
    parser.add_argument('-datetype', '--datetype', help="Type of date used to limit a search;'mdat', 'pdat' & 'edat'")
    parser.add_argument('-reldate', '--reldate',
                        help="an integer n, the search returns by datetype within the last n days")
    parser.add_argument('-mindate', '--mindate', help="Minimum date: yyyy/mm/dd")
    parser.add_argument('-maxdate', '--maxdate', help="Maximum date: yyyy/mm/dd")
    parser.add_argument('-rettype', '--rettype', help="Return Data type: fasta, gb, est ...")
    args_pass = parser.parse_args()
    return args_pass


def write_file(writelist, filename):
    f1 = open(filename, 'w')
    for x in writelist:
        f1.write(x)
    print filename + " written"

def main(db, term, datetype, reldate, mindate, maxdate, rettype):
    # 1. data preparation esearch
    output = "NO_DATA"
    base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    url = base + "esearch.fcgi"
    esearch_query = "?"
    values = {}

    if db:
        values['db'] = db
        esearch_query += "db=" + db + "&"
    if term:
        values['term'] = term
        esearch_query += "term=" + re.sub(" ", "+", term.strip()) + "&"
    if datetype:
        values['datetype'] = datetype
        esearch_query += "datetype=" + datetype + "&"
    if reldate:
        values['reldate'] = reldate
        esearch_query += "reldate=" + reldate + "&"
    if mindate:
        values['mindate'] = mindate
        esearch_query += "mindate=" + mindate + "&"
    if maxdate:
        values['maxdate'] = maxdate
        esearch_query += "maxdate=" + maxdate + "&"
    esearch_query += "usehistory=y&"  # enable user history recording
    esearch_query += "retmax=100000"  # max UIDs to 100000
    values['usehistory'] = 'y'
    values['retmax'] = '100000'
    print "Query string: " + url + esearch_query

    # esearch
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    # 2. get data with efetch
    query_key = ""
    web_env = ""
    record_count = ""

    if rettype:
        rettype_val = rettype
    else:
        rettype_val = 'gb'  # gbank as default returntype

    head_trig = 0
    for line in response.readlines():
        line = line.strip()
        if re.search("<WebEnv>(.*)</WebEnv>", line):
            web_env = re.search("<WebEnv>(.*)</WebEnv>", line).groups()[0]

        if re.search("<QueryKey>(.*)</QueryKey>", line):
            query_key = re.search("<QueryKey>(.*)</QueryKey>", line).groups()[0]
        if re.search(r'[\w+\s+]*<eSearchResult>[\w+\s+]*', line):
            head_trig = 1
        if head_trig == 1:
            if re.search("<Count>(.*)</Count>", line):
                record_count = re.search("<Count>(.*)</Count>", line).groups()[0]
                head_trig = 0
    if query_key != "" and web_env != "" and record_count != "":
        # report summary of download data
        e_sumurl = base + "esummary.fcgi"
        esum_val = {
            'db': db,
            'query_key': query_key,
            'WebEnv': web_env
        }
        esum_data = urllib.urlencode(esum_val)
        esum_req = urllib2.Request(e_sumurl, esum_data)
        print e_sumurl+ "?+" + esum_data
        esum_response = urllib2.urlopen(esum_req)
        write_file(esum_response.read(), re.sub(" ", "_", term.strip()) + "_summary.xml")

        # efetch
        url = base + "efetch.fcgi"
        print "QueryKey: " + query_key
        print "Web Enviroment: " + web_env
        print "Result Count: " + record_count

        # for records <= 10000, download in 1 batch
        if int(record_count) <= 1000000:
            print "downloading sequences..."
            values = {
                'db': db,
                'query_key': query_key,
                'WebEnv': web_env,
                'rettype': rettype_val,
                'retmode': 'text'
            }
            # post the efetch URL
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            output = response.readlines()
            write_file(output, re.sub(" ", "_", term.strip()) + "_records.gb")  # write to gbank file
            exit(1)
        else:
            # times = int(int(record_count)/10000)
            restart = 0
            retmax= 100000
            while restart < int(record_count):
                print "downloading" + str(retmax) + " sequence of " + str(record_count) + " sequences"
                values_max = {
                    'db': db,
                    'query_key': query_key,
                    'WebEnv': web_env,
                    'restart': restart,
                    'retmax': retmax,
                    'rettype': rettype_val,
                    'retmode': 'text'
                }
                restart += retmax
                # post the efetch URL
                data = urllib.urlencode(values_max)
                req = urllib2.Request(url, data)
                response = urllib2.urlopen(req)
                output = response.readlines()
                write_file(output,
                           re.sub(" ", "_", term.strip()) + "_records.gb_" + str(restart))  # write to gbank file
            exit(1)
    print "_"*20


if __name__ == "__main__":
    args = parse_command_line()
    main(args.db, args.term, args.datetype, args.reldate, args.mindate, args.maxdate, args.rettype)
