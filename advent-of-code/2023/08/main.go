package main

import (
	"fmt"
	"util"
)

type instructions []string

type pair struct {
	left  string
	right string
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

func lcm(values ...int) int {
	a, b := values[0], values[1]
	v := (a * b) / gcd(a, b)
	if len(values) == 2 {
		return v
	}
	remaining := []int{v}
	remaining = append(remaining, values[2:]...)

	return lcm(remaining...)
}

func partOne(lines []string) error {
	instructions := parseInstructions(lines[0])
	pairs := parsePairs(lines[2:])

	result := 0
	curr := "AAA"
out:
	for {
		for _, instruction := range instructions {
			if curr == "ZZZ" {
				break out
			}
			if instruction == "L" {
				curr = pairs[curr].left
			} else {
				curr = pairs[curr].right
			}
			result += 1
		}
	}

	// answer: 14681
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	instructions := parseInstructions(lines[0])
	pairs := parsePairs(lines[2:])

	nodes := []string{}
	for k := range pairs {
		if k[2] == 'A' {
			nodes = append(nodes, k)
		}
	}

	periods := []int{}
	for _, node := range nodes {
		curr := node
		period := 0
	out:
		for {
			for _, instruction := range instructions {
				if curr[2] == 'Z' {
					break out
				}
				if instruction == "L" {
					curr = pairs[curr].left
				} else {
					curr = pairs[curr].right
				}
				period += 1
			}
		}
		periods = append(periods, period)
	}
	result := lcm(periods...)

	// answer: 14321394058031
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
