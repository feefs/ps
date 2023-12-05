package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
	"util"
)

type card struct {
	id              int
	winningNumbers  []int
	obtainedNumbers []int
}

func (c card) numMatches() int {
	result := 0
	winning := map[int]struct{}{}
	for _, num := range c.winningNumbers {
		winning[num] = struct{}{}
	}
	for _, num := range c.obtainedNumbers {
		if _, ok := winning[num]; ok {
			result += 1
		}
	}

	return result
}

// s is a string of numbers, each max 2 digits in length and padded
// ex: 61 17 26 13 92  5 73 29 53 42 62 46 96 32 21 97 99 28 12  4  7 44 19 71 76
func parseNumbers(s string) ([]int, error) {
	result := []int{}
	for i := 0; i < len(s)-1; i += 3 {
		num := 0
		if unicode.IsDigit(rune(s[i])) {
			num += 10 * (int(s[i]) - '0')
		}
		num += int(s[i+1]) - '0'
		result = append(result, num)
	}

	return result, nil
}

func parseCard(line string) (result card, err error) {
	trimmed := strings.TrimPrefix(line, "Card")
	values := strings.Split(trimmed, ":")
	if len(values) != 2 {
		return result, util.InvalidStateError("values should be length 2, actual length is %v", len(values))
	}

	id, err := strconv.Atoi(strings.TrimSpace(values[0]))
	if err != nil {
		return result, err
	}
	result.id = id

	values = strings.Split(values[1], "|")
	if len(values) != 2 {
		return result, util.InvalidStateError("values should be length 2, actual length is %v", len(values))
	}

	leftNumbers, rightNumbers := values[0][1:len(values[0])-1], values[1][1:]
	result.winningNumbers, err = parseNumbers(leftNumbers)
	if err != nil {
		return result, err
	}
	result.obtainedNumbers, err = parseNumbers(rightNumbers)
	if err != nil {
		return result, err
	}

	return result, nil
}

func parseCards(lines []string) ([]card, error) {
	cards := []card{}
	for _, line := range lines {
		card, err := parseCard(line)
		if err != nil {
			return nil, err
		}
		cards = append(cards, card)
	}

	return cards, nil
}

func partOne(lines []string) error {
	result := 0
	cards, err := parseCards(lines)
	if err != nil {
		return err
	}

	for _, card := range cards {
		matches := card.numMatches()
		points := 0
		for i := 0; i < matches; i++ {
			if points == 0 {
				points += 1
			} else {
				points *= 2
			}
		}
		result += points
	}

	// answer: 24706
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	result := 0
	cards, err := parseCards(lines)
	if err != nil {
		return err
	}

	copies := make([]int, len(cards))
	for i := 0; i < len(copies); i++ {
		copies[i] = 1
	}

	for i, card := range cards {
		matches := card.numMatches()
		for copy := 0; copy < copies[i]; copy++ {
			for j := 0; j < matches; j++ {
				copies[i+j+1] += 1
			}
		}
	}

	for _, copy := range copies {
		result += copy
	}

	// answer: 13114317
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
