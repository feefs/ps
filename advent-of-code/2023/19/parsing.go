package main

import (
	"regexp"
	"strconv"
)

func parse(lines []string) (map[target]workflow, []part) {
	workflows, parts := map[target]workflow{}, []part{}
	r := regexp.MustCompile(`(\w+){(.+)}`)
	innerR := regexp.MustCompile(`([^,]+)+`)
	stepR := regexp.MustCompile(`(\w)([>|<])(\d+):(\w+)`)

	lIndex := 0
	for lIndex < len(lines) {
		line := lines[lIndex]
		if line == "" {
			lIndex += 1
			break
		}

		match := r.FindStringSubmatch(line)
		innerMatch := innerR.FindAllStringSubmatch(match[2], -1)
		steps := []step{}
		for _, im := range innerMatch {
			stepMatch := stepR.FindStringSubmatch(im[1])
			if len(stepMatch) > 0 {
				n, _ := strconv.Atoi(stepMatch[3])
				steps = append(steps, step{
					cat: category(stepMatch[1]),
					op:  operation(stepMatch[2]),
					val: n,
					tg:  target(stepMatch[4]),
				})
			} else {
				steps = append(steps, step{tg: target(im[1])})
			}
		}
		workflows[target(match[1])] = workflow{steps}

		lIndex += 1
	}

	ratingR := regexp.MustCompile(`(\d+)+`)
	for lIndex < len(lines) {
		line := lines[lIndex]
		match := ratingR.FindAllString(line, -1)
		x, _ := strconv.Atoi(match[0])
		m, _ := strconv.Atoi(match[1])
		a, _ := strconv.Atoi(match[2])
		s, _ := strconv.Atoi(match[3])
		parts = append(parts, part{map[category]int{
			extremely:   x,
			musical:     m,
			aerodynamic: a,
			shiny:       s,
		}})
		lIndex += 1
	}

	return workflows, parts
}
