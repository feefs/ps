package main

import (
	"fmt"
	"strings"
	"util"
)

type grid struct {
	m    int
	n    int
	rows []([]rune)
}

func (g grid) String() string {
	builder := strings.Builder{}

	for _, row := range g.rows {
		for _, r := range row {
			builder.WriteRune(r)
		}
		builder.WriteRune('\n')
	}

	return builder.String()
}

func (g grid) tiltNorth() {
	for j := 0; j < g.n; j++ {
		for i := 0; i < g.m; i++ {
			if g.rows[i][j] == 'O' {
				for i2 := i - 1; i2 >= 0; i2-- {
					if g.rows[i2][j] != '.' {
						break
					}
					g.rows[i2][j], g.rows[i2+1][j] = g.rows[i2+1][j], g.rows[i2][j]
				}
			}
		}
	}
}

func (g grid) tiltWest() {
	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if g.rows[i][j] == 'O' {
				for j2 := j - 1; j2 >= 0; j2-- {
					if g.rows[i][j2] != '.' {
						break
					}
					g.rows[i][j2], g.rows[i][j2+1] = g.rows[i][j2+1], g.rows[i][j2]
				}
			}
		}
	}
}

func (g grid) tiltEast() {
	for i := 0; i < g.m; i++ {
		for j := g.n - 1; j >= 0; j-- {
			if g.rows[i][j] == 'O' {
				for j2 := j + 1; j2 < g.n; j2++ {
					if g.rows[i][j2] != '.' {
						break
					}
					g.rows[i][j2], g.rows[i][j2-1] = g.rows[i][j2-1], g.rows[i][j2]
				}
			}
		}
	}

}

func (g grid) tiltSouth() {
	for j := 0; j < g.n; j++ {
		for i := g.m - 1; i >= 0; i-- {
			if g.rows[i][j] == 'O' {
				for i2 := i + 1; i2 < g.m; i2++ {
					if g.rows[i2][j] != '.' {
						break
					}
					g.rows[i2][j], g.rows[i2-1][j] = g.rows[i2-1][j], g.rows[i2][j]
				}
			}
		}
	}
}

func (g grid) load() int {
	result := 0

	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if g.rows[i][j] == 'O' {
				result += g.m - i
			}
		}
	}

	return result
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	grid.tiltNorth()

	// answer: 113424
	fmt.Println(grid.load())

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	grids := map[string]int{grid.String(): 0}
	i := 0
	for i < 1_000_000_000 {
		grid.tiltNorth()
		grid.tiltWest()
		grid.tiltSouth()
		grid.tiltEast()

		if prevIndex, ok := grids[grid.String()]; ok {
			cycleLength := i - prevIndex
			for i < 1_000_000_000-cycleLength {
				i += cycleLength
			}
		} else {
			grids[grid.String()] = i
		}

		i += 1
	}

	// answer: 96003
	fmt.Println(grid.load())

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
