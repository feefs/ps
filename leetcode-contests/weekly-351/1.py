# 2748. Number of Beautiful Pairs
class Solution:
  def countBeautifulPairs(self, nums: List[int]) -> int:
    n = len(nums)
    result = 0
    for i in range(n):
      for j in range(i + 1, n):
        d1, d2 = int(str(nums[i])[0]), int(str(nums[j])[-1])
        if math.gcd(d1, d2) == 1:
          result += 1

    return result
