package main

import (
	"fmt"
	"util"
)

type dir string

const (
	up    dir = "U"
	down  dir = "D"
	left  dir = "L"
	right dir = "R"
)

func (d dir) next(i, j int) (ni, nj int) {
	switch d {
	case up:
		return i - 1, j
	case down:
		return i + 1, j
	case left:
		return i, j - 1
	case right:
		return i, j + 1
	}
	panic("unreachable")
}

type dig struct {
	direction dir
	amount    int
}

type point struct {
	i int
	j int
}

type grid struct {
	points map[point]struct{}
	minI   int
	minJ   int
	maxI   int
	maxJ   int
}

func (g grid) I() int {
	return g.maxI - g.minI + 1
}

func (g grid) J() int {
	return g.maxJ - g.minJ + 1
}

func (g grid) InBounds(i, j int) bool {
	return 0 <= i && i < g.maxI-g.minI+1 && 0 <= j && j < g.maxJ-g.minJ+1
}

type status int

const (
	unvisited status = 0
	dug       status = -1
	outside   status = 1
	inside    status = 2
)

func (g grid) dfs(i int, j int, fill status, state []([]status)) int {
	if state[i][j] != unvisited {
		return 0
	}
	state[i][j] = fill

	result := 1
	for _, pair := range [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		ni, nj := i+pair[0], j+pair[1]
		if g.InBounds(ni, nj) {
			result += g.dfs(ni, nj, fill, state)
		}
	}

	return result
}

func (g grid) lava() int {
	result := len(g.points) // include the perimeter in the final area

	state := make([]([]status), g.I())
	for i := 0; i < g.I(); i++ {
		state[i] = make([]status, g.J())
	}
	for pt := range g.points {
		state[pt.i-g.minI][pt.j-g.minJ] = dug
	}

	// dfs to fill in the outside of the trench
	// if the trench is a perfect square, nothing happens
	for i := 0; i < g.I(); i++ {
		if state[i][0] == unvisited {
			g.dfs(i, 0, outside, state)
		}
	}
	for i := 0; i < g.I(); i++ {
		if state[i][g.J()-1] == unvisited {
			g.dfs(i, g.J()-1, outside, state)
		}
	}
	for j := 0; j < g.J(); j++ {
		if state[0][j] == unvisited {
			g.dfs(0, j, outside, state)
		}
	}
	for j := 0; j < g.J(); j++ {
		if state[g.I()-1][j] == unvisited {
			g.dfs(g.I()-1, j, outside, state)
		}
	}

	// dfs a second time to compute the inside area
	for i := 0; i < g.I(); i++ {
		for j := 0; j < g.J(); j++ {
			if state[i][j] == unvisited {
				result += g.dfs(i, j, inside, state)
			}
		}
	}

	return result
}

func partOne(lines []string) error {
	digs := parseDigs(lines)
	grid := grid{points: map[point]struct{}{}}
	i, j := 0, 0
	for _, dig := range digs {
		for diff := 0; diff < dig.amount; diff++ {
			i, j = dig.direction.next(i, j)
			grid.points[point{i, j}] = struct{}{}
			grid.minI = min(grid.minI, i)
			grid.minJ = min(grid.minJ, j)
			grid.maxI = max(grid.maxI, i)
			grid.maxJ = max(grid.maxJ, j)
		}
	}

	// answer: 40714
	fmt.Println(grid.lava())

	return nil
}

func partTwo(lines []string) error {
	digs := parseHexDigs(lines)
	perimeter := 0
	endPoints := []point{}

	i, j := 0, 0
	for _, dig := range digs {
		for diff := 0; diff < dig.amount; diff++ {
			perimeter += 1
			i, j = dig.direction.next(i, j)
		}
		endPoints = append(endPoints, point{i, j})
	}

	// Shoelace formula - https://en.wikipedia.org/wiki/Shoelace_formula
	area := 0
	for i = 0; i < len(endPoints)-1; i++ {
		p1, p2 := endPoints[i], endPoints[i+1]
		area += (p1.i * p2.j) - (p2.i * p1.j)
	}
	p1, p2 := endPoints[len(endPoints)-1], endPoints[0]
	area += (p1.i * p2.j) - (p2.i * p1.j)
	area /= 2
	if area < 0 {
		area *= -1
	}

	// area is only the amount enclosed by the lines that go through the center of each cell
	// each cell is missing 1/4, 2/4, or 3/4 depending on what kind of turn the line is
	//   the amount of area missing is perimeter / 2
	// there are always 4 more clockwise turns than counterclockwise turns, since it's a closed loop
	//   4 * 1/4 = 1
	result := area + (perimeter / 2) + 1

	// answer: 129849166997110
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
