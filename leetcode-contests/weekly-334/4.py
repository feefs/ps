# 2577. Minimum Time to Visit a Cell In a Grid
class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    """
    modified dijkstras
      if an adjacent cell needs more time, repeatedly revisit a previous cell and the current one
      check if we are stuck at the starting cell, otherwise a previous cell is guaranteed to exist
    """
    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1

    m, n = len(grid), len(grid[0])

    dist = defaultdict(lambda: float('inf'))
    dist[(0, 0)] = 0
    pq = [(0, (0, 0))]

    while pq:
      t, (i, j) = heapq.heappop(pq)
      # outdated value (a shorter path to (i, j) exists)
      if t > dist[(i, j)]:
        continue

      for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= n_i < m and 0 <= n_j < n:
          t_req = grid[n_i][n_j]
          if t + 1 >= t_req:
            if t + 1 < dist[(n_i, n_j)]:
              dist[(n_i, n_j)] = t + 1
              heapq.heappush(pq, (t + 1, (n_i, n_j)))
          else:
            # t + 2k + 1 >= t_req
            # repeatedly visit an adjacent unblocked cell k times to meet t_req
            # if remainder of t_req - t is 0, we need one extra step to move to n_i, n_j
            # if remainder of t_req - t is 1, we can move to n_i, n_j as the final step
            if (t_req - t) % 2 == 0:
              dist[(n_i, n_j)] = t_req + 1
              heapq.heappush(pq, (t_req + 1, (n_i, n_j)))
            else:
              dist[(n_i, n_j)] = t_req
              heapq.heappush(pq, (t_req, (n_i, n_j)))

    result = dist[(m - 1, n - 1)]

    return result if result != float('inf') else -1
