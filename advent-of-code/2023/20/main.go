package main

import (
	"fmt"
	"util"
)

type pulse int

const (
	loPulse pulse = iota + 1
	hiPulse
)

type moduleName string

type module interface {
	destinationNames() []moduleName
	tick(src moduleName, pulse pulse, q *[]action)
}

type action struct {
	srcName moduleName
	dstName moduleName
	p       pulse
}

func (a action) process(modules map[moduleName]module, q *[]action) {
	if dst, ok := modules[a.dstName]; ok {
		dst.tick(a.srcName, a.p, q)
	}
}

type flipFlop struct {
	name     moduleName
	dstNames []moduleName
	on       *bool
}

func (f flipFlop) destinationNames() []moduleName { return f.dstNames }
func (f flipFlop) tick(_ moduleName, pulse pulse, q *[]action) {
	if pulse == loPulse {
		if *f.on {
			for _, dstName := range f.dstNames {
				*q = append(*q, action{srcName: f.name, dstName: dstName, p: loPulse})
			}
			*f.on = false
		} else {
			for _, dstName := range f.dstNames {
				*q = append(*q, action{srcName: f.name, dstName: dstName, p: hiPulse})
			}
			*f.on = true
		}
	}
}

type conjunction struct {
	name     moduleName
	dstNames []moduleName
	memory   map[moduleName]pulse
}

func (c conjunction) destinationNames() []moduleName { return c.dstNames }
func (c conjunction) tick(src moduleName, pulse pulse, q *[]action) {
	c.memory[src] = pulse
	allHigh := true
	for _, p := range c.memory {
		if p == loPulse {
			allHigh = false
		}
	}
	if allHigh {
		for _, dst := range c.dstNames {
			*q = append(*q, action{srcName: c.name, dstName: dst, p: loPulse})
		}
	} else {
		for _, dst := range c.dstNames {
			*q = append(*q, action{srcName: c.name, dstName: dst, p: hiPulse})
		}
	}
}

func gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

func lcm(values ...int) int {
	a, b := values[0], values[1]
	v := (a * b) / gcd(a, b)
	if len(values) == 2 {
		return v
	}
	remaining := []int{v}
	remaining = append(remaining, values[2:]...)

	return lcm(remaining...)
}

func partOne(lines []string) error {
	modules, broadcastModuleNames := parse(lines)

	loCount, hiCount := 0, 0
	for i := 0; i < 1000; i++ {
		// count the low pulse sent to the broadcaster
		loCount += 1
		q := []action{}
		for _, dstName := range broadcastModuleNames {
			q = append(q, action{srcName: moduleName("broadcast"), dstName: dstName, p: loPulse})
		}
		for len(q) > 0 {
			curr := q[0]
			q = q[1:]
			if curr.p == loPulse {
				loCount += 1
			} else {
				hiCount += 1
			}
			curr.process(modules, &q)
		}
	}

	// answer: 867118762
	fmt.Println(loCount * hiCount)

	return nil
}

func partTwo(lines []string) error {
	modules, broadcastModuleNames := parse(lines)

	// manual graph analysis
	// for each of the 4 third to last modules in the graph
	//   find the cycle length for when it sends a high pulse
	// compute the lcm of these cycle lengths
	fv, kk, vt, xr := moduleName("fv"), moduleName("kk"), moduleName("vt"), moduleName("xr")
	targets := map[moduleName]struct{}{fv: {}, kk: {}, vt: {}, xr: {}}
	seen := map[moduleName]int{}
	periods := []int{}
out:
	for {
		buttonPresses := 0
		for {
			buttonPresses += 1
			q := []action{}
			for _, dstName := range broadcastModuleNames {
				q = append(q, action{srcName: moduleName("broadcast"), dstName: dstName, p: loPulse})
			}
			for len(q) > 0 {
				curr := q[0]
				q = q[1:]
				if _, ok := targets[curr.srcName]; ok && curr.p == hiPulse {
					if prevButtonPresses, ok := seen[curr.srcName]; ok {
						periods = append(periods, buttonPresses-prevButtonPresses)
						delete(targets, curr.srcName)
					} else {
						seen[curr.srcName] = buttonPresses
					}
				}
				curr.process(modules, &q)
				if len(targets) == 0 {
					break out
				}
			}
		}
	}

	// answer: 217317393039529
	fmt.Println(lcm(periods...))

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
