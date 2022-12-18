#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Enter a year and day! Example:"
    echo "./scripts/advent-of-code.sh 2022 01"
    exit 1
fi

DIR=advent-of-code/$1/$2

if [[ -d $DIR ]]; then
    echo "Directory $DIR already exists!"
    exit 1
fi

mkdir -p $DIR
touch $DIR/input.txt
for i in {1..2}; do
    cat << EOF > $DIR/solution$i.py
import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))
EOF
done
