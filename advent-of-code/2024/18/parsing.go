package main

import (
	"strconv"
	"strings"
)

func parseBytes(lines []string) ([]point, error) {
	points := []point{}
	for _, line := range lines {
		nums := strings.Split(line, ",")
		i, err := strconv.Atoi(nums[0])
		if err != nil {
			return nil, err
		}
		j, err := strconv.Atoi(nums[1])
		if err != nil {
			return nil, err
		}
		points = append(points, point{i, j})
	}
	return points, nil
}
