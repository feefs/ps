package main

import (
	"fmt"
	"strconv"
	"strings"
)

func parse(lines []string) ([]pageOrdering, []update, error) {
	pageOrderings := []pageOrdering{}
	updates := []update{}

	i := 0
	for {
		line := lines[i]
		if line == "" {
			i++
			break
		}

		split := strings.Split(line, "|")
		if len(split) != 2 {
			return nil, nil, fmt.Errorf("split isn't length 2: %v", split)
		}

		x, err := strconv.Atoi(split[0])
		if err != nil {
			return nil, nil, err
		}
		y, err := strconv.Atoi(split[1])
		if err != nil {
			return nil, nil, err
		}

		pageOrderings = append(pageOrderings, pageOrdering{x, y})
		i++
	}

	for i < len(lines) {
		line := lines[i]
		split := strings.Split(line, ",")
		pages := make([]int, len(split))
		for j, s := range split {
			page, err := strconv.Atoi(s)
			if err != nil {
				return nil, nil, err
			}
			pages[j] = page
		}
		updates = append(updates, update{pages})
		i++
	}

	return pageOrderings, updates, nil
}
