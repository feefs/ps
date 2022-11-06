# 2461. Maximum Sum of Distinct Subarrays With Length K
class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    result = 0
    window = {}
    window_sum = 0
    for i in range(k):
      n = nums[i]
      window[n] = window.get(n, 0) + 1
      window_sum += n

    if len(window) == k:
      result = max(result, window_sum)

    for i in range(len(nums) - k):
      l, r = nums[i], nums[i + k]
      window_sum = window_sum - l + r
      window[l] -= 1
      if window[l] == 0:
        del window[l]
      window[r] = window.get(r, 0) + 1

      if len(window) == k and window_sum > result:
        result = window_sum

    return result
