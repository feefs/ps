package main

import (
	"fmt"
	"iter"
	"math"
	"util"
)

type point struct {
	i int
	j int
}

type grid struct {
	util.Grid
	start point
	end   point
}

type elem struct {
	p           point
	picoseconds int
}

func (g grid) dists() map[point]int {
	dists := map[point]int{g.start: 0}
	seen := map[point]bool{}
	q := []elem{{g.start, 0}}
	for len(q) > 0 {
		curr := q[0]
		q = q[1:]
		if seen[curr.p] {
			continue
		}
		seen[curr.p] = true
		dists[curr.p] = curr.picoseconds
		for _, dir := range util.CardinalDirs() {
			ni, nj := curr.p.i+dir.Dx, curr.p.j+dir.Dy
			if !g.InBounds(ni, nj) || g.Rows[ni][nj] == '#' {
				continue
			}
			q = append(q, elem{point{ni, nj}, curr.picoseconds + 1})
		}
	}
	return dists
}

// yields pairs of points p1 and p2, where dists[p1] <= dists[p2]
func pairs(dists map[point]int) iter.Seq2[point, point] {
	points := []point{}
	for p := range dists {
		points = append(points, p)
	}
	return func(yield func(point, point) bool) {
		for i := range len(points) {
			for j := i; j < len(points); j++ {
				p1, p2 := points[i], points[j]
				d1, d2 := dists[p1], dists[p2]
				if d1 > d2 {
					p1, p2 = p2, p1
				}
				if !yield(p1, p2) {
					return
				}
			}
		}
	}
}

func manhattanDistance(p1 point, p2 point) int {
	return int(math.Abs(float64(p1.i-p2.i)) + math.Abs(float64(p1.j-p2.j)))
}

func partOne(lines []string) error {
	grid := parseGrid(lines)
	dists := grid.dists()

	result := 0
	for p1, p2 := range pairs(dists) {
		md := manhattanDistance(p1, p2)
		if md <= 2 && dists[p2]-dists[p1]-md >= 100 {
			result += 1
		}
	}

	// answer: 1452
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)
	dists := grid.dists()

	result := 0
	for p1, p2 := range pairs(dists) {
		md := manhattanDistance(p1, p2)
		if md <= 20 && dists[p2]-dists[p1]-md >= 100 {
			result += 1
		}
	}

	// answer: 999556
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
