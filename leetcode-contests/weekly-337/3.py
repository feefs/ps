# 2597. The Number of Beautiful Subsets
class Solution:
  def beautifulSubsets(self, nums: List[int], k: int) -> int:
    """
    subsets backtracking
    |curr - prev| = k
      curr = k + prev
      curr = k - prev
    since all values in nums and k are positive, sorting means curr > prev
      only need to check curr - prev = k
      rearrange and check curr = k + prev
    check if curr is in the ugly set
    add k + curr to the ugly set otherwise
    """
    nums.sort()
    n = len(nums)

    def dfs(start, ugly):
      result = 1
      for i in range(start, n):
        curr = nums[i]
        if curr in ugly:
          continue
        # since duplicate subsets are allowed, there is no nums[i] == nums[i - 1] -> continue check
        # this also means we need a counter instead of just a set
        if k + curr not in ugly:
          ugly[k + curr] = 0
        ugly[k + curr] += 1
        result += dfs(i + 1, ugly)
        ugly[k + curr] -= 1
        if ugly[k + curr] == 0:
          ugly.pop(k + curr)
      return result

    # subtract 1 to exclude the empty set
    return dfs(0, {}) - 1
