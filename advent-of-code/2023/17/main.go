package main

import (
	"container/heap"
	"fmt"
	"util"
)

type grid struct {
	util.Grid
	intRows []([]int)
}

type dir int

const (
	up dir = iota
	down
	left
	right
)

type point struct {
	i int
	j int
}

type beam struct {
	pt          point
	orientation dir
}

// HEAP IMPLEMENTATION

type heapItem struct {
	heat int
	bm   beam
}

type hp []heapItem

func (h hp) Len() int {
	return len(h)
}

func (h hp) Less(i, j int) bool {
	return h[i].heat < h[j].heat
}

func (h hp) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

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

// END HEAP IMPLEMENTATION

type push struct {
	nextBeam beam
	heat     int
}

func (g grid) nextPushes(b beam, lo, hi int) []push {
	result := []push{}
	i, j := b.pt.i, b.pt.j

	switch b.orientation {
	case up:
		heat := 0
		for d := 1; d < hi; d++ {
			ni, nj := i-d, j
			if !g.InBounds(ni, nj) {
				break
			}
			heat += g.intRows[ni][nj]
			if d < lo {
				continue
			}
			result = append(result, push{beam{point{i: ni, j: nj}, left}, heat})
			result = append(result, push{beam{point{i: ni, j: nj}, right}, heat})
		}
	case down:
		heat := 0
		for d := 1; d < hi; d++ {
			ni, nj := i+d, j
			if !g.InBounds(ni, nj) {
				break
			}
			heat += g.intRows[ni][nj]
			if d < lo {
				continue
			}
			result = append(result, push{beam{point{i: ni, j: nj}, left}, heat})
			result = append(result, push{beam{point{i: ni, j: nj}, right}, heat})
		}
	case left:
		heat := 0
		for d := 1; d < hi; d++ {
			ni, nj := i, j-d
			if !g.InBounds(ni, nj) {
				break
			}
			heat += g.intRows[ni][nj]
			if d < lo {
				continue
			}
			result = append(result, push{beam{point{i: ni, j: nj}, up}, heat})
			result = append(result, push{beam{point{i: ni, j: nj}, down}, heat})
		}
	case right:
		heat := 0
		for d := 1; d < hi; d++ {
			ni, nj := i, j+d
			if !g.InBounds(ni, nj) {
				break
			}
			heat += g.intRows[ni][nj]
			if d < lo {
				continue
			}
			result = append(result, push{beam{point{i: ni, j: nj}, up}, heat})
			result = append(result, push{beam{point{i: ni, j: nj}, down}, heat})
		}
	}

	return result
}

func (g grid) dij(lo, hi int) int {
	seen := map[beam]struct{}{}

	pq := &hp{
		heapItem{heat: 0, bm: beam{pt: point{i: 0, j: 0}, orientation: right}},
		heapItem{heat: 0, bm: beam{pt: point{i: 0, j: 0}, orientation: down}},
	}
	for pq.Len() > 0 {
		curr := heap.Pop(pq).(heapItem)
		heat, bm := curr.heat, curr.bm

		if bm.pt.i == g.M-1 && bm.pt.j == g.N-1 {
			return heat
		}

		if _, ok := seen[bm]; ok {
			continue
		}
		seen[bm] = struct{}{}

		for _, push := range g.nextPushes(bm, lo, hi) {
			newHeat := heat + push.heat
			heap.Push(pq, heapItem{heat: newHeat, bm: push.nextBeam})
		}
	}

	panic("unreachable")
}

func partOne(lines []string) error {
	grid := parseGrid(lines)

	// answer: 845
	fmt.Println(grid.dij(1, 4))

	return nil
}

func partTwo(lines []string) error {
	grid := parseGrid(lines)

	// answer: 993
	fmt.Println(grid.dij(4, 11))

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
