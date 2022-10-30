# 2427. Number of Common Factors
class Solution:
  def commonFactors(self, a: int, b: int) -> int:
    if a < b:
      a, b = b, a

    result = 0
    for n in range(1, b + 1):
      if a % n == 0 and b % n == 0:
        result += 1

    return result
