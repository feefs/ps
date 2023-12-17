package main

import (
	"fmt"
	"util"
)

type grid struct {
	util.Grid
}

type dir int

const (
	up dir = iota
	down
	left
	right
)

type beam struct {
	i       int
	j       int
	fromDir dir
}

func (b beam) nextBeams(g grid) []beam {
	result := []beam{}
	i, j := b.i, b.j

	var nFromDir dir
	ni, nj := -1, -1
	switch g.Rows[i][j] {
	case '.':
		switch b.fromDir {
		case up:
			ni, nj = i+1, j
		case down:
			ni, nj = i-1, j
		case left:
			ni, nj = i, j+1
		case right:
			ni, nj = i, j-1
		}
		if g.InBounds(ni, nj) {
			result = append(result, beam{i: ni, j: nj, fromDir: b.fromDir})
		}
	case '/':
		switch b.fromDir {
		case up:
			nFromDir = right
			ni, nj = i, j-1
		case down:
			nFromDir = left
			ni, nj = i, j+1
		case left:
			nFromDir = down
			ni, nj = i-1, j
		case right:
			nFromDir = up
			ni, nj = i+1, j
		}
		if g.InBounds(ni, nj) {
			result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
		}
	case '\\':
		switch b.fromDir {
		case up:
			nFromDir = left
			ni, nj = i, j+1
		case down:
			nFromDir = right
			ni, nj = i, j-1
		case left:
			nFromDir = up
			ni, nj = i+1, j
		case right:
			nFromDir = down
			ni, nj = i-1, j
		}
		if g.InBounds(ni, nj) {
			result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
		}
	case '|':
		switch b.fromDir {
		case up:
			ni, nj = i+1, j
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: b.fromDir})
			}
		case down:
			ni, nj = i-1, j
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: b.fromDir})
			}
		case left, right:
			nFromDir = down
			ni, nj = i-1, j
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
			}
			nFromDir = up
			ni, nj = i+1, j
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
			}
		}
	case '-':
		switch b.fromDir {
		case up, down:
			nFromDir = right
			ni, nj = i, j-1
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
			}
			nFromDir = left
			ni, nj = i, j+1
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: nFromDir})
			}
		case left:
			ni, nj = i, j+1
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: b.fromDir})
			}
		case right:
			ni, nj = i, j-1
			if g.InBounds(ni, nj) {
				result = append(result, beam{i: ni, j: nj, fromDir: b.fromDir})
			}
		}
	}

	return result
}

// returns how many tiles are energized when shining a beam
func (g grid) shine(b beam, visited []([](map[dir]struct{}))) int {
	i, j := b.i, b.j
	if _, ok := visited[i][j][b.fromDir]; ok {
		return 0
	}

	result := 0
	// only count tile being energized once, since beams from different directions can energize the same tile
	if len(visited[i][j]) == 0 {
		result += 1
	}
	visited[i][j][b.fromDir] = struct{}{}

	for _, nextBeam := range b.nextBeams(g) {
		result += g.shine(nextBeam, visited)
	}

	return result
}

func newVisited(m, n int) []([]map[dir]struct{}) {
	result := make([]([]map[dir]struct{}), m)
	for i := 0; i < m; i++ {
		result[i] = make([]map[dir]struct{}, n)
		for j := 0; j < n; j++ {
			result[i][j] = make(map[dir]struct{})
		}
	}

	return result
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	visited := newVisited(grid.M, grid.N)
	result := grid.shine(beam{0, 0, left}, visited)

	// answer: 7884
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	result := 0
	for i := 0; i < grid.M; i++ {
		visited := newVisited(grid.M, grid.N)
		result = max(result, grid.shine(beam{i, 0, left}, visited))
	}
	for i := 0; i < grid.M; i++ {
		visited := newVisited(grid.M, grid.N)
		result = max(result, grid.shine(beam{i, grid.N - 1, right}, visited))
	}
	for j := 0; j < grid.N; j++ {
		visited := newVisited(grid.M, grid.N)
		result = max(result, grid.shine(beam{0, j, up}, visited))
	}
	for j := 0; j < grid.N; j++ {
		visited := newVisited(grid.M, grid.N)
		result = max(result, grid.shine(beam{grid.M - 1, j, down}, visited))
	}

	// answer: 8185
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
