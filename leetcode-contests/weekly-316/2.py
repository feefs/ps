# 2447. Number of Subarrays With GCD Equal to K
class Solution:
  def subarrayGCD(self, nums: List[int], k: int) -> int:
    def gcd(a, b):
      while b:
        a, b = b, a % b
      return a

    n = len(nums)
    result = 0
    for i in range(n):
      curr_gcd = nums[i]
      for j in range(i, n):
        curr_gcd = gcd(curr_gcd, nums[j])
        if curr_gcd == k:
          result += 1

    return result
