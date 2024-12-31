package main

import (
	"regexp"
	"util"
)

func parse(lines []string) ([]node, neighbors, error) {
	nodesMap := map[node]struct{}{}
	neighbors := make(neighbors)
	r := regexp.MustCompile(`(\w+)-(\w+)`)
	for _, line := range lines {
		match := r.FindStringSubmatch(line)
		if len(match) != 3 {
			return nil, nil, util.InvalidStateError("match isn't length 3: %v", match)
		}
		a, b := node(match[1]), node(match[2])
		neighbors[a] = append(neighbors[a], b)
		neighbors[b] = append(neighbors[b], a)
		nodesMap[a] = struct{}{}
		nodesMap[b] = struct{}{}
	}
	nodes := []node{}
	for node := range nodesMap {
		nodes = append(nodes, node)
	}
	return nodes, neighbors, nil
}
