package main

import (
	"fmt"
	"strconv"
	"unicode"
	"util"
)

type grid struct {
	m      int
	n      int
	values []([]rune)
}

func newGrid(lines []string) grid {
	m := len(lines)
	n := len(lines[0])
	values := make([]([]rune), m)
	for i := 0; i < m; i++ {
		values[i] = []rune(lines[i])
	}
	visited := make([]([]bool), m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	return grid{m, n, values}
}

type number struct {
	num    int
	length int
	i      int
	j      int
}

func extractNumber(g *grid, i int, j int, visited []([]bool)) number {
	result := number{i: i, j: j}
	digits := []rune{}

	for j < g.n && unicode.IsDigit(g.values[i][j]) {
		digits = append(digits, g.values[i][j])
		visited[i][j] = true
		j += 1
	}

	num, err := strconv.Atoi(string(digits))
	if err != nil {
		panic(err)
	}
	result.num = num
	result.length = len(digits)

	return result
}

func (g *grid) numbers() []number {
	visited := make([]([]bool), g.m)
	for i := 0; i < g.m; i++ {
		visited[i] = make([]bool, g.n)
	}

	result := []number{}
	for i := 0; i < g.m; i++ {
		for j := 0; j < g.n; j++ {
			if unicode.IsDigit(g.values[i][j]) && !visited[i][j] {
				result = append(result, extractNumber(g, i, j, visited))
			}
		}
	}

	return result
}

func (g *grid) neighbors(i int, j int) []([]int) {
	candidates := []([]int){
		{i + 1, j + 1},
		{i + 1, j},
		{i + 1, j - 1},
		{i, j + 1},
		{i, j - 1},
		{i - 1, j + 1},
		{i - 1, j},
		{i - 1, j - 1},
	}

	neighbors := []([]int){}
	for _, cand := range candidates {
		ni, nj := cand[0], cand[1]
		if 0 <= ni && ni < g.m && 0 <= nj && nj < g.n {
			neighbors = append(neighbors, cand)
		}
	}

	return neighbors
}

func (g *grid) partNumbers(numbers []number) []number {
	result := []number{}
	for _, n := range numbers {
		valid := false
		for l := 0; l < n.length; l++ {
			for _, neb := range g.neighbors(n.i, n.j+l) {
				ni, nj := neb[0], neb[1]
				value := g.values[ni][nj]
				if !unicode.IsDigit(value) && value != '.' {
					valid = true
				}
			}
		}
		if valid {
			result = append(result, n)
		}
	}

	return result
}

type gear struct {
	ratio int
}

func (g *grid) gears(numbers []number) []gear {
	type point struct {
		i int
		j int
	}
	type gearCandidate struct {
		numbers map[number]struct{}
	}
	candidates := map[point]gearCandidate{}

	for _, n := range numbers {
		for l := 0; l < n.length; l++ {
			for _, neb := range g.neighbors(n.i, n.j+l) {
				ni, nj := neb[0], neb[1]
				if g.values[ni][nj] == '*' {
					if _, ok := candidates[point{i: ni, j: nj}]; !ok {
						candidates[point{i: ni, j: nj}] = gearCandidate{make(map[number]struct{})}
					}
					candidates[point{i: ni, j: nj}].numbers[n] = struct{}{}
				}
			}
		}
	}

	result := []gear{}
	for _, cand := range candidates {
		if len(cand.numbers) == 2 {
			ratio := 1
			for n := range cand.numbers {
				ratio *= n.num
			}
			result = append(result, gear{ratio: ratio})
		}
	}

	return result
}

func partOne(lines []string) error {
	result := 0
	g := newGrid(lines)
	for _, n := range g.partNumbers(g.numbers()) {
		result += n.num
	}

	// answer: 528799
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	result := 0
	g := newGrid(lines)
	for _, gr := range g.gears(g.numbers()) {
		result += gr.ratio
	}

	// answer: 84907174
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
