package main

import (
	"fmt"
	"sort"
	"util"
)

type point struct {
	x int
	y int
	z int
}

type brick struct {
	id    int
	start point
	end   point
}

func (b brick) points() []point {
	result := []point{}
	if b.start.x != b.end.x {
		x1, x2 := min(b.start.x, b.end.x), max(b.start.x, b.end.x)
		for x := x1; x <= x2; x++ {
			result = append(result, point{x, b.start.y, b.start.z})
		}
	} else if b.start.y != b.end.y {
		y1, y2 := min(b.start.y, b.end.y), max(b.start.y, b.end.y)
		for y := y1; y <= y2; y++ {
			result = append(result, point{b.start.x, y, b.start.z})
		}
	} else {
		z1, z2 := min(b.start.z, b.end.z), max(b.start.z, b.end.z)
		for z := z1; z <= z2; z++ {
			result = append(result, point{b.start.x, b.start.y, z})
		}
	}
	return result
}

type coord struct {
	x int
	y int
}

type entry struct {
	height int
	id     int
}

type topDownView map[coord]entry

func (t topDownView) get(c coord) entry {
	if _, ok := t[c]; !ok {
		t[c] = entry{height: 0, id: -1}
	}
	return t[c]
}

type supportedByGraph map[int](map[int]struct{})

func computeSupportedByGraph(bricks []brick) supportedByGraph {
	// brick.start.z is always less than brick.end.z
	// sorting by brick.start.z is enough
	sort.SliceStable(bricks, func(i, j int) bool {
		return bricks[i].start.z < bricks[j].start.z
	})

	view := topDownView{}
	supportedBy := supportedByGraph{}
	for _, brick := range bricks {
		points := brick.points()

		// compute height of the coordinates that support the current brick
		touchingHeight := -1
		for _, pt := range points {
			c := coord{pt.x, pt.y}
			touchingHeight = max(touchingHeight, view.get(c).height)
		}

		// update supportedBy
		for _, pt := range points {
			entry := view.get(coord{pt.x, pt.y})
			if entry.height == touchingHeight {
				if _, ok := supportedBy[brick.id]; !ok {
					supportedBy[brick.id] = make(map[int]struct{})
				}
				supportedBy[brick.id][entry.id] = struct{}{}
			}
		}

		// drop brick and update top down view
		brickHeight := brick.end.z - brick.start.z + 1
		if brickHeight > 1 {
			// vertical brick
			c := coord{brick.start.x, brick.start.y}
			view[c] = entry{height: touchingHeight + 1 + (brickHeight - 1), id: brick.id}
		} else {
			// horizontal brick
			for _, pt := range points {
				c := coord{pt.x, pt.y}
				view[c] = entry{height: touchingHeight + 1, id: brick.id}
			}
		}
	}

	return supportedBy
}

func disintegratableBricks(bricks []brick, supportedBy supportedByGraph) map[int]struct{} {
	// for every brick that is supported by only one brick, the supporting brick cannot be disintegrated
	canDisintegrate := map[int]struct{}{}
	for id := 0; id < len(bricks); id++ {
		canDisintegrate[id] = struct{}{}
	}
	for id := 0; id < len(bricks); id++ {
		supportingBricks := supportedBy[id]
		if len(supportingBricks) == 1 {
			for invalidId := range supportingBricks {
				delete(canDisintegrate, invalidId)
				break
			}
		}
	}

	return canDisintegrate
}

func partOne(lines []string) error {
	bricks := parseBricks(lines)

	supportedBy := computeSupportedByGraph(bricks)
	disintegratableBricks := disintegratableBricks(bricks, supportedBy)

	// answer: 398
	fmt.Println(len(disintegratableBricks))

	return nil
}

func partTwo(lines []string) error {
	bricks := parseBricks(lines)

	supportedBy := computeSupportedByGraph(bricks)
	disintegratableBricks := disintegratableBricks(bricks, supportedBy)

	result := 0
	for id := 0; id < len(bricks); id++ {
		if _, ok := disintegratableBricks[id]; ok {
			continue
		}

		fallingBricks := map[int]struct{}{id: {}}
		prevLength := len(fallingBricks)
		for {
			for bid := 0; bid < len(bricks); bid++ {
				willFall := true
				for supportingBid := range supportedBy[bid] {
					if _, ok := fallingBricks[supportingBid]; !ok {
						willFall = false
					}
				}
				if willFall {
					fallingBricks[bid] = struct{}{}
				}
			}

			currLength := len(fallingBricks)
			if currLength == prevLength {
				break
			} else {
				prevLength = currLength
			}
		}

		result += len(fallingBricks) - 1
	}

	// answer: 70727
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
