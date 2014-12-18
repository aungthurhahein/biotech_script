#-------------------------------------------------------------------------#
#!/usr/bin/env python
#To rename cluster to have trinity output format
#Usage
# $ cd_hit_clstr_stat.py -i xxx.clstr
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
    parser = argparse.ArgumentParser('parse cd-hit cluster file and rename the output to Trinity.fasta format file')
    parser.add_argument('-c', '--cluster', type= ValidateFileRead,required=True,help="(.clstr)cluster file from cd-hit output")
    parser.add_argument('-s','--sequence',type=ValidateFileRead,required=True,help="Original fasta seq file")
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


def main(cluster,sequence):

    #check input file
    try:
        inputfile=open(cluster,"rb")
    except:
        p.Print ("file not given...")
        exit(0)

    C=0
    for line in inputfile:
        if ">Cluster" in line:
            I=0
            C= C+1
            # print ('Cluster %s' %C)
        else:
            startmatch= re.search("(>.*)",line)
            if startmatch:
                I= I+1
                header = startmatch.group(1)
                # remove dots
                header = re.sub('\.\.+', ' ', header)
                # remove after space
                headerid= header.split(" ")[0]
                #remove >
                headerid= headerid.split(">")[1]
                # read sequence file and print the corresponding sequence
                for seq_record in SeqIO.parse(sequence, "fasta"):
                    if seq_record.id == headerid:
                        print ">c{0}_g1_i{1} len={2}".format(C,I,len(seq_record.seq))
                        print(seq_record.seq)
                        break;

if __name__ == "__main__":
    args = ParseCommandLine()
    main(args.cluster,args.sequence)
