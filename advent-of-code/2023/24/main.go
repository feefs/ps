package main

import (
	"fmt"
	"math/rand"
	"sort"
	"util"

	"gonum.org/v1/gonum/mat"
)

type position struct {
	x float64
	y float64
	z float64
}

type velocity struct {
	dx float64
	dy float64
	dz float64
}

type hailstone struct {
	pos position
	vel velocity
}

type point struct {
	x float64
	y float64
}

func (h hailstone) intersects(h2 hailstone) *point {
	/*
		y - y1 = s1(x - x1)
		y - y2 = s2(x - x2)

		y = s1(x - x1) + y1 = s2(x - x2) + y2
		(s1 * x) - (s1 * x1) + y1 = (s2 * x) - (s2 * x2) + y2
		x(x1 - s2) = (s1 * x1) - y1 + (s2 * x2) + y2
		x = [(s1 * x1) - y1 - (s2 * x2) + y2] / (s1 - s2)
	*/
	x1, y1 := h.pos.x, h.pos.y
	x2, y2 := h2.pos.x, h2.pos.y
	s1 := h.vel.dy / h.vel.dx
	s2 := h2.vel.dy / h2.vel.dx

	if s1 == s2 {
		return nil
	}

	x := ((s1 * x1) - y1 - (s2 * x2) + y2) / (s1 - s2)
	y := (s1 * (x - x1)) + y1

	return &point{x, y}
}

func inFuture(intersection point, h1 hailstone, h2 hailstone) bool {
	/*
		h1.pos.x + (t1 * h1.vel.dx) = intersection.x
		h2.pos.x + (t2 * h2.vel.dx) = intersection.x

		t1 = (intersection.x - h1.pos.x) / h1.vel.dx
		t2 = (intersection.x - h2.pos.x) / h2.vel.dx
	*/
	t1 := (intersection.x - h1.pos.x) / h1.vel.dx
	t2 := (intersection.x - h2.pos.x) / h2.vel.dx

	return t1 > 0 && t2 > 0
}

type leftValuesFunc func(hailstone, hailstone) []float64
type rightValueFunc func(hailstone, hailstone) float64

// X(dy' - dy) + Y(dx - dx') + DX(y - y') + DY(x' - x) = (x' * dy') - (y' * dx') - (x * dy) + (y * dx)
// solves for X, Y, DX, and DY
func solveXY(h1, h2, h3, h4, h5 hailstone) (X, Y, DX, DY float64) {
	var lvf leftValuesFunc = func(hailstoneA, hailstoneB hailstone) []float64 {
		x, y, dx, dy := hailstoneA.pos.x, hailstoneA.pos.y, hailstoneA.vel.dx, hailstoneA.vel.dy
		x1, y1, dx1, dy1 := hailstoneB.pos.x, hailstoneB.pos.y, hailstoneB.vel.dx, hailstoneB.vel.dy
		return []float64{dy1 - dy, dx - dx1, y - y1, x1 - x}
	}

	var rvf rightValueFunc = func(hailstoneA, hailstoneB hailstone) float64 {
		x, y, dx, dy := hailstoneA.pos.x, hailstoneA.pos.y, hailstoneA.vel.dx, hailstoneA.vel.dy
		x1, y1, dx1, dy1 := hailstoneB.pos.x, hailstoneB.pos.y, hailstoneB.vel.dx, hailstoneB.vel.dy
		return (x1 * dy1) - (y1 * dx1) - (x * dy) + (y * dx)
	}

	x := solve(lvf, rvf, h1, h2, h3, h4, h5)

	return x.AtVec(0), x.AtVec(1), x.AtVec(2), x.AtVec(3)
}

// X(dz' - dz) + Z(dx - dx') + DX(z - z') + DZ(x' - x) = (x' * dz') - (z' * dx') - (x * dz) + (z * dx)
// solves for X, Z, DX, and DZ
func solveXZ(h1, h2, h3, h4, h5 hailstone) (X, Z, DX, DZ float64) {
	var lvf leftValuesFunc = func(hailstoneA, hailstoneB hailstone) []float64 {
		x, z, dx, dz := hailstoneA.pos.x, hailstoneA.pos.z, hailstoneA.vel.dx, hailstoneA.vel.dz
		x1, z1, dx1, dz1 := hailstoneB.pos.x, hailstoneB.pos.z, hailstoneB.vel.dx, hailstoneB.vel.dz
		return []float64{dz1 - dz, dx - dx1, z - z1, x1 - x}
	}

	var rvf rightValueFunc = func(hailstoneA, hailstoneB hailstone) float64 {
		x, z, dx, dz := hailstoneA.pos.x, hailstoneA.pos.z, hailstoneA.vel.dx, hailstoneA.vel.dz
		x1, z1, dx1, dz1 := hailstoneB.pos.x, hailstoneB.pos.z, hailstoneB.vel.dx, hailstoneB.vel.dz
		return (x1 * dz1) - (z1 * dx1) - (x * dz) + (z * dx)
	}

	x := solve(lvf, rvf, h1, h2, h3, h4, h5)

	return x.AtVec(0), x.AtVec(1), x.AtVec(2), x.AtVec(3)
}

