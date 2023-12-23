package main

import (
	"regexp"
	"strconv"
)

func parseBricks(lines []string) []brick {
	result := []brick{}
	r := regexp.MustCompile(`(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)`)

	for id, line := range lines {
		match := r.FindStringSubmatch(line)
		x, _ := strconv.Atoi(match[1])
		y, _ := strconv.Atoi(match[2])
		z, _ := strconv.Atoi(match[3])
		x2, _ := strconv.Atoi(match[4])
		y2, _ := strconv.Atoi(match[5])
		z2, _ := strconv.Atoi(match[6])

		start := point{x, y, z}
		end := point{x2, y2, z2}

		result = append(result, brick{id, start, end})
	}

	return result
}
