# 2507. Smallest Value After Replacing With Sum of Prime Factors
class Solution:
  def smallestValue(self, n: int) -> int:
    def prime_factors(n):
      result = []
      while n % 2 == 0:
        result.append(2)
        n //= 2
      for d in range(3, int(sqrt(n) + 1), 2):
        while n % d == 0:
          result.append(d)
          n //= d
      if n > 2:
        result.append(n)
      return result

    while (next_n := sum(prime_factors(n))) < n:
      n = next_n

    return n
