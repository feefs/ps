# 2501. Longest Square Streak in an Array
class Solution:
  def longestSquareStreak(self, nums: List[int]) -> int:
    values = set(nums)
    result = 0
    for n in nums:
      size = 1
      nxt = n**2
      while nxt in values:
        size += 1
        nxt = nxt**2
      result = max(result, size)

    return result if result >= 2 else -1
