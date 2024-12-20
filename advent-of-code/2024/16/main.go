package main

import (
	"container/heap"
	"fmt"
	"math"
	"slices"
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

var (
	North = util.Dir{Dx: -1, Dy: 0}
	South = util.Dir{Dx: 1, Dy: 0}
	West  = util.Dir{Dx: 0, Dy: -1}
	East  = util.Dir{Dx: 0, Dy: 1}
)

var turns = map[util.Dir]([]util.Dir){
	North: {West, East},
	South: {West, East},
	West:  {North, South},
	East:  {North, South},
}

// HEAP IMPLEMENTATION

type heapItem struct {
	score float64
	pt    point
	dir   util.Dir
	path  []point
}

type hp []heapItem

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].score < h[j].score }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length
	// not just its contents.
	*h = append(*h, x.(heapItem))
}
func (h *hp) Pop() any {
	// Push and Pop use pointer receivers because they modify the slice's length
	// not just its contents.
	var res any
	*h, res = (*h)[:len(*h)-1], (*h)[len(*h)-1]
	return res
}

var _ heap.Interface = (*hp)(nil)

// END HEAP IMPLEMENTATION

type scoresKey struct {
	pt  point
	dir util.Dir
}

func (g *grid) dijkstras() (map[scoresKey]float64, map[point]struct{}) {
	scores := make(map[scoresKey]float64)
	for i := range g.M {
		for j := range g.N {
			pt := point{i, j}
			scores[scoresKey{pt, North}] = math.Inf(1)
			scores[scoresKey{pt, South}] = math.Inf(1)
			scores[scoresKey{pt, West}] = math.Inf(1)
			scores[scoresKey{pt, East}] = math.Inf(1)
		}
	}
	tiles := make(map[point]struct{})

	best := math.Inf(1)
	pq := &hp{{0, g.start, East, []point{g.start}}}
	for pq.Len() > 0 {
		curr := heap.Pop(pq).(heapItem)

		// outdated value (a path to curr.pt with a smaller score already exists)
		if scores[scoresKey{curr.pt, curr.dir}] < curr.score {
			continue
		}

		if curr.pt == g.end && curr.score <= best {
			best = curr.score
			for _, tile := range curr.path {
				tiles[tile] = struct{}{}
			}
		}

		ni, nj := curr.pt.i+curr.dir.Dx, curr.pt.j+curr.dir.Dy
		if g.InBounds(ni, nj) && g.Rows[ni][nj] != '#' {
			alt := curr.score + 1
			k := scoresKey{point{ni, nj}, curr.dir}
			// include equally short paths with (<=), not just strictly better ones (<)
			if alt <= scores[k] {
				scores[k] = alt
				newPath := make([]point, len(curr.path)+1)
				copy(newPath, curr.path)
				newPath[len(curr.path)] = point{ni, nj}
				heap.Push(pq, heapItem{alt, point{ni, nj}, curr.dir, newPath})
			}
		}

		// turn
		for _, turnDir := range turns[curr.dir] {
			alt := curr.score + 1000
			k := scoresKey{curr.pt, turnDir}
			// include equally short paths with (<=), not just strictly better ones (<)
			if alt <= scores[k] {
				scores[k] = alt
				heap.Push(pq, heapItem{alt, curr.pt, turnDir, curr.path})
			}
		}
	}

	return scores, tiles
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	scores, _ := grid.dijkstras()

	result := slices.Min([]float64{
		scores[scoresKey{grid.end, North}],
		scores[scoresKey{grid.end, South}],
		scores[scoresKey{grid.end, West}],
		scores[scoresKey{grid.end, East}],
	})

	// answer: 105496
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	_, tiles := grid.dijkstras()

	result := len(tiles)

	// answer: 524
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
