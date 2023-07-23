# 2790. Maximum Number of Groups With Increasing Length
class Solution:
  def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
    # to form n groups, we must have at least 1 + 2 + ... + n elements
    usageLimits.sort()
    groups = 0
    have = 0
    for limit in usageLimits:
      have += limit
      # increase the number of groups if we have enough elements
      if have > groups:
        groups += 1
        have -= groups

    return groups
