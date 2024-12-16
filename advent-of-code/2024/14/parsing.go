package main

import (
	"regexp"
	"strconv"
	"util"
)

func parseRobots(lines []string) ([]robot, error) {
	robots := []robot{}
	r := regexp.MustCompile(`p=(-?\d+),(-?\d+)\sv=(-?\d+),(-?\d+)`)
	for _, line := range lines {
		match := r.FindStringSubmatch(line)
		if len(match) != 5 {
			return nil, util.InvalidStateError("match isn't len 4: %v", match)
		}
		posX, err := strconv.Atoi(match[1])
		if err != nil {
			return nil, err
		}
		posY, err := strconv.Atoi(match[2])
		if err != nil {
			return nil, err
		}
		velX, err := strconv.Atoi(match[3])
		if err != nil {
			return nil, err
		}
		velY, err := strconv.Atoi(match[4])
		if err != nil {
			return nil, err
		}
		robots = append(robots, robot{
			position{posX, posY},
			velocity{velX, velY},
		})
	}
	return robots, nil
}
