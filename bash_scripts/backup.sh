#!/usr/bin/env bash

# syncing folder #Eclipse--->Pvannamei
# log file is appending from the end of previous backup log

# Assembly
rsync -raqz --log-file=/home/aung/rsync_log/assembly.log --ignore-existing card@eclipse:/fs/home/card/Assembly/ /mnt/nfs/media/assembly/

# Aung
rsync -raqz --log-file=/home/aung/rsync_log/aung.log --ignore-existing card@eclipse:/fs/home/card/Aung/ /mnt/nfs/media/Aung/

# LinWork
rsync -raqz --log-file=/home/aung/rsync_log/linwork.log --ignore-existing card@eclipse:/fs/home/card/LinWork/ /mnt/nfs/media2/LinWork/

# software
rsync -raqz --log-file=/home/aung/rsync_log/software.log --ignore-existing card@eclipse:/fs/home/card/software /mnt/nfs/media2/ &


# nfs server  to HD

rsync -raqz --log-file=/home/nfs/nfs_log/aung.log --ignore-existing /media/nfs/2TBHD2/Aung/ /home/nfs/HD1/Aung/
rsync -raqz --log-file=/home/nfs/nfs_log/linwork.log --ignore-existing /media/nfs/2TBHD2/LinWork /home/nfs/HD2/

rsync -raqz --log-file=/home/nfs/nfs_log/assembly1.log --ignore-existing /media/nfs/2TBHD2/assembly/ /home/nfs/HD1/Assembly/
rsync -raqz --log-file=/home/nfs/nfs_log/assembly2.log --ignore-existing /media/nfs/2TBHD2/assembly/ /home/nfs/HD2/

rsync -raqz --log-file=/home/nfs/nfs_log/newsra.log --ignore-existing /home/back_up/ /home/nfs/HD1/SRA_New_062015/





