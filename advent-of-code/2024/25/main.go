package main

import (
	"errors"
	"fmt"
	"util"
)

type lock [5]int
type key [5]int

func fits(l lock, k key) bool {
	for col := range 5 {
		if l[col]+k[col] > 5 {
			return false
		}
	}
	return true
}

func partOne(lines []string) error {
	locks, keys := parse(lines)

	result := 0
	for _, lock := range locks {
		for _, key := range keys {
			if fits(lock, key) {
				result += 1
			}
		}
	}

	// answer: 3397
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	return errors.New("part not implemented")
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
