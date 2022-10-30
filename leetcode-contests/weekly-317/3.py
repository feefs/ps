# 2457. Minimum Addition to Make Integer Beautiful
class Solution:
  def makeIntegerBeautiful(self, n: int, target: int) -> int:
    total = sum([int(c) for c in str(n)])
    magnitude = 10
    cost = 0

    while total > target:
      cost += magnitude - (n % 10 * (magnitude // 10))
      n //= 10
      n += 1
      total = sum([int(c) for c in str(n)])
      magnitude *= 10

    return cost
