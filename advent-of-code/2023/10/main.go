package main

import (
	"bytes"
	"fmt"
	"strings"
	"util"
)

type grid struct {
	m        int
	n        int
	startRow int
	startCol int
	values   []([]rune)
}

const (
	vertical   = '|'
	horizontal = '-'
	northeast  = 'L'
	northwest  = 'J'
	southwest  = '7'
	southeast  = 'F'
)

var remappings = map[rune]rune{
	vertical:   '│',
	horizontal: '─',
	northeast:  '└',
	northwest:  '┘',
	southwest:  '┐',
	southeast:  '┌',
}

func (g grid) String() string {
	builder := strings.Builder{}
	for _, row := range g.values {
		buffer := bytes.Buffer{}
		for _, r := range row {
			if r2, ok := remappings[r]; ok {
				buffer.WriteRune(r2)
			} else {
				buffer.WriteRune(r)
			}
		}
		builder.WriteString(buffer.String())
		builder.WriteRune('\n')
	}

	return builder.String()
}

var neighborMappings = map[rune]([]([]int)){
	vertical:   {{-1, 0}, {1, 0}},
	horizontal: {{0, 1}, {0, -1}},
	northeast:  {{-1, 0}, {0, 1}},
	northwest:  {{-1, 0}, {0, -1}},
	southwest:  {{1, 0}, {0, -1}},
	southeast:  {{1, 0}, {0, 1}},
}

// returns the rune of the starting point converted to a pipe
func (g grid) startRune() rune {
	leftIncoming := false
	ni, nj := g.startRow, g.startCol-1
	if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
		r := g.values[ni][nj]
		if r == horizontal || r == northeast || r == southeast {
			leftIncoming = true
		}
	}

	rightIncoming := false
	ni, nj = g.startRow, g.startCol+1
	if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
		r := g.values[ni][nj]
		if r == horizontal || r == northwest || r == southwest {
			rightIncoming = true
		}
	}

	topIncoming := false
	ni, nj = g.startRow-1, g.startCol
	if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
		r := g.values[ni][nj]
		if r == vertical || r == southeast || r == southwest {
			topIncoming = true
		}
	}

	botIncoming := false
	ni, nj = g.startRow+1, g.startCol
	if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
		r := g.values[ni][nj]
		if r == vertical || r == northeast || r == northwest {
			botIncoming = true
		}
	}

	if leftIncoming && rightIncoming {
		return horizontal
	} else if topIncoming && botIncoming {
		return vertical
	} else if topIncoming && leftIncoming {
		return northwest
	} else if topIncoming && rightIncoming {
		return northeast
	} else if botIncoming && leftIncoming {
		return southwest
	} else {
		return southeast
	}
}

func (g grid) neighbors(i int, j int) []([]int) {
	neighbors := []([]int){}

	r := g.values[i][j]
	if i == g.startRow && j == g.startCol {
		r = g.startRune()
	}
	candidates, ok := neighborMappings[r]
	if !ok {
		panic(util.InvalidStateError(fmt.Sprintf("rune: %v", string(r))))
	}

	for _, cand := range candidates {
		ni, nj := i+cand[0], j+cand[1]
		if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
			neighbors = append(neighbors, []int{ni, nj})
		}
	}

	return neighbors
}

func (g grid) loopLength(i int, j int, visited [][]bool) int {
	if visited[i][j] {
		return 0
	}
	visited[i][j] = true
	result := 0
	for _, neb := range g.neighbors(i, j) {
		ni, nj := neb[0], neb[1]
		result = max(result, g.loopLength(ni, nj, visited))
	}

	return 1 + result
}

type point struct {
	i int
	j int
}

func (g grid) loopPoints() map[point]struct{} {
	visited := make([]([]bool), g.m)
	for i := 0; i < g.m; i++ {
		visited[i] = make([]bool, g.n)
	}

	_ = g.loopLength(g.startRow, g.startCol, visited)

	result := map[point]struct{}{}
	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if visited[i][j] {
				result[point{i, j}] = struct{}{}
			}
		}
	}

	return result
}

// count the number of times a ray casted from a point crosses a point on the loop
func (g grid) enclosed(i int, j int, points map[point]struct{}) bool {
	crosses := 0
	// cast ray northwest (up and to the left)
	for i >= 0 && j >= 0 {
		if _, ok := points[point{i, j}]; ok {
			r := g.values[i][j]
			// dont count the edge corners on the loop
			if r != northeast && r != southwest {
				crosses += 1
			}
		}
		i -= 1
		j -= 1
	}

	// if the ray crosses a point on the loop an odd number of times, the point is enclosed
	return crosses%2 == 1
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	visited := make([]([]bool), grid.m)
	for i := 0; i < grid.m; i++ {
		visited[i] = make([]bool, grid.n)
	}

	result := grid.loopLength(grid.startRow, grid.startCol, visited) / 2

	fmt.Println(grid)

	// answer: 6714
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	points := grid.loopPoints()

	result := 0
	for i := 0; i < grid.m; i++ {
		for j := 0; j < grid.n; j++ {
			if _, ok := points[point{i, j}]; !ok {
				if grid.enclosed(i, j, points) {
					result += 1
					grid.values[i][j] = 'I'
				} else {
					grid.values[i][j] = 'O'
				}
			}
		}
	}

	fmt.Println(grid)

	// answer: 429
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
