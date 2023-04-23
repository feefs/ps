# 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    # if at least one 1 exists, we can propagate 1s to the non-1 values in n - num_ones operations
    num_ones = sum([(1 if n == 1 else 0) for n in nums])
    if num_ones > 0:
      return n - num_ones

    # test all contiguous subarrays increasing by width
    for width in range(2, n + 1):
      for start in range(n - width + 1):
        # if any subarray has a gcd of 1, it will take width - 1 gcd operations to obtain a 1
        # it will then take n - 1 operations to propagate that 1 to all the other non-1 values
        if math.gcd(*nums[start:start + width]) == 1:
          return (width - 1) + (n - 1)

    return -1
