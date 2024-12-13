package main

import "util"

func parseGrid(lines []string) grid {
	return grid{util.ParseGrid(lines)}
}
