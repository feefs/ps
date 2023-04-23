# 2653. Sliding Subarray Beauty
from sortedcontainers import SortedList

class Solution:
  def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
    # maintain a window and use a SortedList for log(k) time operations
    n = len(nums)
    window, result = SortedList(), []
    for i in range(k):
      window.add(nums[i])

    for i in range(n - k):
      result.append(min(0, window[x - 1]))
      window.add(nums[i + k])
      window.remove(nums[i])
    result.append(min(0, window[x - 1]))

    return result
