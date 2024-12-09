package main

import (
	"fmt"
	"util"
)

type grid struct {
	util.Grid
}

type point struct {
	i int
	j int
}

func (g *grid) frequencies() map[rune]([]point) {
	frequencies := make(map[rune]([]point))
	for i := 0; i < g.M; i++ {
		for j := 0; j < g.N; j++ {
			frequencies[g.Rows[i][j]] = append(frequencies[g.Rows[i][j]], point{i, j})
		}
	}
	delete(frequencies, '.')
	return frequencies
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	antinodes := make(map[point]struct{})
	for _, points := range grid.frequencies() {
		for i := 0; i < len(points); i++ {
			for j := i + 1; j < len(points); j++ {
				p1, p2 := points[i], points[j]
				di := p2.i - p1.i
				dj := p2.j - p1.j
				an1 := point{p1.i - di, p1.j - dj}
				an2 := point{p2.i + di, p2.j + dj}
				if grid.InBounds(an1.i, an1.j) {
					antinodes[an1] = struct{}{}
				}
				if grid.InBounds(an2.i, an2.j) {
					antinodes[an2] = struct{}{}
				}
			}
		}
	}

	result := len(antinodes)

	// answer: 379
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	antinodes := make(map[point]struct{})
	for _, points := range grid.frequencies() {
		for i := 0; i < len(points); i++ {
			for j := i + 1; j < len(points); j++ {
				p1, p2 := points[i], points[j]
				antinodes[p1] = struct{}{}
				antinodes[p2] = struct{}{}
				di := p2.i - p1.i
				dj := p2.j - p1.j
				curr := point{p1.i - di, p1.j - dj}
				for grid.InBounds(curr.i, curr.j) {
					antinodes[curr] = struct{}{}
					curr.i, curr.j = curr.i-di, curr.j-dj
				}
				curr = point{p2.i + di, p2.j + dj}
				for grid.InBounds(curr.i, curr.j) {
					antinodes[curr] = struct{}{}
					curr.i, curr.j = curr.i+di, curr.j+dj
				}
			}
		}
	}

	result := len(antinodes)

	// answer: 1339
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
