# 2428. Maximum Sum of an Hourglass
class Solution:
  def maxSum(self, grid: List[List[int]]) -> int:
    r, c = len(grid), len(grid[0])
    verticals = (r - 3) + 1
    horizontals = (c - 3) + 1

    result = 0
    for v in range(verticals):
      for h in range(horizontals):
        top = grid[v][h] + grid[v][h + 1] + grid[v][h + 2]
        middle = grid[v + 1][h + 1]
        bottom = grid[v + 2][h] + grid[v + 2][h + 1] + grid[v + 2][h + 2]
        value = top + middle + bottom
        if value > result:
          result = value

    return result
