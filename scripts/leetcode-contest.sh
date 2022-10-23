#!/bin/bash -e

if [[ $# -ne 1 ]]; then
    echo "Supply a folder name! Example:"
    echo "./scripts/leetcode-contest.sh weekly-0"
    exit 1
fi

DIR=leetcode-contests/$@

mkdir $DIR
for i in {1..4}; do
    echo $'# ' >> $DIR/$i.py
done
