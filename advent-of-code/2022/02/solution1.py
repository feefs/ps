import os
from enum import Enum

class Move(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

f = open(os.path.join(os.path.dirname(__file__), 'input.txt'))
mappings = {
    'A': Move.ROCK,
    'B': Move.PAPER,
    'C': Move.SCISSORS,
    'X': Move.ROCK,
    'Y': Move.PAPER,
    'Z': Move.SCISSORS
}
score_mappings = {Move.ROCK: 1, Move.PAPER: 2, Move.SCISSORS: 3}

score = 0
for l in f:
  opponent_encoded_move, encoded_move = l.strip().split()
  opponent_move, move = mappings[opponent_encoded_move], mappings[encoded_move]

  outcome_score = 0
  if move == opponent_move:
    outcome_score = 3
  else:
    if move == Move.ROCK:
      if opponent_move == Move.SCISSORS:
        outcome_score = 6
      else:
        outcome_score = 0
    elif move == Move.PAPER:
      if opponent_move == Move.ROCK:
        outcome_score = 6
      else:
        outcome_score = 0
    else:
      if opponent_move == Move.PAPER:
        outcome_score = 6
      else:
        outcome_score = 0
  score += outcome_score + score_mappings[move]

# answer: 13675
print(score)
