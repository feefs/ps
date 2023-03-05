# 2585. Number of Ways to Earn Points
class Solution:
  def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
    # dp[v][i] = number of ways to reach v using types[i:]
    # coin change II with limits
    MOD = (10**9) + 7

    @cache
    def f(v, i):
      # there is one way to score 0 points
      if v == 0:
        return 1
      # there are no more questions we can solve
      if i == len(types):
        return 0
      result = 0
      count, point = types[i]
      for n in range(1, count + 1):
        v_remaining = v - (n * point)
        if v_remaining < 0:
          break
        # solve n questions of type i
        result += f(v_remaining, i + 1) % MOD
      # don't solve any of the questions of type i
      result += f(v, i + 1) % MOD
      return result % MOD

    return f(target, 0)
