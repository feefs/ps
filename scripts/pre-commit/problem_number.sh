#!/bin/bash
for problem in "$@"; do
    if ! head -n 1 "$problem" | grep '^# \d*\. .*$'; then
        echo "$problem is missing a leetcode problem number!"
        exit 1
    fi
done
