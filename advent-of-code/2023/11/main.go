package main

import (
	"fmt"
	"math"
	"slices"
	"util"
)

type grid struct {
	m      int
	n      int
	values []([]rune)
}

type point struct {
	i int
	j int
}

func (p point) manhattanDistance(p2 point) int {
	return int(math.Abs(float64(p.i)-float64(p2.i)) + math.Abs(float64(p.j)-float64(p2.j)))
}

func (g grid) points() []point {
	result := []point{}
	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if g.values[i][j] == '#' {
				result = append(result, point{i, j})
			}
		}
	}

	return result
}

type galaxyGrid struct {
	m         int
	n         int
	emptyRows []int
	emptyCols []int
	values    []([]rune)
}

func (g galaxyGrid) points() []point {
	result := []point{}
	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if g.values[i][j] == '#' {
				result = append(result, point{i, j})
			}
		}
	}

	return result
}

func (g galaxyGrid) galaxyDistance(p point, p2 point) int {
	i1, i2 := p.i, p2.i
	if i1 > i2 {
		i1, i2 = i2, i1
	}
	j1, j2 := p.j, p2.j
	if j1 > j2 {
		j1, j2 = j2, j1
	}

	iDistance := 0
	for i := i1; i < i2; i++ {
		if slices.Contains(g.emptyRows, i) {
			iDistance += 1_000_000
		} else {
			iDistance += 1
		}
	}

	jDistance := 0
	for j := j1; j < j2; j++ {
		if slices.Contains(g.emptyCols, j) {
			jDistance += 1_000_000
		} else {
			jDistance += 1
		}
	}

	return iDistance + jDistance
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	result := 0
	points := grid.points()
	for i := 0; i < len(points); i++ {
		for j := i; j < len(points); j++ {
			result += points[i].manhattanDistance(points[j])
		}
	}

	// answer: 9965032
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGalaxyGrid(lines)

	result := 0
	points := grid.points()
	for i := 0; i < len(points); i++ {
		for j := i; j < len(points); j++ {
			result += grid.galaxyDistance(points[i], points[j])
		}
	}

	// answer: 550358864332
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
