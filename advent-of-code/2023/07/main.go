package main

import (
	"fmt"
	"sort"
	"util"
)

type card string

type hand struct {
	cards []card
	bid   int
}

type ByHand []hand

func (b ByHand) Len() int               { return len(b) }
func (b ByHand) Swap(i int, j int)      { b[i], b[j] = b[j], b[i] }
func (b ByHand) Less(i int, j int) bool { return b[i].less(b[j]) }

type handType int

const (
	fiveKind  handType = 7
	fourKind  handType = 6
	fullHouse handType = 5
	threeKind handType = 4
	twoPair   handType = 3
	onePair   handType = 2
	highCard  handType = 1
)

func (ht handType) less(ht2 handType) bool { return ht < ht2 }

func (h hand) handType() handType {
	hCounts := make(map[card]int)
	for _, c := range h.cards {
		if _, ok := hCounts[c]; !ok {
			hCounts[c] = 0
		}
		hCounts[c] += 1
	}
	// must be five of a kind
	if len(hCounts) == 1 {
		return fiveKind
	}
	// can be four of a kind or a full house
	if len(hCounts) == 2 {
		for _, count := range hCounts {
			if count == 4 {
				return fourKind
			}
		}
		return fullHouse
	}
	// can be three of a kind or two pair
	if len(hCounts) == 3 {
		for _, count := range hCounts {
			if count == 3 {
				return threeKind
			}
		}
		return twoPair
	}
	// must be one pair
	if len(hCounts) == 4 {
		return onePair
	}
	// must be high card
	return highCard
}

var pointValues = map[card]int{
	"2": 2, "3": 3, "4": 4, "5": 5,
	"6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
	"J": 11, "Q": 12, "K": 13, "A": 14,
}

func (h hand) labelLess(h2 hand) bool {
	for i := 0; i < 5; i++ {
		hCard := h.cards[i]
		h2Card := h2.cards[i]
		if hCard != h2Card {
			return pointValues[hCard] < pointValues[h2Card]
		}
	}
	panic("identical hands")
}

func (h hand) less(h2 hand) bool {
	hHandType := h.handType()
	h2HandType := h2.handType()
	if hHandType != h2HandType {
		return hHandType.less(h2HandType)
	} else {
		return h.labelLess(h2)
	}
}

type ByJokerHand []hand

func (b ByJokerHand) Len() int               { return len(b) }
func (b ByJokerHand) Swap(i int, j int)      { b[i], b[j] = b[j], b[i] }
func (b ByJokerHand) Less(i int, j int) bool { return b[i].jokerLess(b[j]) }

func (h hand) jokerHandType() handType {
	hCounts := make(map[card]int)
	for _, c := range h.cards {
		if _, ok := hCounts[c]; !ok {
			hCounts[c] = 0
		}
		hCounts[c] += 1
	}
	// must be five of a kind
	if len(hCounts) == 1 {
		return fiveKind
	}
	// 4 and 1 counts:
	//   can be four of a kind
	//   can be five of a kind (if either 4 count or 1 count is joker)
	//     four jokers match 1 count, or one joker matches 4 count
	// 3 and 2 counts:
	//   can be a full house
	//   can be five of a kind (if either 3 count or 2 count is joker)
	//     three jokers match 2 count, or two jokers match 3 count
	// => if any joker is seen, the hand can be five of a kind
	if len(hCounts) == 2 {
		for c := range hCounts {
			if c == "J" {
				return fiveKind
			}
		}
		for _, count := range hCounts {
			if count == 4 {
				return fourKind
			}
		}
		return fullHouse
	}
	// 3 and 1 and 1 counts:
	//   can be three of a kind
	//   can be four of a kind (if either 3 count or 1 count or 1 count is joker)
	//     one joker matches 3 count, or three jokers match either 1 count
	// 2 and 2 and 1 counts:
	//   can be two pair
	//   can be four of a kind (if either 2 count or 2 count is joker)
	//     two jokers match the other 2 count
	//   can be full house (if 1 count is joker)
	//     one joker matches either 2 count
	if len(hCounts) == 3 {
		isThreeOneOne := false
		for _, count := range hCounts {
			if count == 3 {
				isThreeOneOne = true
				break
			}
		}
		if isThreeOneOne {
			for c := range hCounts {
				if c == "J" {
					return fourKind
				}
			}
			return threeKind
		} else {
			for c, count := range hCounts {
				if c == "J" {
					if count == 2 {
						return fourKind
					} else {
						return fullHouse
					}
				}
			}
			return twoPair
		}
	}
	// 2 and 1 and 1 and 1 counts:
	//   can be one pair
	//   can be three of a kind (if 2 count is joker or 1 count or 1 count or 1 count is joker)
	//     two jokers match any 1 count, or 1 joker matches 2 count
	// => if any joker is seen, the hand can be three of a kind
	if len(hCounts) == 4 {
		for c := range hCounts {
			if c == "J" {
				return threeKind
			}
		}
		return onePair
	}
	// 1 and 1 and 1 and 1 and 1 counts:
	//   can be high card
	//   can be one pair (if 1 count or 1 count or 1 count or 1 count or 1 count is joker)
	//     one joker matches any 1 count
	for c := range hCounts {
		if c == "J" {
			return onePair
		}
	}
	return highCard
}

var jokerPointValues = map[card]int{
	"J": 1, "2": 2, "3": 3, "4": 4, "5": 5,
	"6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
	"Q": 12, "K": 13, "A": 14,
}

func (h hand) jokerLabelLess(h2 hand) bool {
	for i := 0; i < 5; i++ {
		hCard := h.cards[i]
		h2Card := h2.cards[i]
		if hCard != h2Card {
			return jokerPointValues[hCard] < jokerPointValues[h2Card]
		}
	}
	panic("identical hands")
}

func (h hand) jokerLess(h2 hand) bool {
	hHandType := h.jokerHandType()
	h2HandType := h2.jokerHandType()
	if hHandType != h2HandType {
		return hHandType.less(h2HandType)
	} else {
		return h.jokerLabelLess(h2)
	}
}

func partOne(lines []string) error {
	hands := parseHands(lines)
	sort.Sort(ByHand(hands))

	result := 0
	for i, h := range hands {
		rank := i + 1
		result += rank * h.bid
	}

	// answer: 253910319
	fmt.Println(result)

	return nil
}

func partTwo(lines []string) error {
	hands := parseHands(lines)
	sort.Sort(ByJokerHand(hands))

	result := 0
	for i, h := range hands {
		rank := i + 1
		result += rank * h.bid
	}

	// answer: 254083736
	fmt.Println(result)

	return nil
}

func main() {
	util.ParseAndRun(partOne, partTwo)
}
