# 2617. Minimum Number of Visited Cells in a Grid
class Solution:
  def minimumVisitedCells(self, grid: List[List[int]]) -> int:
    # bfs
    m, n = len(grid), len(grid[0])
    q = deque([((0, 0), 1)])
    added = {(0, 0)}
    while q:
      next_q = deque([])
      while q:
        (i, j), cells = q.popleft()
        if (i, j) == (m - 1, n - 1):
          return cells
        # heuristic: add coordinates to the queue starting from the right or bottom of the range
        # these coordinates are closer to the end
        for k in reversed(range(j + 1, min(n, j + grid[i][j] + 1))):
          if (i, k) not in added:
            next_q.append(((i, k), cells + 1))
            added.add((i, k))
        for k in reversed(range(i + 1, min(m, i + grid[i][j] + 1))):
          if (k, j) not in added:
            next_q.append(((k, j), cells + 1))
            added.add((k, j))
      q = next_q

    return -1
