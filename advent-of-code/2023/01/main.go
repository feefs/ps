package main

import (
	"fmt"
	"strings"
	"unicode"
	"util"
)

func partOne(lines []string) error {
	result := 0

	for _, line := range lines {
		firstDigit := -1
		lastDigit := -1
		for _, r := range line {
			if !unicode.IsDigit(r) {
				continue
			}

			digit := int(r - '0')
			if firstDigit == -1 {
				firstDigit = digit
			}
			lastDigit = digit
		}

		if firstDigit == -1 {
			continue
		}

		result += (10 * firstDigit) + lastDigit
	}

	// answer: 55447
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	mappings := map[string]int{
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}
	result := 0

	for _, line := range lines {
		firstDigit := -1
		lastDigit := -1
		leftmostIndex := len(line)
		rightmostIndex := -1
		for word, digit := range mappings {
			if i := strings.Index(line, word); i != -1 {
				if i < leftmostIndex {
					leftmostIndex = i
					firstDigit = digit
				}
			}
			if i := strings.LastIndex(line, word); i != -1 {
				if i > rightmostIndex {
					rightmostIndex = i
					lastDigit = digit
				}
			}
		}

		for i, r := range line {
			if !unicode.IsDigit(r) {
				continue
			}

			digit := int(r - '0')
			if i < leftmostIndex {
				leftmostIndex = i
				firstDigit = digit
			}
			if i > rightmostIndex {
				rightmostIndex = i
				lastDigit = digit
			}
		}

		if firstDigit == -1 {
			continue
		}

		result += (10 * firstDigit) + lastDigit
	}

	// answer: 54706
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
