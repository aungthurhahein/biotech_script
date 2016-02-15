#! /bin/bash
msg=$0
# git status
git pull
git add -A
git commit -m $msg
git push origin master
