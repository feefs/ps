package main

import (
	"strconv"
	"strings"
)

func parseNumbers(line string) []int {
	result := []int{}
	for _, numStr := range strings.Split(line, " ") {
		num, _ := strconv.Atoi(numStr)
		result = append(result, num)
	}

	return result
}
