"""
# -*- coding: utf-8 -*-
# @Author: Aung Thu Rha Hein
# @Date:   2016-03-28 11:28:15
# @Last Modified by:   Aung Thu Rha Hein
# @Last Modified time: 2016-03-28 12:52:39
# check SGE server nodes availability and change queued jobs to these nodes
"""
import sys
import os
import random
stdout = os.popen("qstat")
aval_node= os.popen("python $HOME/bin/check_SGE_Nodes.py")  #expected to find this python script at $HOME/bin/

free_node = []
for node in aval_node:
    if "compute" in node:
        l_split = node.split()
        free_node.append(l_split[0])

queue_jobs = []
for line in stdout:
    line_split = line.split()
    if len(line_split) > 4:
        job_stat = line_split[4]
        job_id = line_split[0]
        if job_stat == 'qw':
            queue_jobs.append(job_id)

for qj in queue_jobs:
    rand_node = random.choice(free_node)
    job_alt = "qalter -l hostname=\""+rand_node+"\" "+ qj
    f = os.popen(job_alt)
    sys.stdout.write(f.read().strip('\n')+ "to "+ rand_node+'\n') 

