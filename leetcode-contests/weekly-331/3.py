class Solution:
  def minCapability(self, nums: List[int], k: int) -> int:
    # binary search for the lowest valid capability value
    N = len(nums)
    lo, hi = min(nums), max(nums)
    while lo < hi:
      mid = (lo + hi) // 2
      count, i = 0, 0
      while i < N:
        """
        for each house nums[i], we can either rob it or skip it
        nums[i] > mid => we must skip it, otherwise we exceed the capability value we are testing
        if nums[i] <= mid, consider both cases for nums[i + 1]
          nums[i + 1] > mid => rob nums[i] since we will skip nums[i + 1] anyways
          nums[i + 1] <= mid
            nums[i + 2] might also be <= mid, so skipping nums[i] to rob only nums[i + 1] is strictly worse
            => rob nums[i]
        """
        if nums[i] <= mid:
          count += 1
          i += 1
        i += 1
      if count >= k:
        # we were able to rob at least k houses
        # => lowest valid capability value is at most mid
        hi = mid
      else:
        # lowest valid capability value must be mid + 1 or higher
        lo = mid + 1

    return lo
