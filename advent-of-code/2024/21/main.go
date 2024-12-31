package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
	"util"
)

type point struct {
	i int
	j int
}

type move struct {
	a rune
	b rune
}

type graph map[move]string

func vertical(p1 point, p2 point) string {
	if p2.i > p1.i {
		return strings.Repeat("v", p2.i-p1.i)
	} else {
		return strings.Repeat("^", p1.i-p2.i)
	}
}

func horizontal(p1 point, p2 point) string {
	if p2.j > p1.j {
		return strings.Repeat(">", p2.j-p1.j)
	} else {
		return strings.Repeat("<", p1.j-p2.j)
	}
}

func createGraph(points map[rune]point, forbidden point) graph {
	g := map[move]string{}
	for a, p1 := range points {
		for b, p2 := range points {
			if p2.j > p1.j {
				if corner := (point{p2.i, p1.j}); corner == forbidden {
					g[move{a, b}] = horizontal(p1, p2) + vertical(p1, p2) + "A"
				} else {
					g[move{a, b}] = vertical(p1, p2) + horizontal(p1, p2) + "A"
				}
			} else {
				if corner := (point{p1.i, p2.j}); corner == forbidden {
					g[move{a, b}] = vertical(p1, p2) + horizontal(p1, p2) + "A"
				} else {
					g[move{a, b}] = horizontal(p1, p2) + vertical(p1, p2) + "A"
				}
			}
		}
	}
	return g
}

func createNumpad() graph {
	points := map[rune]point{
		'7': {0, 0}, '8': {0, 1}, '9': {0, 2},
		'4': {1, 0}, '5': {1, 1}, '6': {1, 2},
		'1': {2, 0}, '2': {2, 1}, '3': {2, 2},
		'0': {3, 1}, 'A': {3, 2},
	}
	return createGraph(points, point{3, 0})
}

func createArrowpad() graph {
	points := map[rune]point{
		'^': {0, 1}, 'A': {0, 2},
		'<': {1, 0}, 'v': {1, 1}, '>': {1, 2},
	}
	forbidden := point{0, 0}
	return createGraph(points, forbidden)
}

func (g graph) presses(sequence string) string {
	b := strings.Builder{}
	curr := 'A'
	for _, button := range sequence {
		b.WriteString(g[move{curr, button}])
		curr = button
	}
	return b.String()
}

func partOne(lines []string) error {
	numpad := createNumpad()
	arrowpad := createArrowpad()

	r := regexp.MustCompile(`\d+`)
	result := 0
	for _, line := range lines {
		numpadPresses := numpad.presses(line)
		arrowpadPresses1 := arrowpad.presses(numpadPresses)
		arrowpadPresses2 := arrowpad.presses(arrowpadPresses1)
		n, _ := strconv.Atoi(r.FindString(line))
		result += len(arrowpadPresses2) * n
	}

	// answer: 171596
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	numpad := createNumpad()
	arrowpad := createArrowpad()

	// since only the length matters, we don't need to construct the full sequence.
	// to find the current sequence length, sum up all the sequence's subsequence
	// lengths with n-1 arrowpads left.
	type key struct {
		sequence string
		n        int
	}
	cache := map[key]int{}
	var f func(string, int) int
	f = func(sequence string, n int) int {
		if v, ok := cache[key{sequence, n}]; ok {
			return v
		}
		if n == 0 {
			return len(sequence)
		}
		result := 0
		curr := 'A'
		for _, button := range sequence {
			result += f(arrowpad[move{curr, button}], n-1)
			curr = button
		}
		cache[key{sequence, n}] = result
		return result
	}

	r := regexp.MustCompile(`\d+`)
	result := 0
	for _, line := range lines {
		numpadPresses := numpad.presses(line)
		n, _ := strconv.Atoi(r.FindString(line))
		result += f(numpadPresses, 25) * n
	}

	// answer: 209268004868246
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
