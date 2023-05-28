# 2711. Difference of Number of Distinct Values on Diagonals
class Solution:
  def differenceOfDistinctValues(self,
                                 grid: List[List[int]]) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    result = [[0 for _ in range(n)] for _ in range(m)]
    for col in reversed(range(n)):
      i, j = 0, col
      before, after = defaultdict(int), defaultdict(int)
      while i < m and j < n:
        after[grid[i][j]] += 1
        i += 1
        j += 1
      i, j = 0, col
      while i < m and j < n:
        after[grid[i][j]] -= 1
        before_distinct = len(list(filter(lambda p: p[1] != 0, before.items())))
        after_distinct = len(list(filter(lambda p: p[1] != 0, after.items())))
        result[i][j] = abs(before_distinct - after_distinct)
        before[grid[i][j]] += 1
        i += 1
        j += 1
    for row in range(1, m):
      i, j = row, 0
      before, after = defaultdict(int), defaultdict(int)
      while i < m and j < n:
        after[grid[i][j]] += 1
        i += 1
        j += 1
      i, j = row, 0
      while i < m and j < n:
        after[grid[i][j]] -= 1
        before_distinct = len(list(filter(lambda p: p[1] != 0, before.items())))
        after_distinct = len(list(filter(lambda p: p[1] != 0, after.items())))
        result[i][j] = abs(before_distinct - after_distinct)
        before[grid[i][j]] += 1
        i += 1
        j += 1

    return result
