import os
from enum import Enum
import ast

class Result(Enum):
  VALID = 1
  INVALID = 2
  UNKNOWN = 3

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

lines = f.read().split()

def validate_packet(first, second):
  i = 0
  while i < min(len(first), len(second)):
    l, r = first[i], second[i]
    if type(l) == int and type(r) == int:
      if l < r:
        return Result.VALID
      if l > r:
        return Result.INVALID
      i += 1
    elif type(l) == list and type(r) == list:
      result = validate_packet(l, r)
      if result != Result.UNKNOWN:
        return result
      i += 1
    else:
      if type(l) == int:
        first[i] = [l]
      else:
        second[i] = [r]
  if len(first) == len(second):
    return Result.UNKNOWN
  else:
    return Result.VALID if len(first) < len(second) else Result.INVALID

divider_one, divider_two = [[2]], [[6]]
before_divider_one, between_dividers = 0, 0
for l in lines:
  packet = ast.literal_eval(l.strip())
  result_one = validate_packet(packet, divider_one)
  result_two = validate_packet(packet, divider_two)
  if result_one == Result.VALID:
    before_divider_one += 1
  elif result_two == Result.VALID:
    between_dividers += 1

# answer: 25935
print((before_divider_one + 1) * (before_divider_one + between_dividers + 2))
