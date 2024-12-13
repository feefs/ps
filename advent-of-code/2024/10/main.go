package main

import (
	"fmt"
	"strconv"
	"util"
)

type grid struct {
	util.Grid
}

type point struct {
	i int
	j int
}

func (g *grid) dfs(i int, j int, targetHeight int, seen map[point]bool, trailheads map[point]struct{}) (int, error) {
	height, err := strconv.Atoi(string(g.Rows[i][j]))
	if err != nil {
		return 0, err
	}
	if seen[point{i, j}] || height != targetHeight {
		return 0, nil
	}
	if height == 9 {
		trailheads[point{i, j}] = struct{}{}
		return 1, nil
	}

	seen[point{i, j}] = true
	result := 0
	for _, dir := range util.CardinalDirs() {
		ni, nj := i+dir.Dx, j+dir.Dy
		if g.InBounds(ni, nj) {
			paths, err := g.dfs(ni, nj, targetHeight+1, seen, trailheads)
			if err != nil {
				return 0, err
			}
			result += paths
		}
	}
	seen[point{i, j}] = false

	return result, nil
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	result := 0
	for i := 0; i < grid.M; i++ {
		for j := 0; j < grid.N; j++ {
			trailheads := make(map[point]struct{})
			_, err := grid.dfs(i, j, 0, make(map[point]bool), trailheads)
			if err != nil {
				return err
			}
			result += len(trailheads)
		}
	}

	// answer: 482
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	result := 0
	for i := 0; i < grid.M; i++ {
		for j := 0; j < grid.N; j++ {
			rating, err := grid.dfs(i, j, 0, make(map[point]bool), make(map[point]struct{}))
			if err != nil {
				return err
			}
			result += rating
		}
	}

	// answer: 1094
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
