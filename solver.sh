#!/bin/sh

cd Solutions

# 1
i=1
for problem in ./Problem*.py; do
    echo Solution to problem $i 
    python $problem
    i=$((i+1))
done

