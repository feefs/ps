package main

import (
	"fmt"
	"slices"
	"util"
)

type point struct {
	i int
	j int
}

type grid struct {
	util.Grid
}

func (g grid) longestHike(p point, used map[point]struct{}, results *[]int) {
	i, j := p.i, p.j
	if i == g.M-1 && j == g.N-2 {
		*results = append(*results, len(used))
	}

	if _, ok := used[p]; ok {
		return
	}
	used[p] = struct{}{}

	diffs := []([]int){}
	switch g.Rows[i][j] {
	case '^':
		diffs = append(diffs, []int{-1, 0})
	case 'v':
		diffs = append(diffs, []int{1, 0})
	case '<':
		diffs = append(diffs, []int{0, -1})
	case '>':
		diffs = append(diffs, []int{0, 1})
	default:
		diffs = []([]int){{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	}

	for _, diff := range diffs {
		ni, nj := i+diff[0], j+diff[1]
		if !g.InBounds(ni, nj) {
			continue
		}
		if g.Rows[ni][nj] == '#' {
			continue
		}

		g.longestHike(point{ni, nj}, used, results)
	}

	delete(used, p)
}

func (g grid) contractedEdges() map[point](map[point]int) {
	allEdges := map[point](map[point]int){}
	for i := 0; i < g.M; i++ {
		for j := 0; j < g.N; j++ {
			if g.Rows[i][j] == '#' {
				continue
			}

			for _, diff := range []([]int){{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				ni, nj := i+diff[0], j+diff[1]
				if !g.InBounds(ni, nj) {
					continue
				}
				if g.Rows[ni][nj] == '#' {
					continue
				}

				p := point{i, j}
				if _, ok := allEdges[p]; !ok {
					allEdges[p] = make(map[point]int)
				}
				np := point{ni, nj}
				if _, ok := allEdges[np]; !ok {
					allEdges[np] = make(map[point]int)
				}
				allEdges[p][np] = 1
				allEdges[np][p] = 1
			}
		}
	}

	for {
		contracted := false
		for p, edges := range allEdges {
			if len(edges) == 2 {
				points, lengths := []point{}, []int{}
				for k, v := range edges {
					points = append(points, k)
					lengths = append(lengths, v)
				}
				ptA, ptB := points[0], points[1]
				lengthA, lengthB := lengths[0], lengths[1]

				allEdges[ptA][ptB] = lengthA + lengthB
				allEdges[ptB][ptA] = lengthA + lengthB
				delete(allEdges[ptA], p)
				delete(allEdges[ptB], p)
				delete(allEdges, p)
				contracted = true
			}
		}
		if !contracted {
			break
		}
	}

	return allEdges
}

func (g grid) longestClimbHike(p point, travelled int, used map[point]int, results *[]int, edges map[point](map[point]int)) {
	i, j := p.i, p.j
	if i == g.M-1 && j == g.N-2 {
		total := travelled
		for _, length := range used {
			total += length
		}
		*results = append(*results, total)
	}

	if _, ok := used[p]; ok {
		return
	}
	used[p] = travelled

	for np, length := range edges[p] {
		g.longestClimbHike(np, length, used, results, edges)
	}

	delete(used, p)
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	results := []int{}
	grid.longestHike(point{0, 1}, map[point]struct{}{}, &results)

	// answer: 2106
	fmt.Println(slices.Max(results))

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	results := []int{}
	grid.longestClimbHike(point{0, 1}, 0, map[point]int{}, &results, grid.contractedEdges())

	// answer: 6350
	fmt.Println(slices.Max(results))

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
