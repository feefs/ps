import os
from enum import Enum
"""
Use a monotonically decreasing queue (left to right), implemented as a stack
We only care about trees that are taller than the current position's tree in a direction
Move in the opposite direction while updating the queue and computing the value
Repeat for all four directions and then combine them for the answer
"""

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

matrix = f.read().splitlines()
m, n = len(matrix), len(matrix[0])
matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

class Direction(Enum):
  LEFT = 1
  RIGHT = 2
  UP = 3
  DOWN = 4

visible = {
    Direction.LEFT: [[0 for _ in range(n)] for _ in range(m)],
    Direction.RIGHT: [[0 for _ in range(n)] for _ in range(m)],
    Direction.UP: [[0 for _ in range(n)] for _ in range(m)],
    Direction.DOWN: [[0 for _ in range(n)] for _ in range(m)]
}

for i in range(m):
  stack = [(float('inf'), 0)]
  for j in range(n):
    tree_height = matrix[i][j]
    while stack[-1][0] < tree_height:
      stack.pop()
    visible[Direction.LEFT][i][j] = j - stack[-1][1]
    stack.append((tree_height, j))

for i in range(m):
  stack = [(float('inf'), n - 1)]
  for j in reversed(range(n)):
    tree_height = matrix[i][j]
    while stack[-1][0] < tree_height:
      stack.pop()
    visible[Direction.RIGHT][i][j] = stack[-1][1] - j
    stack.append((tree_height, j))

for j in range(n):
  stack = [(float('inf'), 0)]
  for i in range(m):
    tree_height = matrix[i][j]
    while stack[-1][0] < tree_height:
      stack.pop()
    visible[Direction.UP][i][j] = i - stack[-1][1]
    stack.append((tree_height, i))

for j in range(n):
  stack = [(float('inf'), m - 1)]
  for i in reversed(range(m)):
    tree_height = matrix[i][j]
    while stack[-1][0] < tree_height:
      stack.pop()
    visible[Direction.DOWN][i][j] = stack[-1][1] - i
    stack.append((tree_height, i))

highest_scenic_score = 0
for i in range(m):
  for j in range(n):
    highest_scenic_score = max(
        highest_scenic_score,
        visible[Direction.LEFT][i][j] * visible[Direction.RIGHT][i][j] *
        visible[Direction.UP][i][j] * visible[Direction.DOWN][i][j])

# answer: 334880
print(highest_scenic_score)
