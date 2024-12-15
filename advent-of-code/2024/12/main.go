package main

import (
	"fmt"
	"util"
)

type point struct {
	i int
	j int
}

type grid struct {
	util.Grid
	component     map[int](map[int]int)
	numComponents int
}

func (g *grid) fence() {
	var dfs func(i int, j int, seen map[point]struct{}, plantType rune, component int)
	dfs = func(i int, j int, seen map[point]struct{}, plantType rune, component int) {
		p := point{i, j}
		if _, ok := seen[p]; ok {
			return
		}
		if g.Rows[i][j] != plantType {
			return
		}
		seen[p] = struct{}{}
		g.component[i][j] = component
		for _, dir := range util.CardinalDirs() {
			ni, nj := i+dir.Dx, j+dir.Dy
			if g.InBounds(ni, nj) {
				dfs(ni, nj, seen, plantType, component)
			}
		}
	}

	component := 0
	for i := range g.M {
		for j := range g.N {
			if g.component[i][j] == -1 {
				dfs(i, j, make(map[point]struct{}), g.Rows[i][j], component)
				component += 1
				g.numComponents += 1
			}
		}
	}
}

func partOne(lines []string) error {
	grid := parseGrid(lines)
	grid.fence()

	result := 0
	for c := range grid.numComponents {
		area := 0
		perimeter := 0
		for i := range grid.M {
			for j := range grid.N {
				if grid.component[i][j] != c {
					continue
				}
				area += 1
				for _, dir := range util.CardinalDirs() {
					ni, nj := i+dir.Dx, j+dir.Dy
					if grid.InBounds(ni, nj) {
						if grid.component[ni][nj] != c {
							perimeter += 1
						}
					} else {
						perimeter += 1
					}
				}
			}
		}
		result += area * perimeter
	}

	// answer: 1494342
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)
	grid.fence()

	result := 0
	for c := range grid.numComponents {
		area := 0
		corners := 0
		for i := range grid.M {
			for j := range grid.N {
				if grid.component[i][j] != c {
					continue
				}
				area += 1

				northDifferent := !grid.InBounds(i-1, j) || grid.component[i-1][j] != c
				northwestDifferent := !grid.InBounds(i-1, j-1) || grid.component[i-1][j-1] != c
				westDifferent := !grid.InBounds(i, j-1) || grid.component[i][j-1] != c
				southwestDifferent := !grid.InBounds(i+1, j-1) || grid.component[i+1][j-1] != c
				southDifferent := !grid.InBounds(i+1, j) || grid.component[i+1][j] != c
				southeastDifferent := !grid.InBounds(i+1, j+1) || grid.component[i+1][j+1] != c
				eastDifferent := !grid.InBounds(i, j+1) || grid.component[i][j+1] != c
				northeastDifferent := !grid.InBounds(i-1, j+1) || grid.component[i-1][j+1] != c

				if northDifferent && eastDifferent {
					// convex corner
					corners += 1
				}
				if northeastDifferent && !northDifferent && !eastDifferent {
					// concave corner
					corners += 1
				}

				if northDifferent && westDifferent {
					// convex corner
					corners += 1
				}
				if northwestDifferent && !northDifferent && !westDifferent {
					// concave corner
					corners += 1
				}

				if southDifferent && westDifferent {
					// convex corner
					corners += 1
				}
				if southwestDifferent && !southDifferent && !westDifferent {
					// concave corner
					corners += 1
				}

				if southDifferent && eastDifferent {
					// convex corner
					corners += 1
				}
				if southeastDifferent && !southDifferent && !eastDifferent {
					// concave corner
					corners += 1
				}
			}
		}
		result += area * corners
	}

	// answer: 893676
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
