package main

import (
	"fmt"
	"util"
)

func extrapolateForward(numbers []int) int {
	lastNumbers := []int{}
	curr := numbers
	for {
		lastNumbers = append(lastNumbers, curr[len(curr)-1])
		nextCurr := []int{}
		allZeros := true
		for i := 0; i < len(curr)-1; i++ {
			diff := curr[i+1] - curr[i]
			if diff != 0 {
				allZeros = false
			}
			nextCurr = append(nextCurr, diff)
		}
		if allZeros {
			break
		}
		curr = nextCurr
	}

	currNum := 0
	for i := len(lastNumbers) - 1; i >= 0; i-- {
		currNum = currNum + lastNumbers[i]
	}

	return currNum
}

func extrapolateBackward(numbers []int) int {
	firstNumbers := []int{}
	curr := numbers
	for {
		firstNumbers = append(firstNumbers, curr[0])
		nextCurr := []int{}
		allZeros := true
		for i := 0; i < len(curr)-1; i++ {
			diff := curr[i+1] - curr[i]
			if diff != 0 {
				allZeros = false
			}
			nextCurr = append(nextCurr, diff)
		}
		if allZeros {
			break
		}
		curr = nextCurr
	}

	currNum := 0
	for i := len(firstNumbers) - 1; i >= 0; i-- {
		currNum = firstNumbers[i] - currNum
	}

	return currNum
}

func partOne(lines []string) error {
	result := 0
	for _, line := range lines {
		numbers := parseNumbers(line)
		result += extrapolateForward(numbers)
	}

	// answer: 1637452029
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	result := 0
	for _, line := range lines {
		numbers := parseNumbers(line)
		result += extrapolateBackward(numbers)
	}

	// answer: 908
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
