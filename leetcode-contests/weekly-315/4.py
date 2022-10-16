# 2444. Count Subarrays With Fixed Bounds
class Solution:
  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    """
    cleaner approach that keeps track of the rightmost minK and maxK indices
    uses float('-inf') and min/max operations to derive l and if the current window is valid
    """
    l_bound = 0
    rightmost_minK = rightmost_maxK = float('-inf')
    result = 0

    for r, n in enumerate(nums):
      # advance entire window past r if n isn't in bounds
      if not minK <= n <= maxK:
        l_bound = r + 1
        rightmost_minK = rightmost_maxK = float('-inf')

      # update rightmost indices
      if n == minK:
        rightmost_minK = r
      if n == maxK:
        rightmost_maxK = r

      # min(rightmost_minK, rightmost_maxK) gets the leftmost index of the current window
      l = min(rightmost_minK, rightmost_maxK)

      # if the window is invalid, then the value will be float('-inf')
      # max and 0 used to represent this case
      result += max(0, (l - l_bound) + 1)

    return result

  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    """
    maintain "two" windows and use two pointers to advance the current window [l:r + 1]
    if the current value num[r] is not within bounds, advance all indices past this point
      exactly as if we restarted the problem with nums[r + 1:]
    if the current window is valid (its minimum and maximum values are minK and maxK)
      continuously expand "left window" rightwards as long as it would keep the current window valid
        "left window" is between l_bound and current window
      add l - l_bound + 1 to the result, which is the number of indices where a subarray starts and will end at r
    """
    l, r = 0, 0
    l_bound = 0
    # minK and maxK counts of the current window
    curr_min_c = curr_max_c = 0
    # minK and maxK counts of left window (between l_bound and current window)
    left_min_c = left_max_c = 0
    result = 0

    while r < len(nums):
      n = nums[r]
      # advance entire window past r if n isn't in bounds
      if not minK <= n <= maxK:
        l = l_bound = r + 1
        curr_min_c = curr_max_c = left_min_c = left_max_c = 0
        r += 1
        continue

      # update current window minK and maxK counts
      if n == minK:
        curr_min_c += 1
      if n == maxK:
        curr_max_c += 1

      # if current window is valid
      if curr_min_c >= 1 and curr_max_c >= 1:
        # continuously expand left window rightwards as long as it would keep the current window valid
        while curr_min_c - (left_min_c +
                            int(nums[l] == minK)) >= 1 and curr_max_c - (
                                left_max_c + int(nums[l] == maxK)) >= 1:
          # update left window minK and maxK counts
          if nums[l] == minK:
            left_min_c += 1
          if nums[l] == maxK:
            left_max_c += 1
          l += 1
        # l - l_bound subarrays end at r, add 1 because the values are indices
        result += (l - l_bound) + 1

      r += 1
    return result
