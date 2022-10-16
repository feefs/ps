# 2441. Largest Positive Integer That Exists With Its Negative
class Solution:
  def findMaxK(self, nums: List[int]) -> int:
    seen = set()
    largest_abs = 0

    for n in nums:
      if n in seen:
        largest_abs = max(largest_abs, abs(n))
      seen.add(-n)

    return largest_abs if largest_abs != 0 else -1
