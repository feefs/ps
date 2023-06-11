# 2733. Neither Minimum nor Maximum
class Solution:
  def findNonMinOrMax(self, nums: List[int]) -> int:
    mn, mx = min(nums), max(nums)
    for n in nums:
      if n != mn and n != mx:
        return n

    return -1
