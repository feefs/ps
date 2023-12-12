package main

import (
	"slices"
	"strings"
)

func emptyRows(lines []string) []int {
	result := []int{}
	for i, line := range lines {
		empty := true
		for _, r := range line {
			if r != '.' {
				empty = false
			}
		}
		if empty {
			result = append(result, i)
		}
	}
	return result
}

func emptyCols(lines []string) []int {
	m := len(lines)
	n := len(lines[0])
	result := []int{}
	for j := 0; j < n; j++ {
		empty := true
		for i := 0; i < m; i++ {
			if lines[i][j] != '.' {
				empty = false
			}
		}
		if empty {
			result = append(result, j)
		}
	}

	return result
}

func parseGrid(lines []string) grid {
	m, n := len(lines), len(lines[0])

	emptyRows := emptyRows(lines)
	emptyCols := emptyCols(lines)

	values := make([]([]rune), m)
	for j := 0; j < n; j++ {
		if slices.Contains(emptyCols, j) {
			for i := 0; i < m; i++ {
				values[i] = append(values[i], '.')
			}
		}
		for i := 0; i < m; i++ {
			values[i] = append(values[i], rune(lines[i][j]))
		}
	}

	values2 := []([]rune){}
	for i := 0; i < m; i++ {
		if slices.Contains(emptyRows, i) {
			values2 = append(values2, []rune(strings.Repeat(".", n+len(emptyCols))))
		}
		values2 = append(values2, values[i])
	}

	return grid{m: len(values2), n: len(values2[0]), values: values2}
}

func parseGalaxyGrid(lines []string) galaxyGrid {
	emptyRows := emptyRows(lines)
	emptyCols := emptyCols(lines)

	values := make([]([]rune), len(lines))
	for i, line := range lines {
		values[i] = []rune(line)
	}

	return galaxyGrid{
		m:         len(lines),
		n:         len(lines[0]),
		emptyRows: emptyRows,
		emptyCols: emptyCols,
		values:    values,
	}
}
