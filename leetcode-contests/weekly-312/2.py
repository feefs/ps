# 2419. Longest Subarray With Maximum Bitwise AND
class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    max_value = float("-inf")
    result = 0
    cr_v = None
    cr_l = 0

    for n in nums:
      if n == cr_v:
        cr_l += 1
      else:
        cr_l = 1
      cr_v = n

      if cr_v > max_value:
        max_value = cr_v
        result = cr_l
      elif cr_v == max_value:
        # don't overwrite with shorter runs of the largest number
        result = max(result, cr_l)

    return result
