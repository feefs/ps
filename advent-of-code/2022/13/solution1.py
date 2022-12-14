import os
from enum import Enum
from ast import literal_eval

class Result(Enum):
  VALID = 1
  INVALID = 2
  UNKNOWN = 3

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

groups = f.read().split("\n\n")

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

valid_indices = []
for i, g in enumerate(groups, 1):
  first, second = g.splitlines()
  first, second = literal_eval(first), literal_eval(second)
  if validate_packet(first, second) == Result.VALID:
    valid_indices.append(i)

# answer: 5717
print(sum(valid_indices))
