package main

import "strings"

func parse(lines []string) ([]string, []string) {
	patterns := strings.Split(strings.ReplaceAll(lines[0], " ", ""), ",")
	towels := []string{}
	for i := 2; i < len(lines); i++ {
		towels = append(towels, lines[i])
	}
	return patterns, towels
}
