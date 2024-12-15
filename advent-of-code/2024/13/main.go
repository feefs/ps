package main

import (
	"fmt"
	"util"
)

type button struct {
	x int
	y int
}

type prize struct {
	X int
	Y int
}

type game struct {
	buttonA button
	buttonB button
	prize   prize
}

func partOne(lines []string) error {
	games, err := parseGames(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, game := range games {
		fmt.Println(game)
		x1, x2 := float64(game.buttonA.x), float64(game.buttonB.x)
		y1, y2 := float64(game.buttonA.y), float64(game.buttonB.y)
		X, Y := float64(game.prize.X), float64(game.prize.Y)
		a := ((X * y2) - (Y * x2)) / ((x1 * y2) - (y1 * x2))
		b := ((Y * x1) - (X * y1)) / ((x1 * y2) - (y1 * x2))
		aInt, bInt := int(a), int(b)
		fmt.Println(a, b, aInt, bInt)
		if a == float64(aInt) && b == float64(bInt) {
			result += (3 * aInt) + bInt
		}
	}

	// answer: 29388
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	games, err := parseGames(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, game := range games {
		fmt.Println(game)
		x1, x2 := float64(game.buttonA.x), float64(game.buttonB.x)
		y1, y2 := float64(game.buttonA.y), float64(game.buttonB.y)
		X, Y := float64(game.prize.X)+10_000_000_000_000, float64(game.prize.Y)+10_000_000_000_000
		a := ((X * y2) - (Y * x2)) / ((x1 * y2) - (y1 * x2))
		b := ((Y * x1) - (X * y1)) / ((x1 * y2) - (y1 * x2))
		aInt, bInt := int(a), int(b)
		fmt.Println(a, b, aInt, bInt)
		if a == float64(aInt) && b == float64(bInt) {
			result += (3 * aInt) + bInt
		}
	}

	// answer: 99548032866004
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
