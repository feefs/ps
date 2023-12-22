package main

import (
	"fmt"
	"util"
)

type grid struct {
	util.Grid
	start point
}

type point struct {
	i int
	j int
}

func (g grid) nextPoints(p point) []point {
	result := []point{}
	for _, change := range []([]int){{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		ni, nj := p.i+change[0], p.j+change[1]
		if g.InBounds(ni, nj) && g.Rows[ni][nj] != '#' {
			result = append(result, point{ni, nj})
		}
	}

	return result
}

func (g grid) nextInfinitePoints(p point) []point {
	result := []point{}
	for _, change := range []([]int){{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
		ni, nj := p.i+change[0], p.j+change[1]
		if g.Rows[((ni%g.M)+g.M)%g.M][((nj%g.N)+g.N)%g.N] != '#' {
			result = append(result, point{ni, nj})
		}
	}

	return result
}

func (g grid) plots(steps int, nextFunction func(point) []point) int {
	q := []point{g.start}
	for len(q) > 0 {
		if steps == 0 {
			return len(q)
		}

		nextQSet := map[point]struct{}{}
		for len(q) > 0 {
			curr := q[0]
			q = q[1:]
			for _, pt := range nextFunction(curr) {
				nextQSet[pt] = struct{}{}
			}
		}

		nextQ := []point{}
		for pt := range nextQSet {
			nextQ = append(nextQ, pt)
		}

		steps -= 1
		q = nextQ
	}

	panic("unreachable")
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	// answer: 3776
	fmt.Println(grid.plots(64, grid.nextPoints))

	return nil
}

func partTwo(lines []string) error {
	/*
		fit a degree 2 polynomial with 3 points
		ax^2 + bx + c

		f(x = 0) = f(65) = f0
		f(x = 1) = f(65 + 131) = f1
		f(x = 2) = f(65 + (131 * 2)) = f2

		c = f0
		a + b + f0 = f1
		4a + 2b + f0 = f2

		a + b = f1 - f0 = g0
		4a + 2b = f2 - f0 = g1

		a = (g1 - 2g0) / 2
		b = g0 - a

		f(26501365) = f(65 + (x * 131))
		=>  x = 202300
	*/
	grid := parseGrid(lines)

	f0 := float64(grid.plots(65+(131*0), grid.nextInfinitePoints)) // x = 0
	f1 := float64(grid.plots(65+(131*1), grid.nextInfinitePoints)) // x = 1
	f2 := float64(grid.plots(65+(131*2), grid.nextInfinitePoints)) // x = 2

	g0 := f1 - f0
	g1 := f2 - f0

	c := f0
	a := (g1 - (2 * g0)) / 2
	b := g0 - a

	x := 202300.0

	result := (a * (x * x)) + (b * x) + c

	// answer: 625587097150084
	fmt.Println(int(result))

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
