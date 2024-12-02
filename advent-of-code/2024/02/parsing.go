package main

import (
	"strconv"
	"strings"
)

func parseLevels(lines []string) ([]levels, error) {
	allLevels := make([]levels, len(lines))

	for i, line := range lines {
		split := strings.Fields(line)
		levels := make(levels, len(split))
		for j, str := range split {
			n, err := strconv.Atoi(str)
			if err != nil {
				return nil, err
			}
			levels[j] = n
		}
		allLevels[i] = levels
	}

	return allLevels, nil
}
