# 2643. Row With Maximum Ones
class Solution:
  def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
    result = [-1, -1]
    for i, row in enumerate(mat):
      total = sum(row)
      if total > result[1]:
        result = [i, total]

    return result
