# 2500. Delete Greatest Value in Each Row
class Solution:
  def deleteGreatestValue(self, grid: List[List[int]]) -> int:
    for row in grid:
      row.sort()
    m, n = len(grid), len(grid[0])
    result = 0
    for j in range(n):
      to_remove = float('-inf')
      for i in reversed(range(m)):
        to_remove = max(to_remove, grid[i][j])
      result += to_remove

    return result
