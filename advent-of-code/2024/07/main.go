package main

import (
	"fmt"
	"strconv"
	"util"
)

type equation struct {
	testValue int
	nums      []int
}

func (e equation) satisfies() bool {
	var f func(nums []int, curr int) bool
	f = func(nums []int, curr int) bool {
		if len(nums) == 0 {
			return curr == e.testValue
		}
		if curr > e.testValue {
			return false
		}
		return f(nums[1:], curr+nums[0]) || f(nums[1:], curr*nums[0])
	}

	return f(e.nums, 0)
}

func (e equation) satisfiesWithConcatenation() (bool, error) {
	var f func(nums []int, curr int) (bool, error)
	f = func(nums []int, curr int) (bool, error) {
		if len(nums) == 0 {
			return curr == e.testValue, nil
		}
		if curr > e.testValue {
			return false, nil
		}

		add, err := f(nums[1:], curr+nums[0])
		if err != nil {
			return false, err
		}
		mul, err := f(nums[1:], curr*nums[0])
		if err != nil {
			return false, err
		}
		c, err := strconv.Atoi(strconv.Itoa(curr) + strconv.Itoa(nums[0]))
		if err != nil {
			return false, err
		}
		con, err := f(nums[1:], c)
		if err != nil {
			return false, err
		}

		return (add || mul || con), nil
	}

	return f(e.nums, 0)
}

func partOne(lines []string) error {
	equations, err := parseEquations(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, equation := range equations {
		if equation.satisfies() {
			result += equation.testValue
		}
	}

	// answer: 975671981569
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	equations, err := parseEquations(lines)
	if err != nil {
		return err
	}

	result := 0
	for _, equation := range equations {
		sat, err := equation.satisfiesWithConcatenation()
		if err != nil {
			return err
		}
		if sat {
			result += equation.testValue
		}
	}

	// answer: 223472064194845
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
