package main

import "util"

func parseGrid(lines []string) grid {
	g := util.ParseGrid(lines)

	intRows := make([]([]int), g.M)
	for i, row := range g.Rows {
		intRows[i] = make([]int, g.N)
		for j, r := range row {
			intRows[i][j] = int(r - '0')
		}
	}

	return grid{g, intRows}
}
