package util

import "slices"

type Grid struct {
	M    int
	N    int
	Rows []([]rune)
}

func (g Grid) InBounds(i, j int) bool {
	return 0 <= i && i < g.M && 0 <= j && j < g.N
}

func ParseGrid(lines []string) Grid {
	m, n := len(lines), len(lines[0])
	rows := make([]([]rune), m)
	for i, line := range lines {
		rows[i] = []rune(line)
	}
	return Grid{m, n, rows}
}

type Dir struct {
	Dx int
	Dy int
}

func CardinalDirs() []Dir {
	return []Dir{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
}

func IntercardinalDirs() []Dir {
	return []Dir{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
}

func AllDirs() []Dir {
	return slices.Concat(CardinalDirs(), IntercardinalDirs())
}
