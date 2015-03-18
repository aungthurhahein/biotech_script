#!/usr/bin/env python
"""
# To rename assembly(MIRA,CAP3,CDHIT) output to Trinity.fasta format(c#_g#_i#)
# Usage
# $ assembly_to_trinity.py -s assembly_out.fasta assembly_out2.fasta -a assembly_ID -i AsTranID
# Output: output files are splitted according to input files but already concatenated technically
# Dev: Aung
# Date: 17032015
"""

import argparse
from Bio import SeqIO

def parse_command_line():
    parser = argparse.ArgumentParser('parse assembly fasta files and '
                                     'rename the sequence header to Trinity.fasta format file')
    parser.add_argument('-s', '--sequence', nargs='+', required=True,
                        help="assembly output sequence file(s)")
    parser.add_argument('-a', '--assemblyid', type=str, required=True,
                        help="Assembly ID for ID mapping table (id1,id2..)")
    parser.add_argument('-i', '--astranid', type=str, required=True,
                        help="AsTran ID for ID mapping table (assemblyid_platform_species_date)")
    theArgs = parser.parse_args()
    return theArgs

def main(sequence, assemblyid, astranid):
    assemblyid_split = assemblyid.split(',')
    astran_count = 0
    for x, f in enumerate(sequence):
        f1 = open(f + "_id_map.txt", 'w')
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
