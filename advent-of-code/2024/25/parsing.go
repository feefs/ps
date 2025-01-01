package main

func parse(lines []string) ([]lock, []key) {
	schematics := []([]string){}
	schematic := []string{}
	for i := range len(lines) {
		line := lines[i]
		if line != "" {
			schematic = append(schematic, line)
			continue
		}
		schematics = append(schematics, schematic)
		schematic = []string{}
	}
	schematics = append(schematics, schematic)
	return parseSchematics(schematics)
}

func parseSchematics(schematics []([]string)) ([]lock, []key) {
	locks := []lock{}
	keys := []key{}
	for _, schematic := range schematics {
		if schematic[0] == "#####" {
			lock := lock{}
			for col := range 5 {
				for row := 1; row < 6; row++ {
					if schematic[row][col] == '#' {
						lock[col] += 1
					}
				}
			}
			locks = append(locks, lock)
		} else {
			key := key{}
			for col := range 5 {
				for row := 5; row > 0; row-- {
					if schematic[row][col] == '#' {
						key[col] += 1
					}
				}
			}
			keys = append(keys, key)
		}
	}
	return locks, keys
}
