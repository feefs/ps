package main

import (
	"fmt"
	"strconv"
	"strings"
	"util"
)

type game struct {
	id     int
	rounds []round
}

type round struct {
	red   int
	green int
	blue  int
}

func parseGame(line string) (*game, error) {
	result := &game{rounds: []round{}}
	trimmed := strings.TrimPrefix(line, "Game ")

	values := strings.Split(trimmed, ":")
	if len(values) != 2 {
		return nil, util.InvalidStateError("length of values should be two, actual length %v", len(values))
	}

	id, err := strconv.Atoi(values[0])
	if err != nil {
		return result, err
	}
	result.id = id

	gameRounds := strings.Split(values[1], ";")
	for _, gameRound := range gameRounds {
		gameRound = strings.TrimSpace(gameRound)
		cubeCounts := strings.Split(gameRound, ", ")

		round := round{}
		for _, cubeCount := range cubeCounts {
			values := strings.Split(cubeCount, " ")
			if len(values) != 2 {
				return nil, util.InvalidStateError("length of values should be two, actual length %v", len(values))
			}

			numCubes, err := strconv.Atoi(values[0])
			if err != nil {
				return nil, err
			}

			color := values[1]
			switch color {
			case "red":
				round.red = numCubes
			case "green":
				round.green = numCubes
			case "blue":
				round.blue = numCubes
			default:
				return nil, util.InvalidStateError("invalid color %v", color)
			}
		}
		result.rounds = append(result.rounds, round)
	}

	return result, nil
}

func parseGames(lines []string) ([]*game, error) {
	games := []*game{}
	for _, line := range lines {
		game, err := parseGame(line)
		if err != nil {
			return nil, err
		}
		games = append(games, game)
	}
	return games, nil
}

func partOne(lines []string) error {
	result := 0
	games, err := parseGames(lines)
	if err != nil {
		return err
	}

	for _, game := range games {
		validGame := true
		for _, round := range game.rounds {
			if round.red > 12 || round.green > 13 || round.blue > 14 {
				validGame = false
				break
			}
		}
		if validGame {
			result += game.id
		}
	}

	// answer: 2563
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	result := 0
	games, err := parseGames(lines)
	if err != nil {
		return err
	}

	for _, game := range games {
		fewestRed, fewestBlue, fewestGreen := 0, 0, 0
		for _, round := range game.rounds {
			fewestRed = max(fewestRed, round.red)
			fewestGreen = max(fewestGreen, round.green)
			fewestBlue = max(fewestBlue, round.blue)
		}
		result += fewestRed * fewestGreen * fewestBlue
	}

	// answer: 70768
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
