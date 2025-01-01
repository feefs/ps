package main

import (
	"fmt"
	"strconv"
	"util"

	"github.com/emicklei/dot"
)

type wire string

type input struct {
	value int
}

type variant int

const (
	and variant = iota
	or
	xor
)

type gate struct {
	inputs  [2]wire
	variant variant
}

type circuit struct {
	elements map[wire]any
	zWires   []wire
}

func (c circuit) eval(w wire) int {
	switch e := c.elements[w].(type) {
	case input:
		return e.value
	case gate:
		i1, i2 := c.eval(e.inputs[0]), c.eval(e.inputs[1])
		switch e.variant {
		case and:
			return i1 & i2
		case or:
			return i1 | i2
		case xor:
			return i1 ^ i2
		}
	}
	panic("unreachable")
}

func partOne(lines []string) error {
	circuit := parseCircuit(lines)

	result := 0
	for offset, zw := range circuit.zWires {
		result |= circuit.eval(zw) << offset
	}

	// answer: 49520947122770
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	circuit := parseCircuit(lines)

	// go run . --part=2 | dot -Tpng -o graph.png
	// inspect the graph and fix the input manually
	graph := dot.NewGraph(dot.Directed)
	graph.Attr("newrank", "true")
	inputs := graph.Subgraph("inputs", dot.ClusterOption{})

	nodes := map[wire]dot.Node{}
	for w := range circuit.elements {
		switch w[0] {
		case 'x':
			nodes[w] = inputs.Node(string(w)).Attr("color", "blue")
		case 'y':
			nodes[w] = inputs.Node(string(w)).Attr("color", "purple")
		default:
			nodes[w] = graph.Node(string(w))
		}
	}
	for _, zw := range circuit.zWires {
		nodes[zw] = graph.Node(string(zw)).Attr("color", "red")
	}
	for i := range len(circuit.zWires) - 1 {
		o1, o2 := circuit.zWires[i], circuit.zWires[i+1]
		graph.Edge(nodes[o1], nodes[o2]).Attr("color", "white")
	}

	id := -1
	genID := func() string {
		id += 1
		return "gate" + strconv.Itoa(id)
	}
	for l, e := range circuit.elements {
		if g, ok := e.(gate); ok {
			n1, n2 := nodes[g.inputs[0]], nodes[g.inputs[1]]

			gn := graph.Node(genID())
			on := graph.Node(string(l))

			graph.Edge(n1, gn)
			graph.Edge(n2, gn)
			graph.Edge(gn, on).Attr("color", "pink")

			switch g.variant {
			case and:
				gn.Label("&")
			case or:
				gn.Label("|")
			case xor:
				gn.Label("^")
			}
		}
	}

	fmt.Print(graph.String())

	// swaps:
	// gjc, qjj (near z11)
	// wmp, z17
	// gvm, z26
	// z39, qsb

	// answer: gjc,gvm,qjj,qsb,wmp,z17,z26,z39

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
