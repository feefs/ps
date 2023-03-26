# 2600. K Items With the Maximum Sum
class Solution:
  def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int,
                           k: int) -> int:
    result = min(numOnes, k)
    k = max(0, k - numOnes)
    k = max(0, k - numZeros)
    result -= max(0, k)

    return result
