#! /usr/bin/env/ python
__author__ = 'aung'
"""
# To combine trinity with other assembly output(MIRA,CAP3,CDHIT)
# usage:
# output: 
# Dev: Aung
# Date: 18032015
"""
import argparse
from Bio import SeqIO


def parse_command_line():
    parser = argparse.ArgumentParser('To combine trinity output with MIRA/CAP3/CDHIT output into a single output')
    parser.add_argument('-s', '--sequence', nargs='+', required=True,
                        help="assembly output sequence file(s) Trinity")
    parser.add_argument('-a', '--assemblyid', type=str, required=True,
                        help="Assembly ID for ID mapping table (id1,id2..)")
    parser.add_argument('-i', '--astranid', type=str, required=True,
                        help="AsTran ID for ID mapping table (assemblyid_platform_species_date)")
    theArgs = parser.parse_args()
    return theArgs


def main(sequence,assemblyid, astranid):
    assemblyid_split = assemblyid.split(',')
    astran_count = 0
    no_of_files = len(sequence)
    print "Input files:" + str(no_of_files)

    f1 = open(sequence[0] + "_id_map.txt", 'w')
    f2 = open(sequence[0] + "_trinity_fmt.fasta", 'w')
    # first file read
    for seq_record in SeqIO.parse(sequence[0], "fasta"):
        new_custom_id = "{0}_{1}".format(astranid, str(astran_count).zfill(5))
        trinity_id = ">" + seq_record.description
        clstr_trinity = trinity_id + "\t" + seq_record.id + "\t" + new_custom_id + "\t" + assemblyid_split[0] + "\n"
        f1.write(clstr_trinity)
        astran_count += 1
        f2.write(trinity_id + '\n')
        f2.write(str(seq_record.seq) + '\n')
    f1.close
    f2.close

    # from second file to last
    for x, f in enumerate(sequence[1:]):
        f1 = open(f + "_id_map.txt", 'w')
        f2 = open(f + "_trinity_fmt.fasta", 'w')
        for seq_record in SeqIO.parse(f, "fasta"):
            trinity_id = ">c{0}_g1_i1 len={1}".format(astran_count, len(seq_record.seq))
            new_custom_id = "{0}_{1}".format(astranid, str(astran_count).zfill(5))
            clstr_trinity = trinity_id + "\t" + seq_record.id + "\t" + new_custom_id + "\t" + assemblyid_split[x+1] + "\n"
            f1.write(clstr_trinity)
            astran_count += 1
            f2.write(trinity_id + '\n')
            f2.write(str(seq_record.seq) + '\n')
        f1.close
        f2.close

if __name__ == "__main__":
    args = parse_command_line()
    main(args.sequence, args.assemblyid, args.astranid)

