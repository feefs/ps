import os
import itertools
import heapq

f = open(os.path.join(os.path.dirname(__file__), "input.txt"))

matrix = f.read().splitlines()
matrix = [list(row) for row in matrix]

m, n = len(matrix), len(matrix[0])

start, destinations = None, []
for i in range(m):
  for j in range(n):
    if matrix[i][j] == 'S':
      matrix[i][j] = ord('a') - ord('a')
    elif matrix[i][j] == 'E':
      start = (i, j)
      matrix[i][j] = ord('z') - ord('a')
    else:
      matrix[i][j] = ord(matrix[i][j]) - ord('a')
    if matrix[i][j] == 0:
      destinations.append((i, j))

coordinates = set(itertools.product(range(m), range(n)))
coordinates.remove(start)

distances = {coord: float('inf') for coord in coordinates}
pq = [(float('inf'), coord) for coord in coordinates]
distances[start] = 0
heapq.heappush(pq, (0, start))
visited = set()

def next_cells(i, j):
  result = []
  for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
    if 0 <= n_i < m and 0 <= n_j < n:
      if matrix[n_i][n_j] >= matrix[i][j] - 1:
        result.append((n_i, n_j))
  return result

while pq:
  dist, (i, j) = heapq.heappop(pq)
  if (i, j) in visited:
    continue
  for next_coord in next_cells(i, j):
    distances[next_coord] = min(distances[next_coord], 1 + dist)
    heapq.heappush(pq, (distances[next_coord], next_coord))
  visited.add((i, j))

# answer: 375
print(min(distances[coord] for coord in destinations))
