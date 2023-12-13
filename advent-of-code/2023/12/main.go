package main

import (
	"fmt"
	"strings"
	"util"
)

type row struct {
	tokens string
	groups []int
	dp     map[key]int
}

type key struct {
	ti   int
	gi   int
	curr int
}

func (r row) f(ti, gi, curr int) (result int) {
	key := key{ti, gi, curr}
	if result, ok := r.dp[key]; ok {
		return result
	}
	defer func() { r.dp[key] = result }()

	if ti == len(r.tokens) {
		// if we reach the end of tokens and groups, and the current group is empty
		if gi == len(r.groups) && curr == 0 {
			return 1
		} else {
			return 0
		}
	}

	possibilities := []rune{}
	if r.tokens[ti] == '?' {
		possibilities = append(possibilities, '.', '#')
	} else {
		possibilities = append(possibilities, rune(r.tokens[ti]))
	}

	for _, p := range possibilities {
		if p == '#' {
			// continue to the next token and increase the group size
			result += r.f(ti+1, gi, curr+1)
		} else if curr > 0 {
			// p must be '.'
			// if we can complete the current group
			//   complete the group and continue to the next token and group
			if gi < len(r.groups) && curr == r.groups[gi] {
				result += r.f(ti+1, gi+1, 0)
			}
		} else {
			// p must be '.'
			// if we can't complete the current group
			//   continue to the next token
			result += r.f(ti+1, gi, 0)
		}
	}

	return result
}

func partOne(lines []string) error {
	rows := parseRows(lines)

	result := 0
	for _, row := range rows {
		result += row.f(0, 0, 0)
	}

	// answer: 7716
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	rows := parseRows(lines)

	result := 0
	for _, row := range rows {
		tokens := row.tokens[:len(row.tokens)-1]
		newTokens := []string{}
		for i := 0; i < 5; i++ {
			newTokens = append(newTokens, tokens)
		}
		row.tokens = strings.Join(newTokens, "?") + "."

		newGroups := []int{}
		for i := 0; i < 5; i++ {
			newGroups = append(newGroups, row.groups...)
		}
		row.groups = newGroups

		result += row.f(0, 0, 0)
	}

	// answer: 18716325559999
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
