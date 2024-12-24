package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
	"util"
)

type computer struct {
	A            int
	B            int
	C            int
	instructions []int
	ip           int
}

type opcode int

var (
	adv opcode = 0
	bxl opcode = 1
	bst opcode = 2
	jnz opcode = 3
	bxc opcode = 4
	out opcode = 5
	bdv opcode = 6
	cdv opcode = 7
)

func (c computer) literalOperand() int {
	return c.instructions[c.ip+1]
}

func (c computer) comboOperand() int {
	operand := c.instructions[c.ip+1]
	if 0 <= operand && operand <= 3 {
		return operand
	}
	if operand == 4 {
		return c.A
	}
	if operand == 5 {
		return c.B
	}
	if operand == 6 {
		return c.C
	}
	panic(fmt.Sprintf("unknown combo operand: %v", operand))
}

func (c *computer) tick(stdout *[]int) {
	switch opcode(c.instructions[c.ip]) {
	case adv:
		c.A >>= c.comboOperand()
	case bxl:
		c.B ^= c.literalOperand()
	case bst:
		c.B = c.comboOperand() % 8
	case jnz:
		if c.A != 0 {
			c.ip = c.literalOperand()
			return
		}
	case bxc:
		c.B = c.B ^ c.C
	case out:
		*stdout = append(*stdout, c.comboOperand()%8)
	case bdv:
		c.B = c.A >> c.comboOperand()
	case cdv:
		c.C = c.A >> c.comboOperand()
	}
	c.ip += 2
}

func (c *computer) run() []int {
	c.ip = 0
	output := []int{}
	for c.ip < len(c.instructions) {
		c.tick(&output)
	}
	return output
}

func partOne(lines []string) error {
	computer := parseComputer(lines)

	output := computer.run()

	values := make([]string, len(output))
	for i, o := range output {
		values[i] = strconv.Itoa(o)
	}

	result := strings.Join(values, ",")

	// answer: 7,6,5,3,6,5,7,0,4
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	/*
		program analysis:
		2,4: B <- A % 8  (last 3 bits of A)
		1,2: B <- B ^ 2
		7,5: C <- A >> B  (floor divide by 2**B)
		0,3: A <- A >> 3  (floor divide by 2**3)
		1,7: B <- B ^ 7
		4,1: B <- B ^ C
		5,5: out <- B % 8 (last 3 bits of B)
		3,0: jnz 0

		because each iteration only depends on the last 3 bits of A,
		brute force 3 bits at a time to reconstruct A

		since C depends on the value of A before 3 bits of it are right shifted,
		it's possible to encounter a "dead end" if implemented iteratively.
		this happens if no values of A in the next iteration lead to the desired output.

		therefore, we use recursion to explore different values of A
	*/

	computer := parseComputer(lines)

	var f func(A uint, offset uint) (uint, bool)
	f = func(A uint, offset uint) (uint, bool) {
		if int(offset) == len(computer.instructions) {
			return A >> 3, true
		}
		clearMask := ^uint(0b111)
		for x := uint(0); x < 8; x++ {
			A &= clearMask
			A |= x
			computer.A = int(A)
			output := computer.run()
			if !slices.Equal(output, computer.instructions[len(computer.instructions)-1-int(offset):]) {
				continue
			}
			if result, ok := f(A<<3, offset+1); ok {
				return result, ok
			}
		}
		return uint(0), false
	}

	result, ok := f(0, 0)
	if !ok {
		return util.InvalidStateError("a solution must exist for the input")
	}

	// answer: 190615597431823
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
