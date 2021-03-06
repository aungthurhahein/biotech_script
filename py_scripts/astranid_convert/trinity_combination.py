#! /usr/bin/env/ python
__author__ = 'aung'
"""
# To combine serveral trinity outputs into one.
# usage:
# output: 
# Dev: Aung
# Date: 18032015
"""
import argparse
from Bio import SeqIO

def parse_command_line():
    parser = argparse.ArgumentParser('To combine several trinity output into a single output')
    parser.add_argument('-s', '--sequence', nargs='+', required=True,
                        help="trinity output sequence file(s)")
    parser.add_argument('-a', '--assemblyid', type=str, required=True,
                        help="Assembly ID for ID mapping table (id1,id2..)")
    parser.add_argument('-i', '--astranid', type=str, required=True,
                        help="AsTran ID for ID mapping table (id1,id2..)")
    theArgs = parser.parse_args()
    return theArgs


def validate_astranid(str_obj, assemblyid):
    str_obj_split = str_obj.split(',')
    assemblyid_split = assemblyid.split(',')
    for x, astran_id in enumerate(str_obj_split):
        astran_split = astran_id.split('_')
        if len(astran_split) == 1:
            print "Invalid astronid! please check astraid format(taxon_assemblyid)"
            exit(1)
        if assemblyid_split[x].strip() == astran_split[1].strip():
            continue
        else:
            print "Assembly_ID should be part of AstranID. Check inputs again."
            exit(0)

def main(sequence, assemblyid, astranid):
    validate_astranid(astranid, assemblyid)
    assemblyid_split = assemblyid.split(',')
    astranid_split = astranid.split(',')
    no_of_files = len(sequence)
    print "Input files:" + str(no_of_files)
    f1 = open(sequence[0] + astranid + "_id_map.txt", 'w')
    f2 = open(sequence[0] + astranid + "_trinity_fmt.fasta", 'w')

    astran_count = 0
    # first file read
    for seq_record in SeqIO.parse(sequence[0], "fasta"):
        new_custom_id = "{0}_{1}".format(astranid_split[0], str(astran_count).zfill(5))
        trinity_id = ">" + seq_record.description
        clstr_trinity = trinity_id + "\t" + seq_record.id + "\t" + new_custom_id + "\t" + assemblyid_split[0] + "\n"
        f1.write(clstr_trinity)
        astran_count += 1
        f2.write(trinity_id + '\n')
        f2.write(str(seq_record.seq) + '\n')

    # get next cluster id
    last_trinity_id = trinity_id.split()[0].split('_')[0].split('>')[1].split('c')[1]
    next_id = int(last_trinity_id)+1

    # from second file to last
    for x, f in enumerate(sequence[1:]):
        astran_count = 0
        for seq_record in SeqIO.parse(f, "fasta"):
            new_custom_id = "{0}_{1}".format(astranid_split[x+1], str(astran_count).zfill(5))
            trinity_split = seq_record.id.split('_')
            desc = seq_record.description.split()
            trinity_id = ">c{0}_{1}_{2} len={3}".format(next_id, trinity_split[1], trinity_split[2], desc[1]+" "+desc[2])
            clstr_trinity = trinity_id + "\t" + seq_record.id + "\t" + new_custom_id + "\t" + assemblyid_split[x+1] + "\n"
            f1.write(clstr_trinity)
            astran_count += 1
            next_id += 1
            f2.write(trinity_id + '\n')
            f2.write(str(seq_record.seq) + '\n')
    f1.close
    f2.close

if __name__ == "__main__":
    args = parse_command_line()
    main(args.sequence, args.assemblyid, args.astranid)
