package main

import "util"

func parseGrid(lines []string) grid {
	g := util.ParseGrid(lines)
	parent := make(map[int](map[int]int), g.M)
	for i := range g.M {
		parent[i] = make(map[int]int, g.N)
		for j := range g.N {
			parent[i][j] = -1
		}
	}
	return grid{g, parent, 0}
}
