#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "Supply a folder name! Example:"
    echo "./scripts/leetcode-contest.sh weekly-0"
    exit 1
fi

DIR=leetcode-contests/$1

if [[ -d $DIR ]]; then
    echo "Directory $DIR already exists!"
    exit 1
fi

mkdir $DIR
for i in {1..4}; do
    echo -n $'# ' >> $DIR/$i.py
done
