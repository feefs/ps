package main

import (
	"container/list"
	"strconv"
)

func parseDisk(lines []string) (*list.List, error) {
	disk := list.New()
	isFile := true
	currId := 0
	for _, r := range lines[0] {
		l, err := strconv.Atoi(string(r))
		if err != nil {
			return nil, err
		}
		if isFile {
			if l > 0 {
				disk.PushBack(&block{id: currId, length: l})
			}
			currId += 1
		} else {
			if l > 0 {
				disk.PushBack(&block{id: -1, length: l})
			}
		}
		isFile = !isFile
	}
	return disk, nil
}
