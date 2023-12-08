package main

import (
	"regexp"
)

func parseInstructions(line string) instructions {
	result := []string{}
	for _, c := range line {
		result = append(result, string(c))
	}

	return result
}

func parsePairs(lines []string) map[string]pair {
	result := map[string]pair{}
	r := regexp.MustCompile(`(\w+)`)
	for _, line := range lines {
		values := r.FindAllString(line, -1)
		result[values[0]] = pair{left: values[1], right: values[2]}
	}

	return result
}
