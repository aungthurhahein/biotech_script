__author__ = 'Aung'

import sys
import re

targetfile = sys.argv[1]
fileopen = open(targetfile, 'r')
file_list = []

put_file = open(targetfile+"_putative", 'w')
predicted_file = open(targetfile+"_predicted", 'w')
uncharacterized_file = open(targetfile+"_uncharacterized", 'w')
# unknown_file = open(targetfile+"_unknown", 'w')
other_file = open(targetfile+"_known", 'w')

for line in fileopen:
    file_list.append(line)

def update_record(record,keyword):
    rec = record.strip()
    rec += "\t" + keyword + "\n"
    new_file.write(rec)

for record in file_list:
    record_split = record.split('\t')
    definition = record_split[7].strip().lower()

    put_id = re.search(r'[\w+\s+]*putative uncharacterized protein[\w+\s+]*', definition)
    pred_id = re.search(r'[\w+\s+]*predicted protein[\w+\s+]*', definition)
    unchar_id = re.search(r'[\w+\s+]*uncharacterized protein[\w+\s+]*', definition)
    # unknown1 = re.search(r'^aael[\d+]*', definition)
    # unknown2 = re.search(r'^acyp[\d+]*', definition)
    # unknown3 = re.search(r'^agap[\d+]*', definition)
    # unknown4 = re.search(r'^cg\d', definition)
    # unknown5 = re.search(r'^gd\d', definition)
    # unknown6 = re.search(r'^gg\d', definition)
    # unknown7 = re.search(r'^gh\d', definition)
    # unknown8 = re.search(r'^gk\d', definition)
    # unknown9 = re.search(r'^gl\d', definition)


    if put_id and record_split[8] == "-" and record_split[9].strip('\n') == "-":
        put_file.write(record)
    elif pred_id and record_split[8] == "-" and record_split[9].strip('\n') == "-":
        predicted_file.write(record)
    elif unchar_id and record_split[8] == "-" and record_split[9].strip('\n') == "-":
        uncharacterized_file.write(record)
    # elif unknown1 or unknown2 or unknown3 or unknown4 or unknown5 or unknown6 or unknown7 or unknown8 or unknown9:
    #     unknown_file.write(record)
    else:
        other_file.write(record)
