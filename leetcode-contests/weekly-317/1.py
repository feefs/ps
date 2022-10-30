# 2455. Average Value of Even Numbers That Are Divisible by Three
class Solution:
  def averageValue(self, nums: List[int]) -> int:
    total, count = 0, 0
    for n in nums:
      if n % 2 == 0 and n % 3 == 0:
        total += n
        count += 1

    return total // count if count > 0 else 0
