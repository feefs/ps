package main

import (
	"regexp"
	"strings"
)

func computeEdge(nodeA, nodeB string) edge {
	if nodeA > nodeB {
		nodeA, nodeB = nodeB, nodeA
	}
	return edge{nodeA, nodeB}
}

func parseGraph(lines []string) graph {
	nodesMap := map[string]struct{}{}
	edgesMap := map[edge]struct{}{}
	r := regexp.MustCompile(`(\w+): (.*)`)
	for _, line := range lines {
		match := r.FindAllStringSubmatch(line, -1)
		a := match[0][1]
		others := strings.Split(match[0][2], " ")

		nodesMap[a] = struct{}{}
		for _, b := range others {
			e := computeEdge(a, b)
			edgesMap[e] = struct{}{}
			nodesMap[b] = struct{}{}
		}

	}

	nodes := []string{}
	for node := range nodesMap {
		nodes = append(nodes, node)
	}

	edges := []edge{}
	for edge := range edgesMap {
		edges = append(edges, edge)
	}

	return graph{nodes, edges}
}
