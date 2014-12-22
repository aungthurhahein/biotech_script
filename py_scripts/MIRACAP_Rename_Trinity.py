#-------------------------------------------------------------------------#
#!/usr/bin/env python
#To rename MIRA and Trinity output to trinity.fasta format
#Usage
# $ MIRACAP_Rename_Trinity.py -s xxx.fasta -q xxx.fasta.qual
#Output: xxx.fasta_2Trinity.fasta,xxx.fasta_2Trinity.fasta.qual
#Dev: Aung
#Date: 22122014
#-------------------------------------------------------------------------#
import argparse
import os, os.path
import sys
import math
import operator
from Bio import SeqIO_
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def ParseCommandLine():
    parser = argparse.ArgumentParser('parse mira/cap3 output file to output to Trinity.fasta format file')
    parser.add_argument('-s','--sequence',type=ValidateFileRead,required=True,help="fasta seq file")
    parser.add_argument('-q', '--quality', type= ValidateFileRead,required=True,help="(.qual) quality score file")
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

def main(seq,qual):
     #check input file
    try:
        seqfile=open(seq,"rb")
    except:
        p.Print ("sequence file not given...")
        exit(0)
    try:
        qualfile=open(qual,"rb")
    except:
        p.Print ("quality file not given...")
        exit(0)

    C=0;I=0;final_records=[]
    #sequence file change
    for seq_record in SeqIO.parse(seqfile, "fasta"):
            header= "c{0}_g{1}_i1".format(C,I)
            C= C+1;I= I+1
            desc = str("len={0}".format(len(seq_record.seq)))
            record = SeqRecord(seq_record.seq,id=header,description=desc)
            final_records.append(record)
    #write to to file
    SeqIO.write(final_records, "{0}_2Trinity.fasta".format(seq), "fasta")
    A=0;B=0
    #modif the same pattern for qualfile
    qualout = open("{0}_2Trinity.fasta.qual".format(seq),"w") #
    for line in qualfile:
        if ">" in line:
            header="c{0}_g{1}_i1".format(A,B)
            A=A+1;B=B+1
            qualout.write("%s\n"% header)
        else:
            qualout.write(line)
    qualout.close()

if __name__ == "__main__":
    args = ParseCommandLine()
    main(args.sequence,args.quality)