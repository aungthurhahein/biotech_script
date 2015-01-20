#! /usr/bin/env python
#--------------------------------------------------------------------------#
# mapp annotataion text file with sample specific text file
# Date: 9012015
# Usage: annotataion_map.py
# __author__ = 'atrx'
#--------------------------------------------------------------------------#

import sys
import re
usage= "Usage %s infile" % sys.argv[0] #specific massage for no input

try:
    infile = sys.argv[1]
    matchfile = sys.argv[2]
except:
    print usage, sys.exit(1)

def rewind(f):
    f.seek(0)

#open file read
matchfile = open(matchfile,'r')
print "ID\tC\tM\tS\tCM\tCS\tMC\tMS\tSC\tSM\tC\tM\tS\tMS\tgene-id\tTranscript-id\tsprot-Top-BLASTX-hit\tTrEMBL-Top-BLASTX-hit\tRNAMMER\tprot-id\tprot-coords\tsprot-Top-BLASTP-hit\tTrEMBL-Top-BLASTP-hit\tPfam\tSignalP\tTmHMM\teggnog\tgene-ontology-blast\tgene-ontology-pfam\ttranscript\tpeptide"
for line in matchfile:
    yvalue = line.split()
    file_split = re.split(r'\t+', line)
    file_id = str(file_split[0])
    ifile = open(infile,'r')
    for annot in ifile:
        i_split = re.split(r'\t+', annot)
        annot_id = str(i_split[1])
        if file_id.strip() == annot_id.strip():
            print line.strip('\n'),
            for item in i_split:
                if len(item) > 750:
                    print "{0}\t".format(item[0:750].strip()),
                else:
                    print "{0}\t".format(item.strip()),
            print "\n"
    else:
        ifile.close()
    if len(yvalue) == 0: continue #skipping blank lines

matchfile.close()
ifile.close()
