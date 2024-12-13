package main

import (
	"container/list"
	"fmt"
	"slices"
	"strconv"
	"strings"
	"util"
)

func partOne(lines []string) error {
	disk := []int{}
	currId := 0
	for i, r := range lines[0] {
		length, err := strconv.Atoi(string(r))
		if err != nil {
			return err
		}
		if i%2 == 0 {
			for range length {
				disk = append(disk, currId)
			}
			currId += 1
		} else {
			for range length {
				disk = append(disk, -1)
			}
		}
	}

	freeBlocks := []int{}
	for i, id := range disk {
		if id == -1 {
			freeBlocks = append(freeBlocks, i)
		}
	}

	for _, i := range freeBlocks {
		for disk[len(disk)-1] == -1 {
			disk = disk[:len(disk)-1]
		}
		if i >= len(disk) {
			break
		}
		disk[i] = disk[len(disk)-1]
		disk = disk[:len(disk)-1]
	}

	result := 0
	for i, id := range disk {
		result += i * id
	}

	// answer: 6323641412437
	fmt.Println(result)

	return nil
}

type block struct {
	id     int
	length int
}

func printDisk(disk *list.List) {
	var builder strings.Builder
	for e := disk.Front(); e != nil; e = e.Next() {
		b := e.Value.(*block)
		s := "."
		if b.id != -1 {
			s = strconv.Itoa(b.id)
		}
		builder.WriteString(
			fmt.Sprintf("[%v]", strings.Repeat(s, b.length)),
		)
	}
	fmt.Println(builder.String())
}

func defragment(disk *list.List) {
	elements := []*list.Element{}
	for e := disk.Front(); e != nil; e = e.Next() {
		if e.Value.(*block).id != -1 {
			elements = append(elements, e)
		}
	}
	slices.SortFunc(elements, func(a *list.Element, b *list.Element) int {
		return b.Value.(*block).id - a.Value.(*block).id
	})

OuterLoop:
	for _, e := range elements {
		b := e.Value.(*block)
		for curr := disk.Front(); curr != nil; curr = curr.Next() {
			for curr.Value.(*block).id != -1 {
				// avoid looking for free space to the right of the current file
				if curr == e {
					continue OuterLoop
				}
				curr = curr.Next()
			}
			cb := curr.Value.(*block)
			if cb.length >= b.length {
				left := cb.length - b.length
				if left == 0 {
					cb.id = b.id
					b.id = -1
				} else {
					disk.InsertBefore(&block{id: b.id, length: b.length}, curr)
					cb.length = left
					b.id = -1
				}
				break
			}
		}
	}
}

func partTwo(lines []string) error {
	disk, err := parseDisk(lines)
	if err != nil {
		return err
	}

	defragment(disk)

	result := 0
	pos := 0
	for e := disk.Front(); e != nil; e = e.Next() {
		b := e.Value.(*block)
		for range b.length {
			if b.id != -1 {
				result += pos * b.id
			}
			pos += 1
		}
	}

	// answer: 6351801932670
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
