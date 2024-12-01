package main

import (
	"fmt"
	"strconv"
	"strings"
)

func parseNums(lines []string) (*nums, error) {
	result := &nums{
		leftNums:  make([]int, len(lines)),
		rightNums: make([]int, len(lines)),
	}

	for i, line := range lines {
		split := strings.Fields(line)
		if len(split) != 2 {
			return nil, fmt.Errorf("match isn't length 2: %v", split)
		}

		left, err := strconv.Atoi(split[0])
		if err != nil {
			return nil, err
		}

		right, err := strconv.Atoi(split[1])
		if err != nil {
			return nil, err
		}

		result.leftNums[i] = left
		result.rightNums[i] = right
	}

	return result, nil
}
