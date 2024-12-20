package main

import "util"

func parse(lines []string) (grid, []rune) {
	gridLines := []string{}
	moves := []string{}

	i := 0
	for {
		if lines[i] == "" {
			break
		}
		gridLines = append(gridLines, lines[i])
		i++
	}
	i++
	for i < len(lines) {
		moves = append(moves, lines[i])
		i++
	}

	allMoves := []rune{}
	for _, move := range moves {
		allMoves = append(allMoves, []rune(move)...)
	}

	g := util.ParseGrid(gridLines)
	robot := point{-1, -1}
out:
	for i := range g.M {
		for j := range g.N {
			if g.Rows[i][j] == '@' {
				robot.i, robot.j = i, j
				break out
			}
		}
	}

	return grid{g, robot}, allMoves
}
