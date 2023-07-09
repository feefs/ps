# 2770. Maximum Number of Jumps to Reach the Last Index
class Solution:
  def maximumJumps(self, nums: List[int], target: int) -> int:
    n = len(nums)
    # dp[i] = maximum number of jumps from i to the end, -1 if not possible
    dp = [-1 for _ in range(n)]
    dp[-1] = 0
    for j in reversed(range(n)):
      if dp[j] == -1:
        continue
      for i in reversed(range(j)):
        if abs(nums[j] - nums[i]) <= target:
          dp[i] = max(dp[i], 1 + dp[j])

    return dp[0]
