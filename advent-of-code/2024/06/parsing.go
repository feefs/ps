package main

import (
	"errors"
	"util"
)

func parseGrid(lines []string) (grid, error) {
	g := util.ParseGrid(lines)
	startDirs := map[rune]util.Dir{
		'^': {Dx: -1, Dy: 0},
		'<': {Dx: 0, Dy: -1},
		'v': {Dx: 1, Dy: 0},
		'>': {Dx: 0, Dy: 1},
	}
	for i := 0; i < g.M; i++ {
		for j := 0; j < g.N; j++ {
			if dir, ok := startDirs[g.Rows[i][j]]; ok {
				return grid{g, point{i, j}, dir}, nil
			}
		}
	}
	return grid{}, errors.New("starting point not found")
}
