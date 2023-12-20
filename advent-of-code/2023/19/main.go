package main

import (
	"fmt"
	"runtime"
	"slices"
	"util"
)

type category string

const (
	extremely   category = "x"
	musical     category = "m"
	aerodynamic category = "a"
	shiny       category = "s"
)

type operation string

const (
	gt operation = ">"
	lt operation = "<"
)

type target string

const (
	accept target = "A"
	reject target = "R"
)

type step struct {
	cat category
	op  operation
	val int
	tg  target
}

func (s step) process(p part) (tg target, next bool) {
	switch s.op {
	case gt:
		if p.ratings[s.cat] > s.val {
			return s.tg, false
		} else {
			return target(""), true
		}
	case lt:
		if p.ratings[s.cat] < s.val {
			return s.tg, false
		} else {
			return target(""), true
		}
	}
	// noop
	return s.tg, false
}

type workflow struct {
	steps []step
}

type part struct {
	ratings map[category]int
}

func process(workflows map[target]workflow, p part) bool {
	curr := target("in")
	for {
		if curr == accept || curr == reject {
			return curr == accept
		}
		wf := workflows[curr]
		for _, s := range wf.steps {
			tg, next := s.process(p)
			curr = tg
			if !next {
				break
			}
		}
	}
}

func partOne(lines []string) error {
	workflows, parts := parse(lines)

	result := 0
	for _, p := range parts {
		if process(workflows, p) {
			for _, v := range p.ratings {
				result += v
			}
		}
	}

	// answer: 399284
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	workflows, _ := parse(lines)

	splits := map[category]([]int){
		extremely:   []int{0, 4000},
		musical:     []int{0, 4000},
		aerodynamic: []int{0, 4000},
		shiny:       []int{0, 4000},
	}
	// search all workflow steps for split points
	for _, wf := range workflows {
		for _, s := range wf.steps {
			if len(s.op) > 0 {
				splitValue := s.val
				if s.op == lt {
					splitValue -= 1
				}
				splits[s.cat] = append(splits[s.cat], splitValue)
			}
		}
	}
	for _, s := range splits {
		slices.Sort(s)
	}

	x, m, a, s := splits[extremely], splits[musical], splits[aerodynamic], splits[shiny]

	innerResults := make(chan int)
	cpus := runtime.NumCPU()
	for cid := 0; cid < cpus; cid++ {
		width := (len(x) - 1) / cpus
		start := cid * width
		end := start + width
		if cid == cpus-1 {
			end = len(x) - 1
		}

		go func(start, end, cid int) {
			innerResult := 0
			prevThreshold := -3
			for xi := start; xi < end; xi++ {
				percent := ((xi - start) * 100) / (end - start)
				if percent >= prevThreshold+3 {
					fmt.Printf("goroutine %v is %v%% done\n", cid, percent)
					prevThreshold += 3
				}

				// compute if every combination of splits will be accepted or not
				x, dx := x[xi+1], x[xi+1]-x[xi]
				for mi := 0; mi < len(m)-1; mi++ {
					m, dm := m[mi+1], m[mi+1]-m[mi]
					for ai := 0; ai < len(a)-1; ai++ {
						a, da := a[ai+1], a[ai+1]-a[ai]
						for si := 0; si < len(s)-1; si++ {
							s, ds := s[si+1], s[si+1]-s[si]
							if process(workflows, part{map[category]int{
								extremely:   x,
								musical:     m,
								aerodynamic: a,
								shiny:       s,
							}}) {
								innerResult += dx * dm * da * ds
							}
						}
					}
				}
			}
			fmt.Printf("goroutine %v has finished!\n", cid)
			innerResults <- innerResult
		}(start, end, cid)
	}

	result := 0
	for c := 0; c < cpus; c++ {
		result += <-innerResults
	}

	// answer: 121964982771486
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
