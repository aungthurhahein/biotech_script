#!/bin/sh
#$ -S /bin/bash
#Define name of job
#$ -N job-name
# Run in current working dir
#$ -cwd
#flag to notify when the jod submitted(b) or finished(e) or both(be)
#$ -m e
#email to distribute job status
#$ -M aungthurhahein@gmail.com
# for mutli-thread(parallel) jobs, provide no. of nodes to run(even number make sense)
#$ -pe mpich 4

. /fs/home/card/.bashrc
. /fs/home/card/.bash_profile
