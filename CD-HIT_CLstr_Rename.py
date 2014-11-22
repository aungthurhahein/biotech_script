#-------------------------------------------------------------------------#
#!/usr/bin/env python
#To rename cluster to have trinity output format
#Usage
# $ cd_hit_clstr_stat.py xxx.clstr
#Dev: Aung
#-------------------------------------------------------------------------#
import argparse
import os, os.path
import sys
import math
import operator
import re
from Bio import SeqIO

def ParseCommandLine():
    parser = argparse.ArgumentParser('parse cd-hit cluster file and rename the output like Trinity fasta file')
    parser.add_argument('-i', '--input', type= ValidateFileRead,required=True,help="input cluster file from cd-hit")
    theArgs = parser.parse_args()
    return theArgs

def ValidateFileRead(theFile):
    # Validate the path is a valid
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')

    # Validate the path is readable
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')


def main(input):

    #check input file
    try:
        inputfile=open(input,"rb")
    except:
        p.Print ("file not given...")
        exit(0)

    C=0
    for line in inputfile:
        if ">Cluster" in line:
            I=1
            C= C+1
            print ('Cluster %s' %C)
        else:
            startmatch= re.search("(>.*)",line)
            if startmatch:
                header = startmatch.group(1)
                # remove dots
                header = re.sub('\.\.+', ' ', header)
                # remove after space
                headerid= header.split(" ")[0]

                # print headerid, ">C{0}-g1-i{1}".format(C,I)

             # read sequence file and print the corresponding sequence
            for seq_record in SeqIO.parse("test.fasta", "fasta"):
                if seq_record.id == headerid:
                    print ">C{0}-g1-i{1}".format(C,I)
                    print(repr(seq_record.seq))
            I= I+1

if __name__ == "__main__":
    args = ParseCommandLine()
    main(args.input)
