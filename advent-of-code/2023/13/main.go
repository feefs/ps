package main

import (
	"fmt"
	"util"
)

type grid struct {
	m    int
	n    int
	rows []([]rune)
}

func (g grid) verticalLineOfReflectionScore(differences int) int {
	for j := 0; j < g.n-1; j++ {
		left, right := j, j+1
		diff := 0
		// check columns expanding left and right from j and j + 1
		for 0 <= left && right < g.n {
			for i := 0; i < g.m; i++ {
				if g.rows[i][left] != g.rows[i][right] {
					diff += 1
				}
			}
			left, right = left-1, right+1
		}
		// columns j and j + 1 form a vertical line of reflection with exactly diff differences
		if diff == differences {
			// if it exists, there is exactly one possible vertical line of reflection
			return (j + 1)
		}
	}

	return 0
}

func (g grid) horizontalLineOfReflectionScore(differences int) int {
	for i := 0; i < g.m-1; i++ {
		up, down := i, i+1
		diff := 0
		// check rows expanding up and down from i and i + 1
		for 0 <= up && down < g.m {
			for j := 0; j < g.n; j++ {
				if g.rows[up][j] != g.rows[down][j] {
					diff += 1
				}
			}
			up, down = up-1, down+1
		}
		// rows i and i + 1 form a horizontal line of reflection with exactly diff differences
		if diff == differences {
			// if it exists, there is exactly one possible horizontal line of reflection
			return 100 * (i + 1)
		}
	}

	return 0
}

func partOne(lines []string) error {
	grids := parseGrids(lines)

	result := 0
	for _, grid := range grids {
		result += grid.verticalLineOfReflectionScore(0)
		result += grid.horizontalLineOfReflectionScore(0)
	}

	// answer: 32723
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grids := parseGrids(lines)

	result := 0
	for _, grid := range grids {
		result += grid.verticalLineOfReflectionScore(1)
		result += grid.horizontalLineOfReflectionScore(1)
	}

	// answer: 34536
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
