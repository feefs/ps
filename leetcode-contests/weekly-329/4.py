# 2547. Minimum Cost to Split an Array
class Solution:
  def minCost(self, nums: List[int], k: int) -> int:
    n = len(nums)
    # f(i) = minCost to split the array nums[i:]
    @cache
    def f(i):
      if i == n:
        return 0
      result = float('inf')
      # d holds the character counts for the left subarray
      # left_trimmed is the trimmed value for the left subarray
      d = defaultdict(int)
      left_trimmed = 0
      for j in range(i, n):
        # update d and left_trimmed with nums[j]
        num = nums[j]
        d[num] += 1
        if d[num] == 2:
          left_trimmed += 1
        if d[num] >= 2:
          left_trimmed += 1
        # compute cost for splitting into nums[:j + 1] and nums[j + 1:]
        result = min(result, (k + left_trimmed) + f(j + 1))
      return result

    return f(0)
