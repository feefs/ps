package main

import (
	"fmt"
	"strconv"
	"strings"
)

func parseEquations(lines []string) ([]equation, error) {
	equations := []equation{}

	for _, line := range lines {
		split := strings.Split(line, ":")
		if len(split) != 2 {
			return nil, fmt.Errorf("split isn't length 2: %v", split)
		}

		testValue, err := strconv.Atoi(split[0])
		if err != nil {
			return nil, err
		}

		fields := strings.Fields(split[1])
		nums := []int{}
		for _, num := range fields {
			n, err := strconv.Atoi(num)
			if err != nil {
				return nil, err
			}
			nums = append(nums, n)
		}

		equations = append(equations, equation{testValue, nums})
	}

	return equations, nil
}
