package main

import (
	"regexp"
	"strconv"
	"strings"
)

func parseHailstones(lines []string) []hailstone {
	result := []hailstone{}

	r := regexp.MustCompile(`([^\s]+),\s*([^\s]+),\s*([^\s]+)`)
	for _, line := range lines {
		split := strings.Split(line, " @ ")
		posValues, velValues := split[0], split[1]

		posMatch := r.FindStringSubmatch(posValues)
		px, _ := strconv.ParseFloat(posMatch[1], 64)
		py, _ := strconv.ParseFloat(posMatch[2], 64)
		pz, _ := strconv.ParseFloat(posMatch[3], 64)

		velMatch := r.FindStringSubmatch(velValues)
		vx, _ := strconv.ParseFloat(velMatch[1], 64)
		vy, _ := strconv.ParseFloat(velMatch[2], 64)
		vz, _ := strconv.ParseFloat(velMatch[3], 64)

		result = append(result, hailstone{
			position{px, py, pz},
			velocity{vx, vy, vz},
		})
	}

	return result
}
