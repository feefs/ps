import os
from collections import defaultdict, deque

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

elves = set()
for i, row in enumerate(f.read().splitlines()):
  for j in range(len(row)):
    if row[j] == '#':
      elves.add((i, j))

def check_north(i, j):
  if all([(n_i, n_j) not in elves
          for n_i, n_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]]):
    return (i - 1, j)
  else:
    return None

def check_south(i, j):
  if all([(n_i, n_j) not in elves
          for n_i, n_j in [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]]):
    return (i + 1, j)
  else:
    return None

def check_west(i, j):
  if all([(n_i, n_j) not in elves
          for n_i, n_j in [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1)]]):
    return (i, j - 1)
  else:
    return None

def check_east(i, j):
  if all([(n_i, n_j) not in elves
          for n_i, n_j in [(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]]):
    return (i, j + 1)
  else:
    return None

def check_no_neighbors(i, j):
  for n_i, n_j in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                   (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
    if (n_i, n_j) in elves:
      return False
  return True

propose_order = deque([check_north, check_south, check_west, check_east])

for _ in range(10):
  proposed_moves = defaultdict(set)
  for i, j in sorted(elves):
    if check_no_neighbors(i, j):
      continue
    for propose in propose_order:
      if proposed_move := propose(i, j):
        proposed_moves[proposed_move].add((i, j))
        break
  for proposed_move, elf in proposed_moves.items():
    if len(elf) == 1:
      elves.remove(list(elf)[0])
      elves.add(proposed_move)
  propose_order.rotate(-1)

min_i, max_i = float('inf'), float('-inf')
min_j, max_j = float('inf'), float('-inf')
for i, j in elves:
  min_i = min(min_i, i)
  max_i = max(max_i, i)
  min_j = min(min_j, j)
  max_j = max(max_j, j)

area = (max_i - min_i + 1) * (max_j - min_j + 1)

# answer: 3996
print(area - len(elves))
