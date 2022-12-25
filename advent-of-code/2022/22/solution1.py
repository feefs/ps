import os
from enum import Enum
from collections import defaultdict
import itertools
import re

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

board, moves = f.read().split('\n\n')

tiles, walls = set(), set()
start = (float('inf'), float('inf'))
m, n = 0, 0
for i, row in enumerate(board.splitlines()):
  m = i
  for j in range(len(row)):
    c = row[j]
    if not c.isspace():
      if j > n:
        n = j
      if c == '.':
        tiles.add((i, j))
        if (i, j) < start:
          start = (i, j)
      else:
        walls.add((i, j))

m, n = m + 1, n + 1

class Direction(Enum):
  LEFT = 1
  RIGHT = 2
  UP = 3
  DOWN = 4

jump = defaultdict(dict)
void = set(itertools.product(range(-1, m + 1), range(-1,
                                                     n + 1))) - tiles - walls
for i in range(m):
  for j in range(n):
    if (i, j) in void or (i, j) in walls:
      continue
    if (i - 1, j) in void:
      for l in reversed(range(m)):
        if (l, j) not in void:
          jump[(i, j)][Direction.UP] = (l, j)
          break
    if (i + 1, j) in void:
      for l in range(m):
        if (l, j) not in void:
          jump[(i, j)][Direction.DOWN] = (l, j)
          break
    if (i, j - 1) in void:
      for k in reversed(range(n)):
        if (i, k) not in void:
          jump[(i, j)][Direction.LEFT] = (i, k)
          break
    if (i, j + 1) in void:
      for k in range(n):
        if (i, k) not in void:
          jump[(i, j)][Direction.RIGHT] = (i, k)
          break

def next_coord(direction, coord):
  i, j = coord
  if direction == Direction.LEFT:
    return (i, j - 1)
  elif direction == Direction.DOWN:
    return (i + 1, j)
  elif direction == Direction.RIGHT:
    return (i, j + 1)
  else:
    return (i - 1, j)

def rotate_left(direction):
  if direction == Direction.LEFT:
    return Direction.DOWN
  elif direction == Direction.DOWN:
    return Direction.RIGHT
  elif direction == Direction.RIGHT:
    return Direction.UP
  else:
    return Direction.LEFT

def rotate_right(direction):
  if direction == Direction.LEFT:
    return Direction.UP
  elif direction == Direction.UP:
    return Direction.RIGHT
  elif direction == Direction.RIGHT:
    return Direction.DOWN
  else:
    return Direction.LEFT

curr_coord = start
curr_direction = Direction.RIGHT
for action in re.findall(r"(\d+|[L|R])", moves.strip()):
  if action.isnumeric():
    for _ in range(int(action)):
      nc = next_coord(curr_direction, curr_coord)
      if nc in tiles:
        curr_coord = nc
      elif curr_direction in jump[curr_coord]:
        nc = jump[curr_coord][curr_direction]
        if nc not in tiles:
          break
        curr_coord = nc
      else:
        break
  else:
    if action == 'L':
      curr_direction = rotate_left(curr_direction)
    else:
      curr_direction = rotate_right(curr_direction)

facing = {
    Direction.LEFT: 2,
    Direction.RIGHT: 0,
    Direction.UP: 3,
    Direction.DOWN: 1
}

# answer: 27436
print(((curr_coord[0] + 1) * 1000) + ((curr_coord[1] + 1) * 4) +
      facing[curr_direction])
