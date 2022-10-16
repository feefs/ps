# 2442. Count Number of Distinct Integers After Reverse Operations
class Solution:
  def countDistinctIntegers(self, nums: List[int]) -> int:
    s = set(nums)

    for n in nums:
      rev_num = 0
      while n > 0:
        rev_num *= 10
        rev_num += n % 10
        n //= 10
      s.add(rev_num)

    return len(s)
