# 2779. Maximum Beauty of an Array After Applying Operation
class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    """
    sliding window approach, sort nums
    l_max = highest value nums[l] can be changed to
    r_max = smallest value nums[r] can be changed to
    nums is sorted
      => all indices in between l and r inclusive can form a subsequence with the same values
    """
    nums.sort()
    result = 0
    l, r = 0, 0
    while r < len(nums):
      l_max, r_min = nums[l] + k, nums[r] - k
      while l_max < r_min:
        l += 1
        l_max = nums[l] + k
      result = max(result, r - l + 1)
      r += 1

    return result
