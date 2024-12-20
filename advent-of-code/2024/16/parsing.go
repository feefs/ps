package main

import "util"

func parseGrid(lines []string) grid {
	g := util.ParseGrid(lines)
	start, end := point{}, point{}
	for i := range g.M {
		for j := range g.N {
			if g.Rows[i][j] == 'S' {
				start.i, start.j = i, j
			}
			if g.Rows[i][j] == 'E' {
				end.i, end.j = i, j
			}
		}
	}
	return grid{g, start, end}
}
