# 2572. Count the Number of Square-Free Subsets
class Solution:
  def squareFreeSubsets(self, nums: List[int]) -> int:
    # compute valid numbers that can be in a square-free subset
    # numbers 2 to 30 that aren't divisible by a square in that same range
    # subsets including 1 are handled separately at the end
    valid_nums = [
        n for n in range(2, 31) if all([n % sq != 0 for sq in [4, 9, 16, 25]])
    ]

    counts = Counter(nums)
    MOD = 10**9 + 7

    def f(arr):
      if not arr:
        return 1
      valid_n = arr[0]
      # knapsack dp
      # filter valid numbers based on them being coprime to valid_n
      # multiply by the count of that number in nums to count subsets using valid_n
      dont_use_valid_n = f(arr[1:])
      use_valid_n = counts[valid_n] * f(
          [n for n in arr if math.gcd(n, valid_n) == 1])
      return (use_valid_n + dont_use_valid_n) % MOD

    one_subsets = (2**counts[1]) % MOD
    nums_subsets = f(valid_nums)

    # multiply subsets with 1 by the subsets with valid numbers to get total subsets
    # subtract 1 to exclude the empty subset
    return ((one_subsets * nums_subsets) - 1) % MOD
