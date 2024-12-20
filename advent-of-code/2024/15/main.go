package main

import (
	"fmt"
	"strings"
	"util"
)

type grid struct {
	util.Grid
	robot point
}

var (
	Up    = util.Dir{Dx: -1, Dy: 0}
	Down  = util.Dir{Dx: 1, Dy: 0}
	Left  = util.Dir{Dx: 0, Dy: -1}
	Right = util.Dir{Dx: 0, Dy: 1}
)

var dirs = map[rune]util.Dir{
	'^': Up,
	'<': Left,
	'>': Right,
	'v': Down,
}

type point struct {
	i int
	j int
}

func (g *grid) print() {
	output := strings.Builder{}
	for _, row := range g.Rows {
		output.WriteString(string(row))
		output.WriteRune('\n')
	}
	fmt.Print(output.String())
}

func (g *grid) push(move rune) {
	dir, _ := dirs[move]
	ni, nj := g.robot.i+dir.Dx, g.robot.j+dir.Dy
	for {
		switch g.Rows[ni][nj] {
		case '#':
			return
		// this code can be reused for horizontal moves in part 2
		case '[':
			fallthrough
		case ']':
			fallthrough
		case 'O':
			ni, nj = ni+dir.Dx, nj+dir.Dy
		default:
			for !(ni == g.robot.i && nj == g.robot.j) {
				g.Rows[ni][nj], g.Rows[ni-dir.Dx][nj-dir.Dy] = g.Rows[ni-dir.Dx][nj-dir.Dy], g.Rows[ni][nj]
				ni, nj = ni-dir.Dx, nj-dir.Dy
			}
			g.robot.i, g.robot.j = g.robot.i+dir.Dx, g.robot.j+dir.Dy
			return
		}
	}
}

func (g *grid) widen() {
	newRows := make([]([]rune), g.M)
	for i := range g.M {
		newRows[i] = make([]rune, g.N*2)
	}
	for i := range g.M {
		for j := range g.N {
			switch g.Rows[i][j] {
			case '#':
				newRows[i][j*2] = '#'
				newRows[i][(j*2)+1] = '#'
			case 'O':
				newRows[i][j*2] = '['
				newRows[i][(j*2)+1] = ']'
			case '.':
				newRows[i][j*2] = '.'
				newRows[i][(j*2)+1] = '.'
			case '@':
				newRows[i][j*2] = '@'
				newRows[i][(j*2)+1] = '.'
				g.robot.j = j * 2
			}
		}
	}
	g.Rows = newRows
	g.N = 2 * g.N
}

func (g *grid) widenedPush(move rune) {
	dir, _ := dirs[move]
	if dir == Left || dir == Right {
		g.push(move)
	} else {
		// point values in the queue correspond to '['
		q := []point{}
		ni, nj := g.robot.i+dir.Dx, g.robot.j+dir.Dy
		switch g.Rows[ni][nj] {
		case '#':
			return
		case '[':
			q = append(q, point{ni, nj})
		case ']':
			q = append(q, point{ni, nj - 1})
		}

		boxRows := []([]point){}
		for len(q) > 0 {
			boxRow := []point{}
			seen := map[point]struct{}{}
			for _, p := range q {
				if _, ok := seen[p]; ok {
					continue
				} else {
					seen[p] = struct{}{}
					boxRow = append(boxRow, p)
				}
			}
			boxRows = append(boxRows, boxRow)

			nextQ := []point{}
			for len(q) > 0 {
				curr := q[0]
				q = q[1:]
				if g.Rows[curr.i+dir.Dx][curr.j+dir.Dy] == ']' {
					nextQ = append(nextQ, point{curr.i + dir.Dx, curr.j + dir.Dy - 1})
				}
				if g.Rows[curr.i+dir.Dx][curr.j+dir.Dy] == '[' {
					nextQ = append(nextQ, point{curr.i + dir.Dx, curr.j + dir.Dy})
				}
				if g.Rows[curr.i+dir.Dx][curr.j+dir.Dy+1] == '[' {
					nextQ = append(nextQ, point{curr.i + dir.Dx, curr.j + dir.Dy + 1})
				}
			}
			q = nextQ
		}

		// verify that all boxes can be moved
		for i := len(boxRows) - 1; i >= 0; i-- {
			for _, box := range boxRows[i] {
				if g.Rows[box.i+dir.Dx][box.j+dir.Dy] == '#' || g.Rows[box.i+dir.Dx][box.j+dir.Dy+1] == '#' {
					return
				}
			}
		}
		// move all boxes starting from the farthest row to the closest
		for i := len(boxRows) - 1; i >= 0; i-- {
			for _, box := range boxRows[i] {
				g.Rows[box.i+dir.Dx][box.j+dir.Dy], g.Rows[box.i+dir.Dx][box.j+dir.Dy+1], g.Rows[box.i][box.j], g.Rows[box.i][box.j+1] =
					g.Rows[box.i][box.j], g.Rows[box.i][box.j+1], g.Rows[box.i+dir.Dx][box.j+dir.Dy], g.Rows[box.i+dir.Dx][box.j+dir.Dy+1]
			}
		}
		// move the robot
		g.Rows[g.robot.i][g.robot.j], g.Rows[g.robot.i+dir.Dx][g.robot.j+dir.Dy] = '.', '@'
		g.robot.i, g.robot.j = g.robot.i+dir.Dx, g.robot.j+dir.Dy
	}
}

func partOne(lines []string) error {
	grid, moves := parse(lines)

	for _, move := range moves {
		grid.push(move)
	}

	result := 0
	for i := range grid.M {
		for j := range grid.N {
			if grid.Rows[i][j] == 'O' {
				result += (100 * i) + j
			}
		}
	}

	// answer: 1465523
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	grid, moves := parse(lines)
	grid.widen()

	for _, move := range moves {
		grid.widenedPush(move)
	}

	result := 0
	for i := range grid.M {
		for j := range grid.N {
			if grid.Rows[i][j] == '[' {
				result += (100 * i) + j
			}
		}
	}

	// answer: 1471049
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
