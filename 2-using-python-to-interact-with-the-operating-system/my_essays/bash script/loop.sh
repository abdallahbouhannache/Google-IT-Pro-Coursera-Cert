#!/bin/bash

echo "first loop"
n=1
while [ $n -le 10 ]; do
	echo " Iterating over $n"
	((n += 1))
done

echo "second loop"

n=150
while [ $n -ge 10 ]; do
	echo " Iterating over $n at :  $(date)"
	((n -= 1))
done

for i in 1 2 9 do
	echo $i
done
