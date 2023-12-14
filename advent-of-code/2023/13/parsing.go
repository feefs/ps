package main

func parseGrids(lines []string) []grid {
	result := []grid{}

	rows := []([]rune){}
	for _, line := range lines {
		if line == "" {
			result = append(result, grid{m: len(rows), n: len(rows[0]), rows: rows})
			rows = []([]rune){}
		} else {
			rows = append(rows, []rune(line))
		}
	}
	result = append(result, grid{m: len(rows), n: len(rows[0]), rows: rows})

	return result
}
