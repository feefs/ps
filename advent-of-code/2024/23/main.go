package main

import (
	"fmt"
	"slices"
	"strings"
	"util"
)

type node string

type neighbors map[node]([]node)

func sharedNeighbors(n1 node, n2 node, nbs neighbors) []node {
	m := map[node]bool{}
	for _, n1n := range nbs[n1] {
		m[n1n] = true
	}
	result := []node{}
	for _, n2n := range nbs[n2] {
		if m[n2n] {
			result = append(result, n2n)
		}
	}
	return result
}

func isClique(nodes []node, nbs neighbors) bool {
	for i := range len(nodes) {
		for j := i + 1; j < len(nodes); j++ {
			n1, n2 := nodes[i], nodes[j]
			if !slices.Contains(nbs[n1], n2) {
				return false
			}
		}
	}
	return true
}

func partOne(lines []string) error {
	nodes, nbs, err := parse(lines)
	if err != nil {
		return err
	}

	result := 0
	for i := range len(nodes) {
		for j := i + 1; j < len(nodes); j++ {
			for k := j + 1; k < len(nodes); k++ {
				n1, n2, n3 := nodes[i], nodes[j], nodes[k]
				if n1[0] != 't' && n2[0] != 't' && n3[0] != 't' {
					continue
				}
				if isClique([]node{n1, n2, n3}, nbs) {
					result += 1
				}
			}
		}
	}

	// answer: 1370
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	nodes, nbs, err := parse(lines)
	if err != nil {
		return err
	}

	// observation: every node has 13 neighbors
	// test for cliques starting from size 14 by looking
	// at pairs of nodes and their shared neighbors

	clique := []node{}
	k := 14
out:
	for k > 0 {
		for _, n1 := range nodes {
			for _, n2 := range nbs[n1] {
				if n2 == n1 {
					continue
				}
				sn := sharedNeighbors(n1, n2, nbs)
				if len(sn) != k-2 {
					continue
				}
				candidate := append(sn, n1, n2)
				if !isClique(candidate, nbs) {
					continue
				}
				clique = candidate
				break out
			}
		}
		k -= 1
	}

	values := make([]string, len(clique))
	for i, n := range clique {
		values[i] = string(n)
	}
	slices.Sort(values)
	result := strings.Join(values, ",")

	// answer: am,au,be,cm,fo,ha,hh,im,nt,os,qz,rr,so
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
