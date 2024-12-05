package main

import (
	"fmt"
	"util"
)

type grid struct {
	util.Grid
}

func (g *grid) dfs(i int, j int, word string, dir util.Dir) int {
	if len(word) == 1 && rune(word[0]) == g.Rows[i][j] {
		return 1
	} else if rune(word[0]) != g.Rows[i][j] {
		return 0
	}

	result := 0
	ni, nj := i+dir.Dx, j+dir.Dy
	if g.InBounds(ni, nj) {
		result += g.dfs(ni, nj, word[1:], dir)
	}

	return result
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	result := 0
	for i := 0; i < grid.M; i++ {
		for j := 0; j < grid.N; j++ {
			for _, dir := range util.AllDirs() {
				result += grid.dfs(i, j, "XMAS", dir)
			}
		}
	}

	// answer: 2569
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	centerPoints := make(map[int](map[int]int), grid.M)
	for i := 0; i < grid.M; i++ {
		centerPoints[i] = make(map[int]int, grid.N)
		for j := 0; j < grid.N; j++ {
			centerPoints[i][j] = 0
		}
	}

	for i := 0; i < grid.M; i++ {
		for j := 0; j < grid.N; j++ {
			for _, dir := range util.IntercardinalDirs() {
				if grid.dfs(i, j, "MAS", dir) == 1 {
					centerPoints[i+dir.Dx][j+dir.Dy] += 1
				}
			}
		}
	}

	result := 0
	for i := 0; i < grid.M; i++ {
		for j := 0; j < grid.N; j++ {
			if centerPoints[i][j] == 2 {
				result += 1
			}
		}
	}

	// answer: 1998
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
