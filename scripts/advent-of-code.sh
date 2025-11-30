#!/bin/bash -e

if [[ $# -ne 2 ]]; then
    echo "Enter a year and day! Example:"
    echo "./scripts/advent-of-code.sh 2025 01"
    exit 1
fi

if ! [[ "$2" =~ ^[0-9]{2}$ ]]; then
    echo "Day must be a two-digit number! Example: 01"
    exit 1
fi

DIR=advent-of-code/$1/days

### C++ 2025
mkdir -p "$DIR"
cat << EOF > "$DIR/day$2.hh"
#pragma once

#include "absl/status/status.h"

namespace day$2 {

absl::Status PartOne(std::vector<std::string> lines);
absl::Status PartTwo(std::vector<std::string> lines);

}  // namespace day$2
EOF
cat << EOF > "$DIR/day$2.cc"
#include "day$2.hh"

#include "absl/log/log.h"
#include "absl/status/status.h"

namespace day$2 {

absl::Status PartOne(std::vector<std::string> lines) {
  (void)lines;
  LOG(WARNING) << "Part 1 isn't implemented.";
  return absl::UnimplementedError("Part 1 isn't implemented.");
}

absl::Status PartTwo(std::vector<std::string> lines) {
  (void)lines;
  LOG(WARNING) << "Part 2 isn't implemented.";
  return absl::UnimplementedError("Part 2 isn't implemented.");
}

}  // namespace day$2
EOF
cat << EOF >> "$DIR/BUILD.bazel"

cc_library(
    name = "day$2",
    srcs = ["day$2.cc"],
    hdrs = ["day$2.hh"],
    deps = [
        "@abseil-cpp//absl/log",
        "@abseil-cpp//absl/status",
    ],
)
EOF
sed -i "s|// #include \"days/day$2.hh\"|#include \"days/day$2.hh\"|" advent-of-code/2025/main.cc
sed -i -E "s|(//) (\{[0-9]+, \{&day$2::PartOne, &day$2::PartTwo\}\},)|\2|" advent-of-code/2025/main.cc
sed -i "s|# \"//days:day$2\"|\"//days:day$2\"|" advent-of-code/2025/BUILD.bazel
cd "advent-of-code/$1"
bazel run //:refresh_compile_commands 2>/dev/null
echo "Set up day $2!"

# if [[ $# -ne 2 ]]; then
#     echo "Enter a year and day! Example:"
#     echo "./scripts/advent-of-code.sh 2022 01"
#     exit 1
# fi

# DIR=advent-of-code/$1/$2

# if [[ -d $DIR ]]; then
#     echo "Directory $DIR already exists!"
#     exit 1
# fi

### GO 2023 2024
# mkdir -p "$DIR"
# cat << EOF > "$DIR/main.go"
# package main

# import (
# 	"errors"
# 	"util"
# )

# func partOne(lines []string) error {
# 	return errors.New("part not implemented")
# }

# func partTwo(lines []string) error {
# 	return errors.New("part not implemented")
# }

# func main() {
# 	util.ParseAndRun(partOne, partTwo)
# }
# EOF
# echo "package main" > "$DIR/parsing.go"
# pushd "$DIR" > /dev/null
# go mod init advent
# go mod edit -replace util=../util
# go get util@v0.0.0
# go mod tidy
# popd > /dev/null
# touch "$DIR/input.txt"
# echo "Set up directory: $DIR"

### PYTHON 2022
# mkdir -p "$DIR"
# touch $DIR/input.txt
# for i in {1..2}; do
#     cat << EOF > $DIR/solution$i.py
# import os

# f = open(os.path.join(os.path.dirname(__file__), "input.txt"))
# EOF
# done
