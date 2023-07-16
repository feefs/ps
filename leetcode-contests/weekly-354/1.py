# 2778. Sum of Squares of Special Elements
class Solution:
  def sumOfSquares(self, nums: List[int]) -> int:
    n = len(nums)
    result = 0
    for i, num in enumerate(nums, 1):
      if n % i == 0:
        result += (num**2)

    return result
