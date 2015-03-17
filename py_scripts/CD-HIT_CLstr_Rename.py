#!/usr/bin/env python

"""
#To rename cdhit cluster to have trinity output format
#Usage
# $ cd_hit_clstr_stat.py -c xxx.clstr -s cdhit_out.fasta -a assembly_ID -i AsTranID
#Dev: Aung ေအာင်သူရဟိန်း
"""
import argparse
import os
import os.path
import re
from Bio import SeqIO


def ParseCommandLine():
    parser = argparse.ArgumentParser('parse cd-hit cluster file and rename the output to Trinity.fasta format file')
    parser.add_argument('-c', '--cluster', type=ValidateFileRead, required=True,
                        help="(.clstr)cluster file from cd-hit output")
    parser.add_argument('-s', '--sequence', type=ValidateFileRead, required=True,
                        help="cd-hit output related sequence file")
    parser.add_argument('-a', '--assemblyid', type=str, required=True,
                        help="Assembly ID for ID mapping table")
    parser.add_argument('-i', '--astranid', type=str, required=True,
                        help="AsTran ID for ID mapping table (assemblyid_platform_species_date)")
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


def main(cluster, sequence, assemblyid, astranid):
    # check input file
    try:
        inputfile = open(cluster, "rb")
    except:
        p.Print("file not given...")
        exit(0)
    f1 = open(cluster+"_clstrtrinitymap.txt", 'w')

    C = 0
    astran_count = 0

    for line in inputfile:
        if ">Cluster" in line:
            I = 0
            C += 1
        else:
            startmatch = re.search("(>.*)", line)
            if startmatch:
                header = startmatch.group(1)
                header = re.sub('\.\.+', ' ', header)  # remove dots
                headerid = header.split(" ")[0]  # remove after space
                headerid = headerid.split(">")[1]  # remove >
                # read sequence file and print the corresponding sequence
                for seq_record in SeqIO.parse(sequence, "fasta"):
                    if seq_record.id == headerid:
                        I += 1
                        astran_count += 1
                        trinity_id = ">c{0}_g1_i{1} len={2}".format(C, I, len(seq_record.seq))
                        new_custom_id = "{0}_{1}".format(astranid,str(astran_count).zfill(4))
                        clstr_trinity = trinity_id + "\t" + headerid + "\t" + new_custom_id + "\t" + assemblyid + "\n"
                        f1.write(clstr_trinity)
                        print trinity_id
                        print(seq_record.seq)
                        break
                f1.close


if __name__ == "__main__":
    args = ParseCommandLine()
    main(args.cluster, args.sequence,args.assemblyid,args.astranid)
