package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"util"
)

type race struct {
	T int
	D int
}

func parseRaces(lines []string) []race {
	r := regexp.MustCompile(`(\d+)`)
	timeMatches := r.FindAllString(lines[0], -1)
	distMatches := r.FindAllString(lines[1], -1)

	result := []race{}
	for i := 0; i < len(timeMatches); i++ {
		t, _ := strconv.Atoi(timeMatches[i])
		d, _ := strconv.Atoi(distMatches[i])
		race := race{T: t, D: d}
		result = append(result, race)
	}

	return result
}

func parseRace(lines []string) race {
	tStr := strings.TrimPrefix(lines[0], "Time:")
	tStr = strings.ReplaceAll(tStr, " ", "")
	dStr := strings.TrimPrefix(lines[1], "Distance:")
	dStr = strings.ReplaceAll(dStr, " ", "")
	t, _ := strconv.Atoi(tStr)
	d, _ := strconv.Atoi(dStr)

	return race{t, d}
}

func partOne(lines []string) error {
	races := parseRaces(lines)
	allWays := []int{}

	for _, race := range races {
		ways := 0
		for hold := 0; hold <= race.T; hold++ {
			if hold*(race.T-hold) > race.D {
				ways += 1
			}
		}
		allWays = append(allWays, ways)
	}

	result := 1
	for _, ways := range allWays {
		result *= ways
	}

	// answer: 800280
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	race := parseRace(lines)
	result := 0

	for hold := 0; hold <= race.T; hold++ {
		if hold*(race.T-hold) > race.D {
			result += 1
		}
	}

	// answer: 45128024
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
