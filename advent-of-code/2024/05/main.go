package main

import (
	"fmt"
	"slices"
	"util"
)

type pageOrdering struct {
	x int
	y int
}

type update struct {
	pages []int
}

func partOne(lines []string) error {
	pageOrderings, updates, err := parse(lines)
	if err != nil {
		return err
	}

	after := map[int]([]int){}
	for _, pageOrdering := range pageOrderings {
		after[pageOrdering.x] = append(after[pageOrdering.x], pageOrdering.y)
	}

	result := 0
UpdateLoop:
	for _, update := range updates {
		for i := 0; i < len(update.pages); i++ {
			for j := i + 1; j < len(update.pages); j++ {
				if !slices.Contains(after[update.pages[i]], update.pages[j]) {
					continue UpdateLoop
				}
			}
		}
		result += update.pages[len(update.pages)/2]
	}

	// answer: 4185
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	pageOrderings, updates, err := parse(lines)
	if err != nil {
		return err
	}

	after := map[int]([]int){}
	for _, pageOrdering := range pageOrderings {
		after[pageOrdering.x] = append(after[pageOrdering.x], pageOrdering.y)
	}

	result := 0
	for _, update := range updates {
		fixed := false
		for i := 0; i < len(update.pages); i++ {
			for j := i + 1; j < len(update.pages); j++ {
				if !slices.Contains(after[update.pages[i]], update.pages[j]) {
					fixed = true
					update.pages[i], update.pages[j] = update.pages[j], update.pages[i]
				}
			}
		}
		if fixed {
			result += update.pages[len(update.pages)/2]
		}
	}

	// answer: 4480
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
