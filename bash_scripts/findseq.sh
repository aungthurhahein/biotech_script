#!/bin/sh
cat query | while read LINE;do grep -A 1 $LINE a01_PM_Count; done > queryout.txt

