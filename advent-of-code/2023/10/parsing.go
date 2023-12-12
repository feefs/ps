package main

func parseGrid(lines []string) grid {
	result := grid{}
	result.m = len(lines)
	result.n = len(lines[0])
	result.values = make([]([]rune), result.m)

	for i := 0; i < result.m; i++ {
		result.values[i] = []rune(lines[i])
		for j := 0; j < result.n; j++ {
			if lines[i][j] == 'S' {
				result.startRow = i
				result.startCol = j
			}
		}
	}

	return result
}
