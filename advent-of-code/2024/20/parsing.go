package main

import "util"

func parseGrid(lines []string) grid {
	grid := grid{util.ParseGrid(lines), point{}, point{}}
	for i := range grid.M {
		for j := range grid.N {
			if grid.Rows[i][j] == 'S' {
				grid.start = point{i, j}
			}
			if grid.Rows[i][j] == 'E' {
				grid.end = point{i, j}
			}
		}
	}
	return grid
}
