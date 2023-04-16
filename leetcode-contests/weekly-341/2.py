# 2644. Find the Maximum Divisibility Score
class Solution:
  def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
    result = float('inf')
    largest_score = 0
    for d in divisors:
      score = 0
      for n in nums:
        if n % d == 0:
          score += 1
      if score > largest_score:
        largest_score = score
        result = d
      elif score == largest_score:
        result = min(result, d)

    return result
