#!/bin/bash

line="-----------------------------------"
echo "Starting at: $(date)"
echo $line
echo "UPTIME"
uptime
echo $line
echo "FREE"
free
echo $line
echo "WHO\'s running it"
who
echo $line
echo "Finishing at :$(date)"
echo $line

for i in $(cat story.txt); do
B=`echo -n "${i:0:1} " | tr "[:lower:]" "[:upper:]"`; 
echo -n "${B}${i:1}"
echo -e "\n"
done;
