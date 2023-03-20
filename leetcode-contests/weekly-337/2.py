# 2596. Check Knight Tour Configuration
class Solution:
  def checkValidGrid(self, grid: List[List[int]]) -> bool:
    if grid[0][0] != 0:
      return False
    n = len(grid)
    move = 0
    pos = (0, 0)
    while move < (n * n) - 1:
      i, j = pos
      for ni, nj in [(i - 1, j + 2), (i - 2, j + 1), (i - 2, j - 1),
                     (i - 1, j - 2), (i + 1, j - 2), (i + 2, j - 1),
                     (i + 2, j + 1), (i + 1, j + 2)]:
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == move + 1:
          pos = (ni, nj)
          break
      else:
        return False
      move += 1

    return True
