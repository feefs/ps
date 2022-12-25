import os
from enum import Enum
from collections import defaultdict, deque

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

class Direction(Enum):
  LEFT = 1
  RIGHT = 2
  UP = 3
  DOWN = 4

starting_blizzards = defaultdict(set)
directions = {
    '<': Direction.LEFT,
    '>': Direction.RIGHT,
    '^': Direction.UP,
    'v': Direction.DOWN
}

rows = f.read().splitlines()

m, n = len(rows) - 2, len(rows[0]) - 2

for i, row in enumerate(rows[1:-1]):
  for j, c in enumerate(row[1:-1]):
    if c in directions:
      starting_blizzards[(i, j)].add(directions[c])

def next_coord(i, j, direction):
  if direction == Direction.LEFT:
    return (i, (j - 1) % n)
  elif direction == Direction.RIGHT:
    return (i, (j + 1) % n)
  elif direction == Direction.UP:
    return ((i - 1) % m, j)
  else:
    return ((i + 1) % m, j)

def next_blizzards(blizzards):
  result = defaultdict(set)
  for (i, j), directions in blizzards.items():
    for dir in directions:
      nc = next_coord(i, j, dir)
      result[nc].add(dir)
  return result

blizzards = {0: next_blizzards(starting_blizzards)}

def get_next_blizzards(steps):
  if steps in blizzards:
    return blizzards[steps]
  blizzards[steps] = next_blizzards(blizzards[steps - 1])
  return blizzards[steps]

q = deque([((-1, 0), 0)])
visited = set()
while q:
  (i, j), steps = q.popleft()
  if (i, j) == (m - 1, n - 1):
    # answer: 281
    print(steps + 1)
    break
  key = (i, j, steps)
  if key in visited:
    continue
  visited.add(key)
  nb = get_next_blizzards(steps)
  for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
    if 0 <= n_i < m and 0 <= n_j < n and (n_i, n_j) not in nb:
      q.append(((n_i, n_j), steps + 1))
  if (i, j) not in nb:
    q.append(((i, j), steps + 1))
