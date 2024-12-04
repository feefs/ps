package main

import (
	"fmt"
	"regexp"
	"strconv"
	"util"
)

func partOne(lines []string) error {
	r := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	result := 0
	for _, line := range lines {
		for _, match := range r.FindAllStringSubmatch(line, -1) {
			if len(match) != 3 {
				return fmt.Errorf("match isn't length 3: %v", match)
			}
			a, err := strconv.Atoi(match[1])
			if err != nil {
				return err
			}
			b, err := strconv.Atoi(match[2])
			if err != nil {
				return err
			}
			result += a * b
		}
	}

	// answer: 178794710
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	r := regexp.MustCompile(`do\(\)|don't\(\)|mul\((\d+),(\d+)\)`)
	result := 0
	enabled := true
	for _, line := range lines {
		for _, match := range r.FindAllStringSubmatch(line, -1) {
			switch match[0] {
			case "do()":
				enabled = true
			case "don't()":
				enabled = false
			default:
				if !enabled {
					break
				}
				if len(match) != 3 {
					return fmt.Errorf("match isn't length 3: %v", match)
				}
				a, err := strconv.Atoi(match[1])
				if err != nil {
					return err
				}
				b, err := strconv.Atoi(match[2])
				if err != nil {
					return err
				}
				result += a * b
			}
		}
	}

	// answer: 76729637
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
