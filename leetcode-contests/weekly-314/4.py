# 2435. Paths in Matrix Whose Sum Is Divisible by K
class Solution:
  def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
    """
    dp[i][j][v] = number of paths that end at (i, j) and sum up to (v mod k)
      for each value v at cell (i, j)
        value from left cell is dp[i][j - 1][v]
        value from above cell is dp[i - 1][j][v]
        compute resulting v mod k = v_curr = (v + grid[i][j]) % k
        dp[i][j][v_curr] += dp[i][j - 1][v] + dp[i - 1][j][v]
    """
    m, n = len(grid), len(grid[0])
    dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]

    # base cases
    dp[0][0][grid[0][0] % k] = 1
    for i in range(1, m):
      for v in range(k):
        dp[i][0][(v + grid[i][0]) % k] += dp[i - 1][0][v]
    for j in range(1, n):
      for v in range(k):
        dp[0][j][(v + grid[0][j]) % k] += dp[0][j - 1][v]

    for i in range(1, m):
      for j in range(1, n):
        for v in range(k):
          v_curr = (v + grid[i][j]) % k
          dp[i][j][v_curr] += dp[i - 1][j][v]
          dp[i][j][v_curr] += dp[i][j - 1][v]

        # keep values mod 10e9 + 7
        for v in range(k):
          dp[i][j][v] %= int(1e9) + 7

    return dp[m - 1][n - 1][0]
