#!/bin/bash
for file in "$@"; do buildifier "$file"; done
