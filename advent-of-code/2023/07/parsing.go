package main

import (
	"strconv"
	"strings"
)

func parseHand(line string) hand {
	result := hand{}
	values := strings.Split(line, " ")
	for _, c := range values[0] {
		result.cards = append(result.cards, card(c))
	}
	result.bid, _ = strconv.Atoi(values[1])

	return result
}

func parseHands(lines []string) []hand {
	result := []hand{}
	for _, line := range lines {
		result = append(result, parseHand(line))
	}

	return result
}
