package main

import (
	"regexp"
	"strconv"
)

func parseDigs(lines []string) []dig {
	result := []dig{}
	r := regexp.MustCompile(`(\w) (\d+)`)
	for _, line := range lines {
		match := r.FindStringSubmatch(line)
		direction := dir(match[1])
		amount, _ := strconv.Atoi(match[2])
		result = append(result, dig{direction, amount})
	}

	return result
}

func parseHexDigs(lines []string) []dig {
	result := []dig{}
	r := regexp.MustCompile(`\w \d+ \(#(\w+)\)`)
	dirMapping := map[int64]dir{
		0: right,
		1: down,
		2: left,
		3: up,
	}
	for _, line := range lines {
		match := r.FindStringSubmatch(line)
		hex := match[1]
		dirInt, _ := strconv.ParseInt(hex[5:], 16, 0)
		amount, _ := strconv.ParseInt(hex[:5], 16, 0)
		result = append(result, dig{dirMapping[dirInt], int(amount)})
	}

	return result
}
