#!/usr/bin/env python
"""
# To rename cdhit cluster to have trinity output format
# Usage
# $ cd_hit_to_trinity.py -s cdhit_out.fasta cdhit_out2.fasta -a assembly_ID -i AsTranID
# Output: output files are splitted according to input files but already concatenated technically
# Dev: Aung ေအာင်သူရဟိန်း
# Date: 17032015
"""
import argparse
import os
import os.path
from Bio import SeqIO

def parse_command_line():
    parser = argparse.ArgumentParser('parse cd-hit fasta files and rename the output to Trinity.fasta format file')
    parser.add_argument('-s', '--sequence', nargs='+', required=True,
                        help="cd-hit output related sequence file(s)")
    parser.add_argument('-a', '--assemblyid', type=str, required=True,
                        help="Assembly ID for ID mapping table (id1,id2)")
    parser.add_argument('-i', '--astranid', type=str, required=True,
                        help="AsTran ID for ID mapping table (assemblyid_platform_species_date)")
    theArgs = parser.parse_args()
    return theArgs


def validate_file_read(thefile):
    # Validate the path is a valid
    if not os.path.exists(thefile):
        raise argparse.ArgumentTypeError('File does not exist')

    # Validate the path is readable
    if os.access(thefile, os.R_OK):
        return thefile
    else:
        raise argparse.ArgumentTypeError('File is not readable')


def main(sequence, assemblyid, astranid):
    assemblyid_split = assemblyid.split(',')
    astran_count = 0
    for x, f in enumerate(sequence):
        f1 = open(f + "_clstrtrinitymap.txt", 'w')
        f2 = open(f + "_trinity_fmt.fasta", 'w')
        for seq_record in SeqIO.parse(f, "fasta"):
            trinity_id = ">c{0}_g1_i1 len={1}".format(astran_count, len(seq_record.seq))
            new_custom_id = "{0}_{1}".format(astranid, str(astran_count).zfill(5))
            clstr_trinity = trinity_id + "\t" + seq_record.id + "\t" + new_custom_id + "\t" + assemblyid_split[x] + "\n"
            f1.write(clstr_trinity)
            astran_count += 1
            f2.write(trinity_id+'\n')
            f2.write(str(seq_record.seq)+'\n')
            print trinity_id
    f1.close
    f2.close

if __name__ == "__main__":
    args = parse_command_line()
    main(args.sequence, args.assemblyid, args.astranid)
