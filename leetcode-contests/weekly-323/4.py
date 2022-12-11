# 2503. Maximum Number of Points From Grid Queries
class Solution:
  def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
    """
    Compute the queries in sorted order for flood fill
      Use a dictionary to retrieve answers in order at the end
    """
    m, n = len(grid), len(grid[0])
    answers = {}
    visited = set()
    marked = 0
    pq = [(grid[0][0], 0, 0)]
    for q in sorted(queries):
      while pq and pq[0][0] < q:
        _, i, j = heapq.heappop(pq)
        if (i, j) in visited:
          continue
        visited.add((i, j))
        marked += 1
        for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
          if 0 <= n_i < m and 0 <= n_j < n:
            heapq.heappush(pq, (grid[n_i][n_j], n_i, n_j))
      answers[q] = marked

    return [answers[q] for q in queries]
