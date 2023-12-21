package main

import (
	"regexp"
	"strings"
)

func parse(lines []string) (modules map[moduleName]module, broadcastModuleNames []moduleName) {
	modules = make(map[moduleName]module)
	broadcastModuleNames = []moduleName{}

	r := regexp.MustCompile(`(%|&)?(\w+) -> (.*)`)
	for _, line := range lines {
		match := r.FindStringSubmatch(line)

		moduleType := match[1]
		name := moduleName(match[2])
		dstStrings := strings.Split(match[3], ", ")
		dsts := []moduleName{}
		for _, d := range dstStrings {
			dsts = append(dsts, moduleName(d))
		}

		switch moduleType {
		case "%":
			on := false
			modules[name] = flipFlop{name: name, dstNames: dsts, on: &on}
		case "&":
			modules[name] = conjunction{name: name, dstNames: dsts, memory: make(map[moduleName]pulse)}
		default:
			broadcastModuleNames = dsts
		}
	}

	// initialize memory for all conjunctions
	for srcName, m := range modules {
		for _, dstName := range m.destinationNames() {
			if dst, ok := modules[dstName].(conjunction); ok {
				dst.memory[srcName] = loPulse
			}
		}
	}

	return modules, broadcastModuleNames
}
