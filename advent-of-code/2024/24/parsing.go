package main

import (
	"regexp"
	"slices"
	"strconv"
)

func parseCircuit(lines []string) circuit {
	elements := map[wire]any{}
	r := regexp.MustCompile(`(\w+): (\d)`)
	i := 0
	for {
		line := lines[i]
		if line == "" {
			break
		}
		match := r.FindStringSubmatch(line)
		w := wire(match[1])
		value, _ := strconv.Atoi(match[2])
		elements[w] = input{value}
		i++
	}

	i++

	zWires := []wire{}
	r2 := regexp.MustCompile(`(\w+) (\w+) (\w+) -> (\w+)`)
	for i < len(lines) {
		line := lines[i]
		match := r2.FindStringSubmatch(line)
		i1, i2 := wire(match[1]), wire(match[3])
		var variant variant
		switch match[2] {
		case "AND":
			variant = and
		case "OR":
			variant = or
		case "XOR":
			variant = xor
		}
		output := wire(match[4])
		elements[output] = gate{[2]wire{i1, i2}, variant}
		if output[0] == 'z' {
			zWires = append(zWires, output)
		}
		i++
	}

	slices.Sort(zWires)

	return circuit{elements, zWires}
}
