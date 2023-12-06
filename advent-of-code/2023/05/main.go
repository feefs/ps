package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
	"util"
)

// inclusive endpoints
type interval struct {
	start int
	end   int
}

func (i interval) intersect(i2 interval) *interval {
	if i2.start > i.end {
		return nil
	} else if i2.start >= i.start {
		return &interval{start: i2.start, end: min(i2.end, i.end)}
	} else if i2.end >= i.start {
		return &interval{start: i.start, end: min(i2.end, i.end)}
	} else {
		return nil
	}
}

type mapping struct {
	src    int
	dst    int
	length int
}

func (c mapping) interval() interval {
	result := interval{start: c.src}
	if c.length == math.MaxInt {
		result.end = math.MaxInt
	} else {
		result.end = c.src + c.length - 1
	}

	return result
}

type almanacMap struct {
	mps []mapping
}

// adds extra mappings to the beginning and end in order to
// pad the boundaries to 0 and math.MaxInt respectively
func (a almanacMap) paddedMappings() []mapping {
	result := []mapping{}
	if a.mps[0].src > 0 {
		result = append(result, mapping{
			src:    0,
			dst:    0,
			length: a.mps[0].src,
		})
	}
	result = append(result, a.mps...)
	last := result[len(result)-1]
	result = append(result, mapping{
		src:    last.src + last.length,
		dst:    last.src + last.length,
		length: math.MaxInt,
	})

	return result
}

func parseSeeds(line string) []int {
	result := []int{}
	line = strings.TrimPrefix(line, "seeds: ")
	numbers := strings.Split(line, " ")
	for _, num := range numbers {
		n, _ := strconv.Atoi(num)
		result = append(result, n)
	}

	return result
}

func parseAlmanacMap(lines []string) almanacMap {
	result := almanacMap{}

	for _, line := range lines[1:] {
		mp := mapping{}
		numberStrings := strings.Split(line, " ")
		numbers := []int{}
		for _, num := range numberStrings {
			n, _ := strconv.Atoi(num)
			numbers = append(numbers, n)
		}

		mp.dst = numbers[0]
		mp.src = numbers[1]
		mp.length = numbers[2]

		result.mps = append(result.mps, mp)
	}

	sort.Slice(result.mps, func(i, j int) bool {
		return result.mps[i].src < result.mps[j].src
	})

	return result
}

func parseAlmanacMaps(lines []string) []almanacMap {
	buffer := []string{}
	almanacMaps := []almanacMap{}
	for _, line := range lines {
		if line == "" {
			if len(buffer) > 0 {
				almanacMaps = append(almanacMaps, parseAlmanacMap(buffer))
			}
			buffer = []string{}
		} else {
			buffer = append(buffer, line)
		}
	}
	almanacMaps = append(almanacMaps, parseAlmanacMap(buffer))

	return almanacMaps
}

func parseSeedIntervals(line string) []interval {
	result := []interval{}
	trimmed := strings.TrimPrefix(line, "seeds: ")
	numbers := strings.Split(trimmed, " ")
	for i := 0; i < len(numbers)-1; i += 2 {
		iv := interval{}
		iv.start, _ = strconv.Atoi(numbers[i])
		length, _ := strconv.Atoi(numbers[i+1])
		iv.end = iv.start + length - 1
		result = append(result, iv)
	}

	return result
}

func search(start int, almanacMaps []almanacMap) int {
	curr := start
	for _, almanacMap := range almanacMaps {
		for _, mapping := range almanacMap.paddedMappings() {
			if curr < mapping.src {
				break
			}
			if curr <= mapping.src+mapping.length {
				curr = mapping.dst + (curr - mapping.src)
				break
			}
		}
	}

	return curr
}

func searchIntervals(iv interval, almanacMaps []almanacMap) int {
	result := math.MaxInt

	intervals := []interval{iv}
	for _, almanacMap := range almanacMaps {
		next_intervals := []interval{}
		for _, iv := range intervals {
			for _, mapping := range almanacMap.paddedMappings() {
				intersection := iv.intersect(mapping.interval())
				if intersection != nil {
					next_intervals = append(next_intervals, interval{
						start: mapping.dst + (intersection.start - mapping.src),
						end:   mapping.dst + (intersection.end - mapping.src),
					})
				}
			}
		}
		intervals = next_intervals
	}

	for _, iv := range intervals {
		result = min(result, iv.start)
	}

	return result
}

func partOne(lines []string) error {
	result := math.MaxInt
	seeds := parseSeeds(lines[0])
	almanacMaps := parseAlmanacMaps(lines[2:])
	for _, seed := range seeds {
		result = min(result, search(seed, almanacMaps))
	}

	// answer: 214922730
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	result := math.MaxInt
	seedIntervals := parseSeedIntervals(lines[0])
	almanacMaps := parseAlmanacMaps(lines[2:])
	for _, iv := range seedIntervals {
		result = min(result, searchIntervals(iv, almanacMaps))
	}

	// answer: 148041808
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
