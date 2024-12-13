package main

import (
	"fmt"
	"strconv"
	"strings"
	"util"
)

type key struct {
	stone int
	blink int
}

func f(stone int, blink int, cache map[key]int) int {
	k := key{stone, blink}
	if result, ok := cache[k]; ok {
		return result
	}
	if blink == 0 {
		return 1
	}
	if stone == 0 {
		cache[k] = f(1, blink-1, cache)
		return cache[k]
	}
	digits := strconv.Itoa(stone)
	if len(digits)%2 == 0 {
		left, right := digits[:len(digits)/2], digits[len(digits)/2:]
		l, _ := strconv.Atoi(left)
		r, _ := strconv.Atoi(right)
		cache[k] = f(l, blink-1, cache) + f(r, blink-1, cache)
		return cache[k]
	} else {
		cache[k] = f(stone*2024, blink-1, cache)
		return cache[k]
	}
}

func partOne(lines []string) error {
	stones := []int{}
	for _, f := range strings.Fields(lines[0]) {
		stone, err := strconv.Atoi(f)
		if err != nil {
			return err
		}
		stones = append(stones, stone)
	}

	result := 0
	for _, stone := range stones {
		result += f(stone, 25, make(map[key]int))
	}

	// answer: 175006
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	stones := []int{}
	for _, f := range strings.Fields(lines[0]) {
		stone, err := strconv.Atoi(f)
		if err != nil {
			return err
		}
		stones = append(stones, stone)
	}

	result := 0
	for _, stone := range stones {
		result += f(stone, 75, make(map[key]int))
	}

	// answer: 207961583799296
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
