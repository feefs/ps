package main

import (
	"regexp"
	"strconv"
	"util"
)

func parseGames(lines []string) ([]game, error) {
	r := regexp.MustCompile(`(\d+)`)
	games := []game{}

	row := 0
	currGame := game{}
	for _, line := range lines {
		if line == "" {
			row = 0
			continue
		}
		match := r.FindAllString(line, -1)
		if len(match) != 2 {
			return nil, util.InvalidStateError("match isn't length 2: %v", match)
		}
		a, err := strconv.Atoi(match[0])
		if err != nil {
			return nil, err
		}
		b, err := strconv.Atoi(match[1])
		if err != nil {
			return nil, err
		}
		if row == 0 {
			currGame.buttonA = button{a, b}
		} else if row == 1 {
			currGame.buttonB = button{a, b}
		} else {
			currGame.prize = prize{a, b}
			games = append(games, currGame)
			currGame = game{}
		}
		row += 1
	}

	return games, nil
}
