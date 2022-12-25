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
"""
edges are numbered 1-14 starting from the top middle one
edge connections
  1 - 10
  2 - 9
  3 - 6
  4 - 5
  7 - 8
  11 - 14
  12 - 13
"""
# map to the coordinate we would reappear to and the new direction
# 1-10, 10-1
for j in range(50, 100):
  jump[(0, j)][Direction.UP] = (150 + (j - 50), 0), Direction.RIGHT
for i in range(150, 200):
  jump[(i, 0)][Direction.LEFT] = (0, 50 + (i - 150)), Direction.DOWN

# 2-9, 9-2
for j in range(100, 150):
  jump[(0, j)][Direction.UP] = (199, 0 + (j - 100)), Direction.UP
for j in range(50):
  jump[(199, j)][Direction.DOWN] = (0, 100 + j), Direction.DOWN

# 3-6, 6-3
for i in range(50):
  jump[(i, 149)][Direction.RIGHT] = (149 - i, 99), Direction.LEFT
for i in range(100, 150):
  jump[(i, 99)][Direction.RIGHT] = (49 - (i - 100), 149), Direction.LEFT

# 4-5, 5-4
for j in range(100, 150):
  jump[(49, j)][Direction.DOWN] = (50 + (j - 100), 99), Direction.LEFT
for i in range(50, 100):
  jump[(i, 99)][Direction.RIGHT] = (49, 100 + (i - 50)), Direction.UP

# 7-8, 8-7
for j in range(50, 100):
  jump[(149, j)][Direction.DOWN] = (150 + (j - 50), 49), Direction.LEFT
for i in range(150, 200):
  jump[(i, 49)][Direction.RIGHT] = (149, 50 + (i - 150)), Direction.UP

# 11-14, 14-11
for i in range(100, 150):
  jump[(i, 0)][Direction.LEFT] = (49 - (i - 100), 50), Direction.RIGHT
for i in range(50):
  jump[(i, 50)][Direction.LEFT] = (149 - i, 0), Direction.RIGHT

# 12-13, 13-12
for j in range(50):
  jump[(100, j)][Direction.UP] = (50 + j, 50), Direction.RIGHT
for i in range(50, 100):
  jump[(i, 50)][Direction.LEFT] = (100, 0 + (i - 50)), Direction.DOWN

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
        nc, nd = jump[curr_coord][curr_direction]
        if nc not in tiles:
          break
        curr_coord, curr_direction = nc, nd
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

# answer: 15426
print(((curr_coord[0] + 1) * 1000) + ((curr_coord[1] + 1) * 4) +
      facing[curr_direction])
