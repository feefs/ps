package main

import (
	"fmt"
	"strings"
	"util"
)

func possibleWays(towel string, patterns []string) int {
	cache := map[string]int{}
	var f func(curr string) int
	f = func(curr string) int {
		if v, ok := cache[curr]; ok {
			return v
		}
		if len(curr) == 0 {
			return 1
		}
		ways := 0
		for _, p := range patterns {
			if !strings.HasPrefix(string(curr), string(p)) {
				continue
			}
			ways += f(curr[len(p):])
		}
		cache[curr] = ways
		return cache[curr]
	}
	return f(towel)
}

func partOne(lines []string) error {
	patterns, towels := parse(lines)

	result := 0
	for _, towel := range towels {
		ways := possibleWays(towel, patterns)
		if ways > 0 {
			result += 1
		}
	}

	// answer: 319
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	patterns, towels := parse(lines)

	result := 0
	for _, towel := range towels {
		result += possibleWays(towel, patterns)
	}

	// answer: 692575723305545
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
