# 2712. Minimum Cost to Make All Characters Equal
class Solution:
  def minimumCost(self, s: str) -> int:
    """
    flipping can make at most two adjacent characters match each other
    check all adjacent characters s[i] and s[i - 1]
      greedily flip s[:i] or s[i:] to make the two adjacent characters match
    """
    n = len(s)
    result = 0
    for i in range(1, n):
      if s[i] != s[i - 1]:
        result += min(i, n - i)

    return result
