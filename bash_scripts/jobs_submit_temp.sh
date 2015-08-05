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

perl blstxSECqsubNOParse_500.pl /fs/home/card/LinWork/byTri/e0102/stept/smallfastafile/pepfiles/pep.nonC_Trinity /fs/home/card/LinWork/byTri/e0102/stept/blastp/e0102_blastp/ /fs/home/card/LinWork/byTri/e0102/stept/blastp/qsub.e0102_blastp/ /fs/home/card/Aung/trinotate_req/uniport_sprot/uniprot_sprot.trinotate.pep blstp xxx 1 25 UniPorta

perl blstxSECqsubNOParse_500.pl /fs/home/card/LinWork/byTri/e0102/stept/smallfastafile/pepfiles/pep.nonC_Trinity /fs/home/card/LinWork/byTri/e0102/stept/blastp/e0102_blastp/ /fs/home/card/LinWork/byTri/e0102/stept/blastp/qsub.e0102_blastp /fs/home/card/Aung/trinotate_req/uniport_sprot/uniprot_sprot.trinotate.pep blstp xxx 26 50 UniPortb

