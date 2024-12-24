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
	corrupted map[point]bool
	M         int
	N         int
}

type qItem struct {
	p point
	d int
}

func (g grid) bfs() int {
	seen := map[point]bool{}
	q := []qItem{{point{0, 0}, 0}}
	for len(q) > 0 {
		nextQ := []qItem{}
		for len(q) > 0 {
			curr := q[0]
			q = q[1:]
			if seen[curr.p] {
				continue
			}
			seen[curr.p] = true

			if curr.p.i == g.M-1 && curr.p.j == g.N-1 {
				return curr.d
			}

			for _, dir := range util.CardinalDirs() {
				ni, nj := curr.p.i+dir.Dx, curr.p.j+dir.Dy
				if !(0 <= ni && ni < g.M) || !(0 <= nj && nj < g.N) {
					continue
				}
				if g.corrupted[point{ni, nj}] {
					continue
				}
				nextQ = append(nextQ, qItem{point{ni, nj}, curr.d + 1})
			}
		}
		q = nextQ
	}

	return -1
}

func partOne(lines []string) error {
	bytes, err := parseBytes(lines)
	if err != nil {
		return err
	}

	corrupted := map[point]bool{}
	for i, coordinate := range bytes {
		if i == 1024 {
			break
		}
		corrupted[coordinate] = true
	}

	grid := grid{corrupted, 71, 71}

	result := grid.bfs()

	// answer: 348
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	bytes, err := parseBytes(lines)
	if err != nil {
		return err
	}

	var blockingCoordinate point
	corrupted := map[point]bool{}
	grid := grid{corrupted, 71, 71}
	for _, coordinate := range bytes {
		corrupted[coordinate] = true
		v := grid.bfs()
		if v == -1 {
			blockingCoordinate = coordinate
			break
		}
	}

	result := fmt.Sprintf("%d,%d", blockingCoordinate.i, blockingCoordinate.j)

	// answer: 54,44
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
