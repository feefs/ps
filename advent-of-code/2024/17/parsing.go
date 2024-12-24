package main

import (
	"regexp"
	"strconv"
)

func parseComputer(lines []string) *computer {
	r := regexp.MustCompile(`(\d+)`)

	registerA := r.FindString(lines[0])
	A, _ := strconv.Atoi(registerA)
	registerB := r.FindString(lines[1])
	B, _ := strconv.Atoi(registerB)
	registerC := r.FindString(lines[2])
	C, _ := strconv.Atoi(registerC)

	nums := r.FindAllString(lines[4], -1)
	instructions := make([]int, len(nums))
	for i, n := range nums {
		inst, _ := strconv.Atoi(n)
		instructions[i] = inst
	}

	return &computer{A, B, C, instructions, 0}
}
