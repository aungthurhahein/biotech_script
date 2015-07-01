#!/usr/bin/env python
"""
# check SGE server nodes availability.(Need to run at head node)
# usage:python check_SGE_Nodes.py
# output: list of recommended node to submit jobs
# Dev: __author__ = 'aung' 
# Date: 03/06/2015
"""
import os
stdout = os.popen("qstat -u '*'")

# nodes that user "card" can submit jobs to
aval_node = ['compute-0-7.local', 'compute-0-8.local', 'compute-0-9.local', 'compute-0-10.local', 'compute-0-11.local',
             'compute-0-13.local', 'compute-0-14.local', 'compute-0-15.local', 'compute-0-17.local']

job_summary = {}
job_aval = {}
for line in stdout:
    line_split = line.split()
    if len(line_split) > 4:
        job_stat = line_split[4]
        if job_stat == 'r':
            job_node = line_split[7]
            job_slot = line_split[8]
            if job_node in job_summary:
                job_summary[job_node] += int(job_slot)
            else:
                job_summary[job_node] = int(job_slot)
print "List of All Nodes with Occupied Slots"
print "#------------------------------------#"
print "Nodes\tSlots"
for key, value in job_summary.iteritems():
    print key.split('@')[1],'\t', value
    if value < 32:
        job_aval[key.split('@')[1]] = value
print "#------------------------------------#"
print "\n"
print "List of Recommended Nodes"
print "#------------------------------------#"
print "Nodes\tOccupied Slots\tAvailable Slots"
for key,value in job_aval.iteritems():
    if key.strip() in aval_node:
        print key,'\t',value,'\t',32-value
print "#------------------------------------#"


