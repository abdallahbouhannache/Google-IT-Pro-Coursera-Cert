#!/bin/bash

n=0
command=$1
echo "$1  $2"
while ! $command && [ $n -le 5 ]; do
	sleep $n
	((n = n + 1))
	echo "Retry  #$n"
done
