package main

import "strings"

func parseSteps(lines []string) []step {
	result := []step{}
	stepStrings := strings.Split(lines[0], ",")
	for _, ss := range stepStrings {
		result = append(result, step(ss))
	}

	return result
}
