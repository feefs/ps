package main

import (
	"strconv"
	"strings"
)

func parseRows(lines []string) []row {
	result := []row{}
	for _, line := range lines {
		split := strings.Split(line, " ")
		groupSizes := strings.Split(split[1], ",")
		groups := []int{}
		for _, gs := range groupSizes {
			val, _ := strconv.Atoi(gs)
			groups = append(groups, val)
		}

		// append "." to the end of each row to make end checking easier
		result = append(result,
			row{
				tokens: split[0] + ".",
				groups: groups,
				dp:     make(map[key]int),
			})
	}

	return result
}
