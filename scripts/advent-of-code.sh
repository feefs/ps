#!/bin/bash -e

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

### GO 2023
mkdir -p "$DIR"
cat << EOF > "$DIR/main.go"
package main

import (
	"errors"
	"util"
)

func partOne(lines []string) error {
	return errors.New("part not implemented")
}

func partTwo(lines []string) error {
	return errors.New("part not implemented")
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
EOF
echo "package main" > "$DIR/parsing.go"
pushd "$DIR" > /dev/null
go mod init advent
go mod edit -replace util=../util
go get util@v0.0.0
go mod tidy
popd > /dev/null
touch "$DIR/input.txt"

### PYTHON 2022
# mkdir -p "$DIR"
# touch $DIR/input.txt
# for i in {1..2}; do
#     cat << EOF > $DIR/solution$i.py
# import os

# f = open(os.path.join(os.path.dirname(__file__), "input.txt"))
# EOF
# done
