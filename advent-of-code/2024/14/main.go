package main

import (
	"fmt"
	"slices"
	"util"
)

type position struct {
	x int
	y int
}

type velocity struct {
	dx int
	dy int
}

type robot struct {
	pos position
	vel velocity
}

func tick(p position, v velocity) position {
	return position{
		(p.x + v.dx + 101) % 101,
		(p.y + v.dy + 103) % 103,
	}
}

func safetyFactor(positions []position) int {
	quad1, quad2, quad3, quad4 := 0, 0, 0, 0
	for _, pos := range positions {
		if pos.x == 50 || pos.y == 51 {
			continue
		}
		if pos.x > 50 {
			if pos.y < 51 {
				quad1 += 1
			} else {
				quad4 += 1
			}
		} else {
			if pos.y < 51 {
				quad2 += 1
			} else {
				quad3 += 1
			}
		}
	}
	return quad1 * quad2 * quad3 * quad4
}

func partOne(lines []string) error {
	robots, err := parseRobots(lines)
	if err != nil {
		return err
	}

	positions := []position{}
	for _, robot := range robots {
		positions = append(positions, robot.pos)
	}

	for range 100 {
		for i := range positions {
			positions[i] = tick(positions[i], robots[i].vel)
		}
	}

	result := safetyFactor(positions)

	// answer: 229421808
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	robots, err := parseRobots(lines)
	if err != nil {
		return err
	}

	positions := []position{}
	for _, robot := range robots {
		positions = append(positions, robot.pos)
	}

	iterations := 100_000
	safetyFactors := []int{safetyFactor(positions)}
	for range iterations {
		for i := range positions {
			positions[i] = tick(positions[i], robots[i].vel)
		}
		safetyFactors = append(safetyFactors, safetyFactor(positions))
	}

	result := slices.Index(safetyFactors, slices.Min(safetyFactors))

	// answer: 6577
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
