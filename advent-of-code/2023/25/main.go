package main

import (
	"errors"
	"fmt"
	"math/rand"
	"util"
)

type graph struct {
	nodes []string
	edges []edge
}

type edge struct {
	a string
	b string
}

type disjointSet struct {
	parent        map[string]string
	size          map[string]int
	numComponents int
}

func (d *disjointSet) root(node string) string {
	if d.parent[node] == node {
		return node
	}
	result := d.root(d.parent[node])
	d.parent[node] = result
	return result
}

func (d *disjointSet) union(a, b string) {
	r1, r2 := d.root(a), d.root(b)
	if r1 == r2 {
		return
	}
	if d.size[r1] < d.size[r2] {
		r1, r2 = r2, r1
	}
	d.parent[r2] = r1
	d.size[r1] += d.size[r2]
	d.numComponents -= 1
}

func djs(nodes []string) *disjointSet {
	parent := make(map[string]string, len(nodes))
	for _, node := range nodes {
		parent[node] = node
	}
	size := make(map[string]int, len(nodes))
	for _, node := range nodes {
		size[node] = 1
	}

	return &disjointSet{parent, size, len(nodes)}
}

// https://en.wikipedia.org/wiki/Karger's_algorithm
func (g graph) kargers() int {
	for {
		djs := djs(g.nodes)
		for djs.numComponents > 2 {
			// pick a random edge
			e := g.edges[rand.Intn(len(g.edges))]
			a, b := e.a, e.b
			// contract, noop if a and b are already in the same component
			djs.union(a, b)
		}

		// filter out edges that do not cross components
		minCutEdges := []edge{}
		for _, e := range g.edges {
			a, b := e.a, e.b
			if djs.root(a) != djs.root(b) {
				minCutEdges = append(minCutEdges, e)
			}
		}

		if len(minCutEdges) == 3 {
			fmt.Println("min cut of length 3 found:")
			fmt.Println(minCutEdges)
			a, b := minCutEdges[0].a, minCutEdges[0].b
			return djs.size[djs.root(a)] * djs.size[djs.root(b)]
		}
		fmt.Println(minCutEdges)
	}
}

func partOne(lines []string) error {
	g := parseGraph(lines)

	// answer: 562912
	fmt.Println(g.kargers())

	return nil
}

func partTwo(lines []string) error {
	return errors.New("part not implemented")
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
