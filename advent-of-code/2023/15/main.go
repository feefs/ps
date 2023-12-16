package main

import (
	"container/list"
	"fmt"
	"regexp"
	"strconv"
	"util"
)

func hash[T ~string](s T) int {
	curr := 0
	for _, r := range s {
		curr += int(r)
		curr = (curr * 17) % 256
	}

	return curr
}

type step string

func (s step) hash() int {
	return hash(s)
}

type operation rune

const (
	dash   operation = '-'
	equals operation = '='
)

type instruction struct {
	label       string
	operation   operation
	focalLength int
}

func (s step) parseInstruction() instruction {
	r := regexp.MustCompile(`(\w+)(\-|\=)(\d)?`)
	match := r.FindStringSubmatch(string(s))

	label, op, fl := match[1], operation(match[2][0]), match[3]
	focalLength, _ := strconv.Atoi(fl)

	return instruction{
		label:       label,
		operation:   op,
		focalLength: focalLength,
	}
}

func (inst instruction) boxNum() int {
	return hash(inst.label)
}

type box struct {
	instructions []instruction
}

func (b box) lenses() *list.List {
	lenses := list.New()
	lensReferences := map[string]*list.Element{}
	for _, inst := range b.instructions {
		if inst.operation == dash {
			if ref, ok := lensReferences[inst.label]; ok {
				lenses.Remove(ref)
				delete(lensReferences, inst.label)
			}
		} else {
			if ref, ok := lensReferences[inst.label]; ok {
				ref.Value = inst.focalLength
			} else {
				lensReferences[inst.label] = lenses.PushBack(inst.focalLength)
			}
		}
	}

	return lenses
}

func (b box) totalFocusingPower(boxNum int) int {
	lenses := b.lenses()
	result := 0
	multiplier := 1 + boxNum
	slotNumber := 1
	for e := lenses.Front(); e != nil; e = e.Next() {
		v, _ := e.Value.(int)
		result += multiplier * slotNumber * v
		slotNumber += 1
	}

	return result
}

func partOne(lines []string) error {
	steps := parseSteps(lines)

	result := 0
	for _, s := range steps {
		result += s.hash()
	}

	// answer: 506437
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	steps := parseSteps(lines)

	boxes := make([]box, 256)
	for _, s := range steps {
		inst := s.parseInstruction()
		boxNum := inst.boxNum()
		boxes[boxNum].instructions = append(boxes[boxNum].instructions, inst)
	}

	result := 0
	for boxNum, box := range boxes {
		result += box.totalFocusingPower(boxNum)
	}

	// answer: 288521
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
