import os
from enum import Enum

class Move(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

class Outcome(Enum):
  LOSE = 1
  DRAW = 2
  WIN = 3

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))
move_mappings = {'A': Move.ROCK, 'B': Move.PAPER, 'C': Move.SCISSORS}
move_score_mappings = {Move.ROCK: 1, Move.PAPER: 2, Move.SCISSORS: 3}
outcome_mappings = {'X': Outcome.LOSE, 'Y': Outcome.DRAW, 'Z': Outcome.WIN}
outcome_score_mappings = {Outcome.LOSE: 0, Outcome.DRAW: 3, Outcome.WIN: 6}

score = 0
for l in f:
  opponent_encoded_move, encoded_outcome = l.strip().split()
  opponent_move, outcome = move_mappings[
      opponent_encoded_move], outcome_mappings[encoded_outcome]

  move = None
  outcome_score = outcome_score_mappings[outcome]
  if outcome == Outcome.LOSE:
    if opponent_move == Move.ROCK:
      move = Move.SCISSORS
    elif opponent_move == Move.PAPER:
      move = Move.ROCK
    else:
      move = Move.PAPER
  elif outcome == outcome.DRAW:
    if opponent_move == Move.ROCK:
      move = Move.ROCK
    elif opponent_move == Move.PAPER:
      move = Move.PAPER
    else:
      move = Move.SCISSORS
  else:
    if opponent_move == Move.ROCK:
      move = Move.PAPER
    elif opponent_move == Move.PAPER:
      move = Move.SCISSORS
    else:
      move = Move.ROCK
  move_score = move_score_mappings[move]
  score += outcome_score + move_score

# answer: 14184
print(score)
