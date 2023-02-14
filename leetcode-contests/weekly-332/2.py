# 2563. Count the Number of Fair Pairs
from sortedcontainers import SortedList

class Solution:
  def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    """
    similar idea to two sum
    use a sorted list/binary tree to answer how many inserted values are < or < a value n
    """
    sl = SortedList()
    result = 0
    for n in nums:
      """
      rewrite lower <= nums[i] + nums[j] <= upper by subtracting nums[j] from all sides
      => lower - nums[j] <= nums[i] <= upper - nums[j]
      for each iteration, there are three sections of numbers
      A <= B <= C
      |B + C| form all numbers >= A
      |A + B| form all numbers <= C
      to compute |B|, compute |A + B| - |A| or |B + C| - |C|
      bisect_left(n) computes how many values are < n
      bisect_right(n) computes how many values are <= n
      """
      # |A + B| = how many nums[i] values that satisfy nums[i] <= upper - nums[j]
      AB = sl.bisect_right(upper - n)
      # |A| = how many nums[i] values that satisfy nums[i] < lower - nums[j]
      A = sl.bisect_left(lower - n)
      # we can compute |B + C| = |A + B + C| - |A| and |C| = |A + B + C| - |A + B|
      # with |A + B + C| == len(sl) and by using |A| and |A + B| above
      result += AB - A
      # add current number to sorted list/binary tree data structure
      sl.add(n)

    return result
