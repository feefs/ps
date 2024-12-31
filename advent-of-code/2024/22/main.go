package main

import (
	"fmt"
	"strconv"
	"util"
)

func evolve(n int) int {
	n = n ^ (n * 64)
	n %= 16777216

	n = n ^ (n / 32)
	n %= 16777216

	n = n ^ (n * 2048)
	n %= 16777216

	return n
}

func prices(n int, changes int) []int {
	prices := []int{n % 10}
	for range changes {
		n = evolve(n)
		prices = append(prices, n%10)
	}
	return prices
}

func deltas(prices []int) []int {
	deltas := []int{}
	for i := 0; i < len(prices)-1; i++ {
		deltas = append(deltas, prices[i+1]-prices[i])
	}
	return deltas
}

type sequence struct {
	a int
	b int
	c int
	d int
}

func partOne(lines []string) error {
	result := 0
	for _, l := range lines {
		num, err := strconv.Atoi(l)
		if err != nil {
			return err
		}
		for range 2000 {
			num = evolve(num)
		}
		result += num
	}

	// answer: 12759339434
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	bananas := map[sequence]int{}
	for _, l := range lines {
		num, err := strconv.Atoi(l)
		if err != nil {
			return err
		}
		prices := prices(num, 2000)
		deltas := deltas(prices)
		seen := map[sequence]bool{}
		for i := 0; i < len(deltas)-4; i++ {
			seq := sequence{deltas[i], deltas[i+1], deltas[i+2], deltas[i+3]}
			if seen[seq] {
				continue
			}
			seen[seq] = true
			bananas[seq] += prices[i+4]
		}
	}

	result := 0
	for _, v := range bananas {
		if v > result {
			result = v
		}
	}

	// answer: 1405
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
