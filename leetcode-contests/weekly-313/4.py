# 2430. Maximum Deletions on a String
class Solution:
  def deleteString(self, s: str) -> int:
    """
    O(n^3) DP
    """
    n = len(s)

    # dp[i] = number of deletions to delete s[i:]
    dp = [1] * n
    for i in reversed(range(n)):
      for width in (i + 1 for i in range((n - i) // 2)):
        # avoid dp comparisons that can't improve the result
        if 1 + dp[i + width] > dp[i]:
          if s[i:i + width] == s[i + width:i + (2 * width)]:
            dp[i] = max(dp[i], 1 + dp[i + width])
    return dp[0]
