package main

import (
	"fmt"
	"util"
)

type grid struct {
	util.Grid
	start    point
	startDir util.Dir
}

type point struct {
	i int
	j int
}

var (
	Up    = util.Dir{Dx: -1, Dy: 0}
	Down  = util.Dir{Dx: 1, Dy: 0}
	Left  = util.Dir{Dx: 0, Dy: -1}
	Right = util.Dir{Dx: 0, Dy: 1}
)

type state struct {
	position point
	dir      util.Dir
}

func (g *grid) patrol() (exited bool, seen map[state]struct{}, err error) {
	seen = make(map[state]struct{})

	nextDirs := map[util.Dir]util.Dir{
		Up:    Right,
		Right: Down,
		Down:  Left,
		Left:  Up,
	}

	curr := g.start
	currDir := g.startDir
	for {
		if _, ok := seen[state{curr, currDir}]; ok {
			return false, seen, nil
		} else {
			seen[state{curr, currDir}] = struct{}{}
		}

		ni, nj := curr.i+currDir.Dx, curr.j+currDir.Dy
		if !g.InBounds(ni, nj) {
			return true, seen, nil
		}

		if g.Rows[ni][nj] == '#' {
			nextDir, ok := nextDirs[currDir]
			if !ok {
				return false, seen, util.InvalidStateError("nextDir not found for currDir: %v", currDir)
			}
			currDir = nextDir
		} else {
			curr.i, curr.j = ni, nj
		}
	}
}

func partOne(lines []string) error {
	grid, err := parseGrid(lines)
	if err != nil {
		return err
	}

	_, seen, err := grid.patrol()
	if err != nil {
		return err
	}

	visited := make(map[point]struct{})
	for state := range seen {
		visited[state.position] = struct{}{}
	}

	result := len(visited)

	// answer: 5318
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid, err := parseGrid(lines)
	if err != nil {
		return err
	}

	_, seen, err := grid.patrol()
	if err != nil {
		return err
	}

	visited := make(map[point]struct{})
	for state := range seen {
		visited[state.position] = struct{}{}
	}

	result := 0
	for obstruction := range visited {
		grid.Rows[obstruction.i][obstruction.j] = '#'
		exited, _, err := grid.patrol()
		if err != nil {
			return err
		}
		if !exited {
			result += 1
		}
		grid.Rows[obstruction.i][obstruction.j] = '.'
	}

	// answer: 1831
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
