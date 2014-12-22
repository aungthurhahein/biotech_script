#! /bin/bash
# just a script to put multiple jobs into nodes

Dataset=(SRR839222 SRR1037362 SRR1037365 SRR842625 SRR839236 SRR1037363 SRR842627 SRR1037366 SRR842572 SRR1037364 SRR1039534)

node=('compute-0-9' 'compute-0-8' 'compute-0-10' 'compute-0-11' 'compute-0-12' 'compute-0-13' 'compute-0-14' 'compute-0-15' 'compute-0-16' 'compute-0-8' 'compute-0-9')

c=0

for i in "${Dataset[@]}"
do
        qsub -l hostname= ${node[c]} {$i}.IL_PE
        c =c +1
done

~                                                                                                  
~                                                                                                  
~                