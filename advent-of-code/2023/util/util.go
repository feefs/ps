package util

import (
	"flag"
	"fmt"
	"os"
	"strings"
)

type Part func(lines []string) error

func runPart(part Part) error {
	b, err := os.ReadFile("input.txt")
	if err != nil {
		return err
	}
	lineStr := string(b)
	lines := strings.Split(lineStr, "\n")

	if err := part(lines); err != nil {
		return err
	}

	return nil
}

var (
	part = flag.Int("part", 0, "[1|2] to run part 1 or 2 respectively")
)

func ParseAndRun(partOne Part, partTwo Part) {
	flag.Parse()
	switch *part {
	case 1:
		if err := runPart(partOne); err != nil {
			fmt.Printf("part one error: %v\n", err)
		}
	case 2:
		if err := runPart(partTwo); err != nil {
			fmt.Printf("part two error: %v\n", err)
		}
	default:
		fmt.Printf("unknown part: %v\n", *part)
		flag.Usage()
	}
}
