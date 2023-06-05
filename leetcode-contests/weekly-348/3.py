# 2718. Sum of Matrix After Queries
class Solution:
  def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
    used_rows, used_cols = set(), set()
    row_count, col_count = n, n
    result = 0
    for t, i, v in reversed(queries):
      if t == 0:
        if i not in used_rows:
          used_rows.add(i)
          col_count -= 1
          result += v * row_count
      else:
        if i not in used_cols:
          used_cols.add(i)
          row_count -= 1
          result += v * col_count

    return result
