#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-02-16 16:40:13
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-02-16 17:47:21
#!/usr/bin/env python
import sys
from Bio import SeqIO

# user parameters
fastq_file = sys.argv[1]
for seq_record in SeqIO.parse(fastq_file, "fasta"):        
    ncount = seq_record.seq.lower().count('n') 
    sys.stdout.write(str(seq_record.id)+"\t"+str(ncount)+'\n')

