# 2549. Count Distinct Numbers on Board
class Solution:
  def distinctIntegers(self, n: int) -> int:
    result = set()
    for i in range(1, n + 1):
      for j in range(i, n + 1):
        if j % i == 1:
          result.add(i)

    return len(result) + 1
