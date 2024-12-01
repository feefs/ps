package main

import (
	"fmt"
	"math"
	"slices"
	"util"
)

type nums struct {
	leftNums  []int
	rightNums []int
}

func partOne(lines []string) error {
	nums, err := parseNums(lines)
	if err != nil {
		return err
	}

	slices.Sort(nums.leftNums)
	slices.Sort(nums.rightNums)

	result := 0
	for i := 0; i < len(nums.leftNums); i++ {
		result += int(math.Abs(float64(nums.leftNums[i] - nums.rightNums[i])))
	}

	// answer: 1834060
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	nums, err := parseNums(lines)
	if err != nil {
		return err
	}

	counts := map[int]int{}
	for _, right := range nums.rightNums {
		if _, ok := counts[right]; !ok {
			counts[right] = 0
		}
		counts[right] += 1
	}

	result := 0
	for _, left := range nums.leftNums {
		if count, ok := counts[left]; ok {
			result += left * count
		}
	}

	// answer: 21607792
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
