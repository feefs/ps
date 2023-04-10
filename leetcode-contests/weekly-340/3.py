# 2616. Minimize the Maximum Difference of Pairs
class Solution:
  def minimizeMax(self, nums: List[int], p: int) -> int:
    # binary search for the resulting minimum maximum difference
    n = len(nums)
    nums.sort()
    lo, hi = 0, nums[-1] - nums[0]
    while lo < hi:
      mid = (lo + hi) // 2
      count = 0
      i = 0
      while i < n - 1:
        # greedily pairing numbers works because nums is sorted
        # pairing ab and cd can only be the same or better than ad and bc
        # b - a can be only be the same or better (less) than d - a
        # a <= b <= c <= d implies b <= d implies b - a <= d - a
        if nums[i + 1] - nums[i] <= mid:
          count += 1
          i += 2
        else:
          i += 1
      # if at least p pairs cannot be formed, the result must be higher
      if count < p:
        lo = mid + 1
      else:
        hi = mid

    return lo
