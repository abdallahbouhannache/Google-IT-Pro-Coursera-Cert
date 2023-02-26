#!/bin/bash

a=ls -la

for fruit in peach apple; do
    echo "$fruit"
done

for file in *.HTM; do
    name= $(basename "$file" .HTM)
    echo "name"
done
