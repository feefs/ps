# 2684. Maximum Number of Moves in a Grid
class Solution:
  def maxMoves(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])

    @cache
    def dfs(i, j):
      result = 0
      for ni, nj in [(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]:
        if 0 <= ni < m and 0 <= nj < n:
          if grid[ni][nj] > grid[i][j]:
            result = max(result, 1 + dfs(ni, nj))
      return result

    result = 0
    for i in range(m):
      result = max(result, dfs(i, 0))

    return result
