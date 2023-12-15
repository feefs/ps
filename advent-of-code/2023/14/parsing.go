package main

func parseGrid(lines []string) grid {
	rows := make([]([]rune), len(lines))
	for i, line := range lines {
		rows[i] = []rune(line)
	}

	return grid{m: len(lines), n: len(lines[0]), rows: rows}
}
