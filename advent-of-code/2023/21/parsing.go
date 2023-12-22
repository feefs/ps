package main

import "util"

func parseGrid(lines []string) grid {
	g := util.ParseGrid(lines)
	start := point{}
out:
	for i := 0; i < g.M; i++ {
		for j := 0; j < g.N; j++ {
			if g.Rows[i][j] == 'S' {
				start.i, start.j = i, j
				break out
			}
		}
	}

	return grid{g, start}
}
