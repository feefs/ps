package main

import (
	"fmt"
	"math"
	"util"
)

type levels []int

func isSafe(levels levels) bool {
	var increasing *bool
	for i := 0; i < len(levels)-1; i++ {
		a, b := levels[i], levels[i+1]

		currIncreasing := a < b
		if increasing == nil {
			increasing = &currIncreasing
		} else if currIncreasing != *increasing {
			return false
		}

		difference := 0
		if *increasing {
			difference = int(math.Abs(float64(b - a)))
		} else {
			difference = int(math.Abs(float64(a - b)))
		}
		if difference == 0 || difference > 3 {
			return false
		}
	}

	return true
}

func partOne(lines []string) error {
	allLevels, err := parseLevels(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, levels := range allLevels {
		if isSafe(levels) {
			result += 1
		}
	}

	// answer: 334
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	allLevels, err := parseLevels(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, levels := range allLevels {
		if isSafe(levels) {
			result += 1
			continue
		}

		for removeIndex := 0; removeIndex < len(levels); removeIndex++ {
			modifiedLevels := make([]int, len(levels))
			copy(modifiedLevels, levels)
			modifiedLevels = append(modifiedLevels[:removeIndex], modifiedLevels[removeIndex+1:]...)
			if isSafe(modifiedLevels) {
				result += 1
				break
			}
		}
	}

	// answer: 400
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
