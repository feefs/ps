import os

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

matrix = f.read().splitlines()
m, n = len(matrix), len(matrix[0])
matrix = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]

visible = set()

for i in range(m):
  highest_so_far = -1
  for j in range(n):
    if matrix[i][j] > highest_so_far:
      visible.add((i, j))
      highest_so_far = matrix[i][j]

for i in range(m):
  highest_so_far = -1
  for j in reversed(range(n)):
    if matrix[i][j] > highest_so_far:
      visible.add((i, j))
      highest_so_far = matrix[i][j]

for j in range(m):
  highest_so_far = -1
  for i in range(n):
    if matrix[i][j] > highest_so_far:
      visible.add((i, j))
      highest_so_far = matrix[i][j]

for j in range(m):
  highest_so_far = -1
  for i in reversed(range(n)):
    if matrix[i][j] > highest_so_far:
      visible.add((i, j))
      highest_so_far = matrix[i][j]

# answer: 1792
print(len(visible))