func solve(lvf leftValuesFunc, rvf rightValueFunc, h1, h2, h3, h4, h5 hailstone) mat.VecDense {
	AValues := []float64{}
	AValues = append(AValues, lvf(h1, h2)...)
	AValues = append(AValues, lvf(h1, h3)...)
	AValues = append(AValues, lvf(h1, h4)...)
	AValues = append(AValues, lvf(h1, h5)...)
	A := mat.NewDense(4, 4, AValues)
	b := mat.NewVecDense(4, []float64{
		rvf(h1, h2),
		rvf(h1, h3),
		rvf(h1, h4),
		rvf(h1, h5),
	})
	var x mat.VecDense
	_ = x.SolveVec(A, b)

	return x
}

func partOne(lines []string) error {
	hailstones := parseHailstones(lines)

	lowerBound := 200_000_000_000_000.0
	upperBound := 400_000_000_000_000.0

	result := 0
	for i := 0; i < len(hailstones); i++ {
		for j := i + 1; j < len(hailstones); j++ {
			h1, h2 := hailstones[i], hailstones[j]
			pt := h1.intersects(h2)
			if pt == nil {
				continue
			}
			if !inFuture(*pt, h1, h2) {
				continue
			}
			if lowerBound <= pt.x && pt.x <= upperBound && lowerBound <= pt.y && pt.y <= upperBound {
				result += 1
			}
		}
	}

	// answer: 20361
	fmt.Println(result)
	return nil
}

func partTwo(lines []string) error {
	/*
		X   Y   Z   and DX   DY   DZ   = position and velocity of thrown rock
		x   y   z   and dx   dy   dz   = position and velocity of hailstone 1
		x'  y'  z'  and dx'  dy'  dz'  = position and velocity of hailstone 2
		...

		X + (t * DX) = x + (t * dx)
		t = (x - X) / (DX - dx) = (y - Y) / (DY - dy)
		(Y * DX) - (X * DY) = (x * dy) - (y * dx) + (Y * dx) + (y * DX) - (x * DY) - (X * dy)

		do the same for the rock with hailstone 2
		(Y * DX) - (X * DY) = (x' * dy') - (y' * dx') + (Y * dx') + (y' * DX) - (x' * DY) - (X * dy')

		the LHS of both equations is (Y * DX) - (X * DY)
		(x * dy) - (y * dx) + (Y * dx) + (y * DX) - (x * DY) - (X * dy) = (x' * dy') - (y' * dx') + (Y * dx') + (y' * DX) - (x' * DY) - (X * dy')
		X(dy' - dy) + Y(dx - dx') + DX(y - y') + DY(x' - x) = (x' * dy') - (y' * dx') - (x * dy) + (y * dx)

		all lower case variables are known from hailstone 1 and 2
		to solve for unknowns X, Y, DX, DY, repeat the process with 3 other hailstone pairs to generate 4 equations in total

		repeat the above process to find Z and DZ (solve for unknowns X, Z, DX, DZ)
		X(dz' - dz) + Z(dx - dx') + DX(z - z') + DZ(x' - x) = (x' * dz') - (z' * dx') - (x * dz) + (z * dx)
		technically there are now only two unknowns so a new set of equations can be written
			but it's easier to implement the same thing twice
	*/
	hailstones := parseHailstones(lines)

	counts := map[int]int{}
	for seed := 0; seed < 100; seed++ {
		picked := []hailstone{}
		r := rand.New(rand.NewSource(int64(seed))) // adjustable random seed to get past numerical instability
		for n := 0; n < 5; n++ {
			picked = append(picked, hailstones[r.Intn(len(hailstones))])
		}
		h1, h2, h3, h4, h5 := picked[0], picked[1], picked[2], picked[3], picked[4]

		X, Y, _, _ := solveXY(h1, h2, h3, h4, h5)
		_, Z, _, _ := solveXZ(h1, h2, h3, h4, h5)

		result := int(X + Y + Z)
		if _, ok := counts[result]; !ok {
			counts[result] = 0
		}
		counts[result] += 1
	}

	type result struct {
		value int
		count int
	}
	results := []result{}
	for val, count := range counts {
		results = append(results, result{value: val, count: count})
	}
	sort.Slice(results, func(i, j int) bool {
		return results[i].count > results[j].count
	})

	fmt.Println("top 5 results by count:")
	for _, r := range results[:5] {
		fmt.Printf("%v - %v\n", r.value, r.count)
	}
	fmt.Println()

	// answer: 558415252330828
	fmt.Println(results[0].value)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
