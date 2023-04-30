# 2661. First Completely Painted Row or Column
class Solution:
  def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    locations = {}
    for i in range(m):
      for j in range(n):
        locations[mat[i][j]] = (i, j)

    rows, cols = defaultdict(set), defaultdict(set)
    for index, value in enumerate(arr):
      i, j = locations[value]
      rows[i].add((i, j))
      cols[j].add((i, j))
      if len(rows[i]) == n or len(cols[j]) == m:
        return index
